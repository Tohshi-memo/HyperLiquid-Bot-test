# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T11:22:29.196556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5897`

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

- `market_context_high->crypto_alt_24h` score `12.1011` n `40` status `ready` deltaP `51.4583` edge `0.7051` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `10.8575` n `40` status `ready` deltaP `51.1458` edge `0.5766` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.6804` n `31` status `ready` deltaP `-6.668` edge `0.2529` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9591` n `31` status `ready` deltaP `20.1371` edge `0.0099` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9293` n `31` status `ready` deltaP `12.192` edge `0.0614` maxDD `-1.5526`
- `market_context_high->commodity_1h` score `0.3572` n `47` status `ready` deltaP `7.7143` edge `0.0318` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.3421` n `31` status `ready` deltaP `13.8572` edge `-0.0138` maxDD `-1.6728`
- `market_context_high->commodity_4h` score `0.2995` n `47` status `ready` deltaP `4.7289` edge `0.0915` maxDD `-2.7703`
- `news_risk_high->index_4h` score `0.2909` n `31` status `ready` deltaP `0.2409` edge `0.0607` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1525` n `31` status `ready` deltaP `5.0453` edge `0.0362` maxDD `-0.356`
- `news_risk_high->crypto_alt_1h` score `0.1272` n `31` status `ready` deltaP `12.3382` edge `-0.0019` maxDD `-3.1233`
- `news_risk_high->index_1h` score `0.0387` n `31` status `ready` deltaP `3.9405` edge `-0.0015` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.017` n `47` status `ready` deltaP `6.8161` edge `-0.0087` maxDD `-0.7804`
- `market_context_high->fx_4h` score `-0.1291` n `47` status `ready` deltaP `12.046` edge `-0.0054` maxDD `-1.8531`
- `news_risk_high->fx_1h` score `-0.2279` n `31` status `ready` deltaP `-0.1159` edge `0.0027` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.3268` n `47` status `ready` deltaP `1.839` edge `0.0364` maxDD `-4.9116`
- `news_risk_high->metal_1h` score `-0.5816` n `31` status `ready` deltaP `-2.2117` edge `-0.0018` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.6827` n `40` status `ready` deltaP `0.6597` edge `0.0367` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.7355` n `31` status `ready` deltaP `3.7087` edge `-0.047` maxDD `-3.762`
- `news_risk_high->equity_1h` score `-0.9378` n `31` status `ready` deltaP `-9.7112` edge `0.0268` maxDD `-2.916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
