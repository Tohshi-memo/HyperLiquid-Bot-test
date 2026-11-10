# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T21:22:27.899818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11752`

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

- `market_context_high->unknown_4h` score `55.9667` n `88` status `ready` deltaP `7.525` edge `4.6585` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2568` n `88` status `ready` deltaP `33.6489` edge `2.9542` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.5296` n `88` status `ready` deltaP `28.5985` edge `1.1559` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.8942` n `88` status `ready` deltaP `29.7664` edge `0.339` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.8816` n `88` status `ready` deltaP `23.911` edge `0.0527` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3825` n `88` status `ready` deltaP `2.8375` edge `0.0003` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4072` n `88` status `ready` deltaP `3.1982` edge `0.0124` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.4947` n `88` status `ready` deltaP `5.2245` edge `-0.0005` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5201` n `88` status `ready` deltaP `3.4091` edge `0.0212` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0094` n `88` status `ready` deltaP `-0.4434` edge `0.0119` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0104` n `88` status `ready` deltaP `-7.8048` edge `0.0056` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2323` n `88` status `ready` deltaP `-12.7109` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5855` n `88` status `ready` deltaP `-7.5054` edge `0.0314` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.7636` n `88` status `ready` deltaP `3.6458` edge `-0.0113` maxDD `-3.4642`
- `market_context_high->crypto_alt_1h` score `-1.8142` n `88` status `ready` deltaP `1.2316` edge `-0.0429` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8163` n `88` status `ready` deltaP `-1.5798` edge `-0.0042` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-2.9507` n `88` status `ready` deltaP `-3.7629` edge `-0.0909` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.7873` n `88` status `ready` deltaP `2.7439` edge `-0.1194` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.6323` n `88` status `ready` deltaP `5.4136` edge `0.4904` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.0585` n `88` status `ready` deltaP `5.1414` edge `-0.194` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
