## 제로 트러스트 (Zero Trust)

- 제로 트러스트 용어 시작: 2010년, 존 킨더박
- 요약: 아무것도 믿지 마라.
- 신뢰할 수 있는 네트워크 포기 필요
- 전통적인 네트워크에는 보안 경계 개념 존재
- 보안 경계: 나쁜 세상은 외부, 내부는 안전한 공간
- 보안 경계 작동하지 않으면 침입 가능
- 침입 후, 내부 네트워크의 느슨한 규칙과 신뢰로 적의 작업 용이
- 제로 트러스트 유행 원인: 구글, 원격 근무, 통신 속도, 인증 기술 발달
- 해결책: 제로 트러스트 네트워킹, 모든 연결 인증, 트래픽 암호화, 모든 기록
- 목표: 손상된 사용자 자격 증명 남용, 원격 악용, 내부자 위협 방지, 악의적 활동 영향 완화

## Zero Trust 네트워크로 전환하는 법

- Microsegmentation: 중심 신뢰 네트워크에서 제로 트러스트로 전환 기술
- 전통적인 네트워크: 1개 세그먼트, 큰 네트워크에서 작은 기계 세트 차단
- 액세스 제어 규칙 사용하여 두 개 세그먼트로 분할
- 프로세스 반복, 세그먼트 작아질 때까지 분할, 마이크로세그먼팅
- 각 마이크로세그먼트에 하나 머신 포함: 제로 트러스트 네트워크

## 왜 제로 트러스트가 유행하는가?

- 기존 소프트웨어로는 안전하지 않은 프로그래밍 방식 대비 필요
- 네트워크 모델에서 신뢰는 개인 수준 확인
- 개별 기반 인증, 액세스 제어 확장
- 제로 트러스트 컴퓨팅: 인터넷 모든 것 연결, 분산된 액세스 결정

## 중세와 현

- 중세 유럽 가톨릭 교회 정보 독점권
- 인쇄기 등장, 신뢰에 대한 새로운 종류가 생성되어 최종적으로는 가톨릭을 붕괴
- 인터넷으로 모든 사람은 출판자될 수 있으나 그만큼 다양한 정보들이 마음대로 공유
- 제로 트러스트: 모든 자원 부패 위협, 인증 + 권한 부여 + 암호화 필요

## 제로 트러스트 구현

- 제로 트러스트 원칙: 인증 + 권한 부여 + 암호화
- 사용자와 컴퓨터 인증
- 최소 권한 원칙에 따른 권한 부여
- 모든 통신 암호화
- 중앙 집중식 ID 거버넌스, 역할 기반 액세스 제어 사용
- 악의적 클라이언트 피해 제한
- 정보가 어디서 시작하든 통신 암호화 필요