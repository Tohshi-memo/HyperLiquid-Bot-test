# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T07:22:22.561142+00:00`
- Price records: `672`
- Market context records: `3050`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `25.3857` n `99` status `ready` deltaP `13.7626` edge `2.4154` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.4771` n `99` status `ready` deltaP `24.6686` edge `1.0051` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.4368` n `99` status `ready` deltaP `44.4602` edge `0.8474` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.8651` n `99` status `ready` deltaP `24.9369` edge `1.3737` maxDD `-18.3486`
- `market_context_high->index_24h` score `9.3844` n `99` status `ready` deltaP `23.8321` edge `0.7487` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.7291` n `129` status `ready` deltaP `18.321` edge `0.17` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1431` n `134` status `ready` deltaP `1.1909` edge `0.0224` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4658` n `129` status `ready` deltaP `1.6981` edge `0.0552` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.4967` n `134` status `ready` deltaP `3.7358` edge `0.0177` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5377` n `134` status `ready` deltaP `-4.7725` edge `0.0` maxDD `-0.303`
- `market_context_high->crypto_alt_1h` score `-0.6071` n `134` status `ready` deltaP `5.9746` edge `0.0953` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7009` n `134` status `ready` deltaP `3.28` edge `0.0296` maxDD `-8.3065`
- `market_context_high->crypto_major_1h` score `-0.9528` n `134` status `ready` deltaP `4.491` edge `0.0742` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-0.9589` n `134` status `ready` deltaP `4.3168` edge `-0.0356` maxDD `-3.1801`
- `market_context_high->index_4h` score `-0.9701` n `129` status `ready` deltaP `12.4078` edge `0.0622` maxDD `-16.8761`
- `market_context_high->fx_4h` score `-1.1038` n `129` status `ready` deltaP `-8.1785` edge `-0.0035` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.179` n `134` status `ready` deltaP `-1.7763` edge `-0.0025` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.2133` n `99` status `ready` deltaP `-0.0631` edge `-0.0135` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9298` n `129` status `ready` deltaP `9.8423` edge `0.0515` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.1677` n `129` status `ready` deltaP `18.1745` edge `0.2772` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
