# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T08:07:26.442551+00:00`
- Price records: `672`
- Market context records: `2644`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.6143` n `133` status `ready` deltaP `17.8271` edge `0.5485` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.4698` n `133` status `ready` deltaP `25.4126` edge `0.5543` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `4.5772` n `133` status `ready` deltaP `7.4327` edge `0.7795` maxDD `-27.8092`
- `market_context_high->crypto_major_4h` score `4.017` n `133` status `ready` deltaP `16.3281` edge `0.4069` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.1701` n `133` status `ready` deltaP `7.1222` edge `0.155` maxDD `-3.7312`
- `market_context_high->index_24h` score `1.1457` n `133` status `ready` deltaP `11.5875` edge `0.1163` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.1334` n `133` status `ready` deltaP `10.3035` edge `0.1445` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5861` n `133` status `ready` deltaP `7.449` edge `0.1186` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4873` n `133` status `ready` deltaP `11.0032` edge `0.0514` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.09` n `133` status `ready` deltaP `3.5467` edge `0.038` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.1972` n `133` status `ready` deltaP `3.2507` edge `0.0113` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.2558` n `133` status `ready` deltaP `4.7863` edge `0.0284` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.2692` n `133` status `ready` deltaP `6.5407` edge `0.0218` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4097` n `133` status `ready` deltaP `0.9883` edge `0.0039` maxDD `-0.2373`
- `market_context_high->fx_24h` score `-0.6461` n `133` status `ready` deltaP `5.1718` edge `-0.0004` maxDD `-0.7001`
- `market_context_high->metal_1h` score `-0.7024` n `133` status `ready` deltaP `-0.0765` edge `0.0059` maxDD `-2.114`
- `market_context_high->fx_4h` score `-0.948` n `133` status `ready` deltaP `-1.0063` edge `0.0108` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0438` n `133` status `ready` deltaP `-2.5843` edge `0.0141` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.1666` n `133` status `ready` deltaP `3.8098` edge `0.0193` maxDD `-10.2078`
- `market_context_high->equity_24h` score `-1.3367` n `133` status `ready` deltaP `9.0395` edge `-0.0739` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
