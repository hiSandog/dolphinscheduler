# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Test resource definition."""

from pydolphinscheduler.core.resource_definition import ResourceDefinition


def test_sql_get_define():
    """Test resource set attributes which get with same type."""
    user = "admin"
    name = "test"
    suffix = "py"
    current_dir = "/dev"
    content = """print("hello world")"""
    description = "hello world"
    expect = {
        "user": user,
        "name": name,
        "suffix": suffix,
        "currentDir": current_dir,
        "content": content,
        "description": description,
    }
    resourceDefinition = ResourceDefinition(
        user=user,
        name=name,
        suffix=suffix,
        current_dir=current_dir,
        content=content,
        description=description,
    )
    assert resourceDefinition.get_define() == expect
