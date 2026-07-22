# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T14:07:29.298291+00:00`
- Price records: `672`
- Market context records: `7571`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14496`

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

- `market_context_high->commodity_4h` score `0.2682` n `167` status `ready` deltaP `10.1339` edge `0.0308` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.0907` n `167` status `ready` deltaP `5.5493` edge `0.0079` maxDD `-1.5217`
- `market_context_high->commodity_24h` score `-0.2096` n `153` status `ready` deltaP `12.4024` edge `0.0582` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2668` n `167` status `ready` deltaP `4.7823` edge `0.0031` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4553` n `167` status `ready` deltaP `11.575` edge `0.0371` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.4778` n `167` status `ready` deltaP `1.5024` edge `0.0001` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.818` n `167` status `ready` deltaP `-0.5988` edge `0.0095` maxDD `-1.4971`
- `market_context_high->crypto_alt_1h` score `-0.8192` n `167` status `ready` deltaP `-0.5988` edge `0.0012` maxDD `-5.8454`
- `market_context_high->crypto_major_1h` score `-0.8288` n `167` status `ready` deltaP `4.6407` edge `0.0035` maxDD `-7.5892`
- `market_context_high->fx_24h` score `-0.8708` n `153` status `ready` deltaP `8.4694` edge `0.015` maxDD `-3.8554`
- `market_context_high->unknown_4h` score `-1.0173` n `167` status `ready` deltaP `10.0117` edge `0.0387` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-1.1972` n `167` status `ready` deltaP `1.1976` edge `-0.0454` maxDD `-1.3217`
- `market_context_high->unknown_24h` score `-1.2764` n `154` status `ready` deltaP `5.9388` edge `0.0671` maxDD `-9.9598`
- `market_context_high->equity_1h` score `-1.3672` n `167` status `ready` deltaP `3.903` edge `0.0254` maxDD `-13.4699`
- `market_context_high->metal_4h` score `-1.4648` n `167` status `ready` deltaP `1.0945` edge `0.0531` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.5774` n `167` status `ready` deltaP `3.3575` edge `0.2121` maxDD `-21.9375`
- `market_context_high->crypto_alt_4h` score `-1.6985` n `167` status `ready` deltaP `0.3213` edge `0.0356` maxDD `-13.7735`
- `market_context_high->fx_4h` score `-2.079` n `167` status `ready` deltaP `-0.8973` edge `0.0012` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.4198` n `167` status `ready` deltaP `4.6654` edge `0.0366` maxDD `-22.5675`
- `market_context_high->index_24h` score `-3.8895` n `153` status `ready` deltaP `-18.8017` edge `0.0013` maxDD `-15.3023`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
