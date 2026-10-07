# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T07:07:34.015476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `988.3786` n `110` status `ready` deltaP `10.2904` edge `82.3343` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `31.4636` n `110` status `ready` deltaP `-1.4024` edge `2.6852` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8744` n `62` status `ready` deltaP `34.6184` edge `0.6124` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5663` n `62` status `ready` deltaP `22.0201` edge `0.5348` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6892` n `110` status `ready` deltaP `17.2284` edge `0.289` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3188` n `62` status `ready` deltaP `23.7847` edge `0.118` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8518` n `62` status `ready` deltaP `32.0024` edge `0.0505` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.1726` n `62` status `ready` deltaP `4.4859` edge `0.1611` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.05` n `62` status `ready` deltaP `7.3305` edge `0.1575` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9528` n `62` status `ready` deltaP `24.7248` edge `0.0129` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8076` n `62` status `ready` deltaP `17.0142` edge `0.097` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.582` n `110` status `ready` deltaP `1.1696` edge `0.2964` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3791` n `62` status `ready` deltaP `19.7236` edge `0.0869` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.0973` n `110` status `ready` deltaP `7.7651` edge `0.3863` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9572` n `62` status `ready` deltaP `2.4097` edge `0.1156` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8674` n `110` status `ready` deltaP `19.4179` edge `0.0185` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.769` n `110` status `ready` deltaP `13.1655` edge `0.0047` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.6457` n `62` status `ready` deltaP `27.1954` edge `0.0581` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.2903` n `110` status `ready` deltaP `9.9889` edge `0.0276` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2408` n `110` status `ready` deltaP `6.9624` edge `0.0121` maxDD `-0.4094`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
