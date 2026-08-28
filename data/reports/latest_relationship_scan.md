# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T19:07:23.046183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.4798` n `50` status `ready` deltaP `14.0381` edge `4.4464` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.0502` n `50` status `ready` deltaP `44.7002` edge `2.5003` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.4981` n `60` status `ready` deltaP `23.3841` edge `0.8165` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `6.2262` n `50` status `ready` deltaP `23.8614` edge `0.4091` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `5.9179` n `50` status `ready` deltaP `30.1005` edge `0.3853` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.347` n `50` status `ready` deltaP `43.4073` edge `0.0771` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `3.7886` n `120` status `ready` deltaP `7.3714` edge `0.3398` maxDD `-3.1917`
- `news_risk_high->fx_4h` score `3.6731` n `60` status `ready` deltaP `43.3638` edge `0.0302` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.4011` n `70` status `ready` deltaP `9.1532` edge `0.2581` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.1642` n `120` status `ready` deltaP `28.7406` edge `0.174` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.377` n `50` status `ready` deltaP `26.9948` edge `0.0332` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3005` n `120` status `ready` deltaP `17.5508` edge `0.1154` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9023` n `120` status `ready` deltaP `9.3913` edge `0.0576` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6407` n `70` status `ready` deltaP `12.9256` edge `0.0059` maxDD `-0.094`
- `news_risk_high->commodity_1h` score `0.4512` n `70` status `ready` deltaP `12.7759` edge `0.0047` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0409` n `120` status `ready` deltaP `13.1504` edge `0.0093` maxDD `-3.3377`
- `news_risk_high->index_4h` score `-0.3055` n `60` status `ready` deltaP `3.7805` edge `-0.0136` maxDD `-1.0618`
- `news_risk_high->metal_4h` score `-0.3615` n `60` status `ready` deltaP `9.8171` edge `-0.0241` maxDD `-3.0158`
- `market_context_high->fx_1h` score `-0.4122` n `120` status `ready` deltaP `3.1637` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4439` n `70` status `ready` deltaP `-0.586` edge `-0.0097` maxDD `-0.7981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
