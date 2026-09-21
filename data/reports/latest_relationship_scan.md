# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T06:07:31.022287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9198`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `33.9001` n `58` status `ready` deltaP `1.23` edge `2.8318` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.0863` n `98` status `ready` deltaP `11.7489` edge `2.6147` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.7345` n `98` status `ready` deltaP `12.3158` edge `1.9672` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.5432` n `101` status `ready` deltaP `19.9861` edge `0.3663` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0215` n `101` status `ready` deltaP `21.5105` edge `0.3175` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7834` n `101` status `ready` deltaP `16.5308` edge `0.1683` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1288` n `101` status `ready` deltaP `18.1775` edge `0.1085` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2225` n `98` status `ready` deltaP `23.643` edge `0.1297` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0608` n `58` status `ready` deltaP `7.9548` edge `0.0607` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8406` n `58` status `ready` deltaP `12.0741` edge `0.0151` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6329` n `101` status `ready` deltaP `14.7477` edge `0.0146` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.4094` n `58` status `ready` deltaP `16.0008` edge `0.0095` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.3972` n `101` status `ready` deltaP `15.422` edge `0.0357` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3549` n `58` status `ready` deltaP `6.2978` edge `0.0184` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3187` n `58` status `ready` deltaP `8.4762` edge `0.0057` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1797` n `101` status `ready` deltaP `8.3358` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0141` n `101` status `ready` deltaP `3.5676` edge `0.0156` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1561` n `58` status `ready` deltaP `-1.6415` edge `0.0698` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2304` n `101` status `ready` deltaP `2.8428` edge `0.0062` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3248` n `98` status `ready` deltaP `10.1226` edge `-0.0247` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
