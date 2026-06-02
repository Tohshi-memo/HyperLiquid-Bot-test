# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T23:22:20.919709+00:00`
- Price records: `672`
- Market context records: `2709`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `10.7191` n `111` status `ready` deltaP `16.3523` edge `1.1336` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.611` n `111` status `ready` deltaP `17.1312` edge `0.6362` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8612` n `143` status `ready` deltaP `6.0965` edge `0.1361` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2681` n `143` status `ready` deltaP `12.2282` edge `0.037` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `0.2065` n `111` status `ready` deltaP `6.5175` edge `0.7393` maxDD `-44.169`
- `market_context_high->index_1h` score `-0.1308` n `143` status `ready` deltaP `3.4997` edge `0.0093` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2722` n `143` status `ready` deltaP `2.4497` edge `0.0338` maxDD `-3.1587`
- `market_context_high->fx_1h` score `-0.4045` n `143` status `ready` deltaP `0.9998` edge `0.004` maxDD `-0.2164`
- `market_context_high->crypto_alt_4h` score `-0.4451` n `143` status `ready` deltaP `16.3633` edge `0.2879` maxDD `-28.7261`
- `market_context_high->commodity_1h` score `-0.4704` n `143` status `ready` deltaP `1.6991` edge `0.0037` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.4722` n `143` status `ready` deltaP `6.5942` edge `0.0715` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7045` n `143` status `ready` deltaP `-0.8009` edge `-0.0004` maxDD `-3.0996`
- `market_context_high->fx_24h` score `-0.7254` n `111` status `ready` deltaP `5.0911` edge `-0.0072` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-0.896` n `143` status `ready` deltaP `-1.049` edge `0.0102` maxDD `-0.5631`
- `market_context_high->crypto_major_1h` score `-0.9198` n `143` status `ready` deltaP `3.6473` edge `0.0447` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.1177` n `143` status `ready` deltaP `3.6479` edge `0.0244` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.138` n `111` status `ready` deltaP `5.5321` edge `0.1266` maxDD `-12.4171`
- `market_context_high->equity_1h` score `-1.2331` n `143` status `ready` deltaP `-4.4857` edge `0.011` maxDD `-2.7085`
- `market_context_high->index_24h` score `-1.4035` n `111` status `ready` deltaP `1.4124` edge `-0.0283` maxDD `-2.5127`
- `market_context_high->equity_4h` score `-1.9875` n `143` status `ready` deltaP `-0.8816` edge `-0.0193` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
