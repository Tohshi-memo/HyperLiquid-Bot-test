# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T00:07:26.549382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9036`

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

- `news_risk_high->crypto_major_24h` score `24.8069` n `98` status `ready` deltaP `12.7906` edge `2.6678` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3019` n `98` status `ready` deltaP `15.0935` edge `2.0793` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.676` n `101` status `ready` deltaP `20.5958` edge `0.3733` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8473` n `101` status `ready` deltaP `20.4434` edge `0.3101` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7426` n `101` status `ready` deltaP `16.5308` edge `0.1649` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.034` n `101` status `ready` deltaP `18.0278` edge `0.1016` maxDD `-2.8494`
- `market_context_high->fx_1h` score `1.0537` n `51` status `ready` deltaP `14.4359` edge `0.0095` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9826` n `98` status `ready` deltaP `22.2541` edge `0.1082` maxDD `-3.4467`
- `market_context_high->fx_4h` score `0.8109` n `43` status `ready` deltaP `13.0212` edge `0.009` maxDD `-0.2586`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `market_context_high->equity_1h` score `0.6064` n `51` status `ready` deltaP `5.3951` edge `0.0399` maxDD `-0.36`
- `news_risk_high->metal_4h` score `0.5826` n `101` status `ready` deltaP `16.7939` edge `0.042` maxDD `-2.0994`
- `market_context_high->index_1h` score `0.565` n `51` status `ready` deltaP `8.6885` edge `0.0147` maxDD `-0.0435`
- `market_context_high->commodity_4h` score `0.4264` n `43` status `ready` deltaP `20.682` edge `-0.0103` maxDD `-2.4997`
- `news_risk_high->fx_4h` score `0.2237` n `101` status `ready` deltaP `8.9456` edge `0.0226` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.2127` n `98` status `ready` deltaP `15.0085` edge `0.0586` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.159` n `51` status `ready` deltaP `4.4529` edge `0.0145` maxDD `-0.1415`
- `news_risk_high->equity_1h` score `0.0339` n `101` status `ready` deltaP `4.0167` edge `0.0166` maxDD `-0.9112`
- `market_context_high->index_4h` score `0.0301` n `43` status `ready` deltaP `10.9259` edge `-0.0053` maxDD `-1.0949`
- `news_risk_high->metal_24h` score `-0.037` n `98` status `ready` deltaP `13.4212` edge `-0.0098` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
