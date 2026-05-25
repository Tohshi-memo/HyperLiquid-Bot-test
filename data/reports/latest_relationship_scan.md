# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T05:37:16.493355+00:00`
- Price records: `672`
- Market context records: `1813`
- Flow alert records: `7117`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4514`

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

- `market_context_high->crypto_alt_4h` score `7.1062` n `183` status `ready` deltaP `23.1232` edge `0.5525` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8596` n `178` status `ready` deltaP `27.5905` edge `0.6303` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.6739` n `183` status `ready` deltaP `27.115` edge `0.5` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5473` n `30` status `ready` deltaP `29.563` edge `0.414` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7365` n `183` status `ready` deltaP `17.6846` edge `0.4792` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6682` n `178` status `ready` deltaP `17.8683` edge `0.3094` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3321` n `30` status `ready` deltaP `25.3194` edge `0.1406` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9641` n `183` status `ready` deltaP `15.6537` edge `0.2521` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.8469` n `178` status `ready` deltaP `18.4925` edge `0.6038` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.3461` n `178` status `ready` deltaP `12.9975` edge `0.6409` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9065` n `30` status `ready` deltaP `21.6362` edge `-0.0008` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8018` n `183` status `ready` deltaP `11.3572` edge `0.1` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.5114` n `189` status `ready` deltaP `6.335` edge `0.099` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4279` n `189` status `ready` deltaP `6.8744` edge `0.1012` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3971` n `30` status `ready` deltaP `9.9796` edge `0.0567` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.0941` n `189` status `ready` deltaP `4.4301` edge `0.042` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2225` n `178` status `ready` deltaP `17.9912` edge `0.7201` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.3592` n `178` status `ready` deltaP `10.0461` edge `0.008` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3747` n `189` status `ready` deltaP `0.3961` edge `0.0125` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4419` n `30` status `ready` deltaP `16.7066` edge `-0.1208` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
