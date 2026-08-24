# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T04:37:27.662151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `51.5979` n `51` status `ready` deltaP `17.0139` edge `4.1864` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3935` n `51` status `ready` deltaP `40.237` edge `1.0243` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9485` n `51` status `ready` deltaP `23.4965` edge `0.927` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.8216` n `51` status `ready` deltaP `48.9481` edge `0.174` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.5538` n `51` status `ready` deltaP `16.0355` edge `0.2197` maxDD `-0.7693`
- `news_risk_high->equity_4h` score `3.3709` n `51` status `ready` deltaP `25.4035` edge `0.1886` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.2236` n `51` status `ready` deltaP `37.9304` edge `0.0292` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.218` n `145` status `ready` deltaP `21.3194` edge `0.0564` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `1.9731` n `51` status `ready` deltaP `36.2336` edge `-0.0729` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `1.695` n `51` status `ready` deltaP `25.8681` edge `-0.0312` maxDD `0.0`
- `news_risk_high->fx_1h` score `1.2314` n `51` status `ready` deltaP `16.8457` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8937` n `51` status `ready` deltaP `17.7439` edge `0.0327` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8305` n `51` status `ready` deltaP `12.7869` edge `0.0237` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2317` n `51` status `ready` deltaP `9.1229` edge `0.0042` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2195` n `51` status `ready` deltaP `8.8382` edge `-0.0098` maxDD `-0.4666`
- `market_context_high->fx_24h` score `-0.0101` n `92` status `ready` deltaP `10.2129` edge `0.0115` maxDD `-1.4708`
- `news_risk_high->metal_4h` score `-0.0537` n `51` status `ready` deltaP `8.435` edge `-0.0076` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1208` n `51` status `ready` deltaP `2.043` edge `-0.0068` maxDD `-0.1184`
- `market_context_high->commodity_24h` score `-0.2166` n `92` status `ready` deltaP `-5.2235` edge `0.0721` maxDD `-2.204`
- `market_context_high->unknown_1h` score `-0.4026` n `157` status `ready` deltaP `8.8418` edge `-0.0476` maxDD `-1.5916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
