# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T07:52:28.342480+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11560`

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

- `market_context_high->unknown_24h` score `210.9626` n `88` status `ready` deltaP `6.0318` edge `17.5541` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `89.0394` n `88` status `ready` deltaP `7.2201` edge `7.4166` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `30.5279` n `52` status `ready` deltaP `23.9486` edge `2.4455` maxDD `-3.2263`
- `market_context_high->equity_24h` score `15.2961` n `88` status `ready` deltaP `16.5185` edge `1.4037` maxDD `-16.7984`
- `news_risk_high->crypto_major_24h` score `12.6168` n `52` status `ready` deltaP `37.9491` edge `1.5611` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.494` n `53` status `ready` deltaP `34.7158` edge `0.8386` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.8027` n `52` status `ready` deltaP `40.1384` edge `0.2993` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.267` n `88` status `ready` deltaP `34.9638` edge `0.9516` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8765` n `88` status `ready` deltaP `35.0071` edge `0.2283` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3135` n `53` status `ready` deltaP `41.5181` edge `0.1203` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.1266` n `53` status `ready` deltaP `22.1152` edge `0.3452` maxDD `-9.2335`
- `news_risk_high->index_24h` score `4.0705` n `52` status `ready` deltaP `21.0074` edge `0.2252` maxDD `-0.4168`
- `news_risk_high->equity_1h` score `3.5754` n `53` status `ready` deltaP `18.464` edge `0.2461` maxDD `-3.6997`
- `market_context_high->index_24h` score `2.9386` n `88` status `ready` deltaP `16.9864` edge `0.1779` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7688` n `53` status `ready` deltaP `24.8821` edge `0.0902` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2934` n `53` status `ready` deltaP `25.8887` edge `0.2853` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2337` n `53` status `ready` deltaP `21.3558` edge `0.0874` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1091` n `53` status `ready` deltaP `25.1412` edge `0.0336` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3556` n `53` status `ready` deltaP `17.7748` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7885` n `53` status `ready` deltaP `19.2407` edge `0.078` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
