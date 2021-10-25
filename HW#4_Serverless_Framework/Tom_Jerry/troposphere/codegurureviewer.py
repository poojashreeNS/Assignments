# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 18.6.0


from . import AWSObject


class RepositoryAssociation(AWSObject):
    resource_type = "AWS::CodeGuruReviewer::RepositoryAssociation"

    props = {
        "ConnectionArn": (str, False),
        "Name": (str, True),
        "Owner": (str, False),
        "Type": (str, True),
    }
