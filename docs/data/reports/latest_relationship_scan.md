# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T17:22:29.061376+00:00`
- Price records: `672`
- Market context records: `6729`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `market_context_high->unknown_24h` score `1.3634` n `176` status `ready` deltaP `2.7935` edge `0.5314` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0006` n `176` status `ready` deltaP `7.9512` edge `0.0329` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1184` n `176` status `ready` deltaP `5.3484` edge `0.0309` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.347` n `176` status `ready` deltaP `0.4831` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3706` n `176` status `ready` deltaP `7.9704` edge `0.1028` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5889` n `176` status `ready` deltaP `-0.7179` edge `0.0007` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.611` n `176` status `ready` deltaP `-0.0034` edge `-0.01` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.656` n `176` status `ready` deltaP `-4.5421` edge `-0.0013` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.0704` n `176` status `ready` deltaP `3.7051` edge `-0.0112` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2082` n `176` status `ready` deltaP `6.5964` edge `-0.0109` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2154` n `176` status `ready` deltaP `7.5388` edge `0.0003` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5074` n `176` status `ready` deltaP `-2.2311` edge `-0.0294` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.9444` n `176` status `ready` deltaP `-7.7742` edge `-0.0201` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.1598` n `176` status `ready` deltaP `6.0976` edge `0.0139` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3669` n `176` status `ready` deltaP `3.5892` edge `0.0128` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.605` n `176` status `ready` deltaP `-6.3193` edge `-0.0058` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.9085` n `176` status `ready` deltaP `5.5987` edge `-0.1115` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9896` n `176` status `ready` deltaP `-18.0017` edge `0.0241` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3587` n `176` status `ready` deltaP `-8.7437` edge `-0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.6092` n `176` status `ready` deltaP `-9.1225` edge `-0.0662` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
