# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T17:27:44.840852+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9994`

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

- `market_context_high->unknown_24h` score `535.5734` n `64` status `ready` deltaP `3.8128` edge `44.6057` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.1826` n `50` status `ready` deltaP `50.3917` edge `3.4999` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.5001` n `64` status `ready` deltaP `46.7667` edge `3.2174` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.5666` n `64` status `ready` deltaP `62.37` edge `2.4891` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.3521` n `50` status `ready` deltaP `46.2149` edge `2.8001` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2959` n `50` status `ready` deltaP `39.372` edge `0.8752` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.2028` n `50` status `ready` deltaP `18.87` edge `1.5046` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1377` n `64` status `ready` deltaP `49.5586` edge `0.3564` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.7126` n `50` status `ready` deltaP `44.3674` edge `0.2636` maxDD `0.0`
- `market_context_high->metal_24h` score `6.6755` n `64` status `ready` deltaP `63.0578` edge `0.5246` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5435` n `50` status `ready` deltaP `42.2461` edge `0.294` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.3123` n `50` status `ready` deltaP `22.9756` edge `0.4271` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.9344` n `50` status `ready` deltaP `44.689` edge `0.1509` maxDD `-1.0104`
- `market_context_high->crypto_major_24h` score `4.6263` n `64` status `ready` deltaP `13.2149` edge `1.2312` maxDD `-69.0352`
- `news_risk_high->crypto_alt_4h` score `4.5864` n `50` status `ready` deltaP `26.9939` edge `0.3458` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9408` n `50` status `ready` deltaP `20.8982` edge `0.2521` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.7403` n `50` status `ready` deltaP `34.8963` edge `0.1044` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6609` n `50` status `ready` deltaP `25.8659` edge `0.0843` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1873` n `50` status `ready` deltaP `24.994` edge `0.0411` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2567` n `50` status `ready` deltaP `16.7485` edge `0.0232` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
