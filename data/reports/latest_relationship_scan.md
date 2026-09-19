# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T22:22:25.543185+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8700`

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

- `news_risk_high->crypto_major_24h` score `51.11` n `72` status `ready` deltaP `27.0833` edge `4.1678` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.5592` n `72` status `ready` deltaP `33.507` edge `3.6278` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `21.4177` n `109` status `ready` deltaP `-4.7647` edge `1.8399` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.6507` n `72` status `ready` deltaP `36.9792` edge `0.4786` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9506` n `109` status `ready` deltaP `39.6104` edge `0.451` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.7778` n `98` status `ready` deltaP `21.6183` edge `0.4583` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4955` n `98` status `ready` deltaP `22.3805` edge `0.3512` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3312` n `98` status `ready` deltaP `18.9234` edge `0.198` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.967` n `109` status `ready` deltaP `29.3564` edge `0.0878` maxDD `-0.2343`
- `news_risk_high->crypto_major_1h` score `2.4846` n `98` status `ready` deltaP `20.2707` edge `0.1242` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.699` n `72` status `ready` deltaP `22.3958` edge `0.0767` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.5537` n `111` status `ready` deltaP `18.9257` edge `0.0285` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.0855` n `109` status `ready` deltaP `20.515` edge `0.0005` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7455` n `98` status `ready` deltaP `18.2149` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.5357` n `72` status `ready` deltaP `3.4723` edge `0.0397` maxDD `-0.1231`
- `news_risk_high->equity_1h` score `0.4438` n `98` status `ready` deltaP `6.9657` edge `0.0311` maxDD `-0.9112`
- `market_context_high->fx_24h` score `0.4167` n `109` status `ready` deltaP `9.4993` edge `-0.0244` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.2166` n `111` status `ready` deltaP `6.3212` edge `0.0017` maxDD `-0.063`
- `news_risk_high->equity_4h` score `-0.1349` n `98` status `ready` deltaP `7.989` edge `0.0799` maxDD `-5.2186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
