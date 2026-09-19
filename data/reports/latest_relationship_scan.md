# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T23:29:47.392018+00:00`
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

- `news_risk_high->crypto_major_24h` score `51.0536` n `72` status `ready` deltaP `27.0833` edge `4.1631` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.4115` n `72` status `ready` deltaP `33.1598` edge `3.6178` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `15.8658` n `105` status `ready` deltaP `-5.254` edge `1.3805` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.5384` n `72` status `ready` deltaP `36.8055` edge `0.4704` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9622` n `105` status `ready` deltaP `39.2609` edge `0.4543` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8866` n `98` status `ready` deltaP `22.2281` edge `0.4633` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5751` n `98` status `ready` deltaP `22.6854` edge `0.3558` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.4336` n `105` status `ready` deltaP `31.7524` edge `0.0923` maxDD `-0.0943`
- `news_risk_high->crypto_alt_1h` score `3.2305` n `98` status `ready` deltaP `18.3246` edge `0.1936` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4319` n `98` status `ready` deltaP `19.9713` edge `0.1218` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.693` n `72` status `ready` deltaP `22.3958` edge `0.0762` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.6194` n `107` status `ready` deltaP `19.5674` edge `0.0297` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.1436` n `105` status `ready` deltaP `21.1208` edge `0.0013` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7577` n `98` status `ready` deltaP `18.3673` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.6009` n `72` status `ready` deltaP `4.1667` edge `0.0405` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.4887` n `105` status `ready` deltaP `10.1587` edge `-0.0228` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4174` n `98` status `ready` deltaP `6.6663` edge `0.0309` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.2407` n `107` status `ready` deltaP `6.5924` edge `0.0019` maxDD `-0.063`
- `news_risk_high->fx_4h` score `-0.1561` n `98` status `ready` deltaP `4.3181` edge `0.0218` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
