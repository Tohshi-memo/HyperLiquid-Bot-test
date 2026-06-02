# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T05:52:19.733357+00:00`
- Price records: `672`
- Market context records: `2634`
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

- `market_context_high->unknown_24h` score `7.5066` n `142` status `ready` deltaP `18.1607` edge `0.5373` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0909` n `142` status `ready` deltaP `24.9957` edge `0.5255` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3569` n `142` status `ready` deltaP `14.5418` edge `0.3638` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.4286` n `142` status `ready` deltaP `4.2058` edge `0.6967` maxDD `-37.7883`
- `market_context_high->index_24h` score `1.3381` n `142` status `ready` deltaP `11.5023` edge `0.1329` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2647` n `142` status `ready` deltaP `10.7742` edge `0.1523` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0836` n `142` status `ready` deltaP `7.6305` edge `0.1444` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6604` n `142` status `ready` deltaP `8.0628` edge `0.1207` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.3574` n `142` status `ready` deltaP `9.3803` edge `0.0514` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1705` n `142` status `ready` deltaP `3.5992` edge `0.0112` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.2854` n `142` status `ready` deltaP `6.338` edge `0.0218` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.2976` n `142` status `ready` deltaP `2.4901` edge `0.0153` maxDD `-1.8692`
- `market_context_high->metal_1h` score `-0.5511` n `142` status `ready` deltaP `-0.2109` edge `0.0035` maxDD `-2.8194`
- `market_context_high->fx_1h` score `-0.6925` n `142` status `ready` deltaP `-1.1976` edge `0.0033` maxDD `-0.2422`
- `market_context_high->metal_4h` score `-0.7757` n `142` status `ready` deltaP `2.9178` edge `0.0288` maxDD `-4.0314`
- `market_context_high->commodity_4h` score `-0.8662` n `142` status `ready` deltaP `5.4019` edge `0.0472` maxDD `-10.2078`
- `market_context_high->fx_24h` score `-0.9628` n `142` status `ready` deltaP `2.7313` edge `-0.0029` maxDD `-1.3101`
- `market_context_high->fx_4h` score `-1.0188` n `142` status `ready` deltaP `-1.7713` edge `0.01` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0437` n `142` status `ready` deltaP `-2.2834` edge `0.0121` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.4174` n `142` status `ready` deltaP `1.2946` edge `0.0137` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
