# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T23:07:18.980341+00:00`
- Price records: `672`
- Market context records: `2505`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.369` n `123` status `ready` deltaP `19.8213` edge `0.3481` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.5617` n `151` status `ready` deltaP `21.5756` edge `0.5042` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8311` n `151` status `ready` deltaP `17.8596` edge `0.3812` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.149` n `123` status `ready` deltaP `12.4915` edge `0.5815` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.8799` n `151` status `ready` deltaP `11.0745` edge `0.1878` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7193` n `158` status `ready` deltaP `7.3164` edge `0.1299` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5503` n `158` status `ready` deltaP `7.6158` edge `0.1145` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.3759` n `123` status `ready` deltaP `2.5999` edge `0.7266` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.1038` n `123` status `ready` deltaP `4.1285` edge `0.0792` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1077` n `151` status `ready` deltaP `6.9264` edge `0.029` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1407` n `123` status `ready` deltaP `18.297` edge `0.019` maxDD `-6.8828`
- `market_context_high->fx_1h` score `-0.2677` n `158` status `ready` deltaP `2.1981` edge `0.0045` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.396` n `158` status `ready` deltaP `2.4843` edge `0.0224` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4069` n `158` status `ready` deltaP `3.8657` edge `0.0099` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5202` n `158` status `ready` deltaP `-0.1421` edge `0.007` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.6718` n `151` status `ready` deltaP `1.8929` edge `0.04` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.6886` n `151` status `ready` deltaP `-1.6081` edge `0.0084` maxDD `-0.8774`
- `market_context_high->metal_1h` score `-0.8245` n `158` status `ready` deltaP `0.0815` edge `0.0067` maxDD `-3.0759`
- `market_context_high->fx_24h` score `-0.8691` n `123` status `ready` deltaP `3.2309` edge `0.0045` maxDD `-2.6633`
- `market_context_high->equity_1h` score `-0.8727` n `158` status `ready` deltaP `-0.1004` edge `0.0118` maxDD `-2.7085`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
