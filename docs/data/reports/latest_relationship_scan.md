# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T06:07:30.994354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `90.3271` n `150` status `ready` deltaP `-29.625` edge `8.016` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1719` n `32` status `ready` deltaP `-43.75` edge `4.6195` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1719` n `32` status `ready` deltaP `-43.75` edge `4.6195` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0138` n `36` status `ready` deltaP `10.0694` edge `0.8053` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.129` n `36` status `ready` deltaP `38.2622` edge `0.339` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7841` n `32` status `ready` deltaP `32.2917` edge `0.1834` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8946` n `32` status `ready` deltaP `20.1982` edge `0.1248` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8946` n `32` status `ready` deltaP `20.1982` edge `0.1248` maxDD `-0.1258`
- `market_context_high->commodity_24h` score `2.857` n `150` status `ready` deltaP `22.2917` edge `0.1698` maxDD `-2.4263`
- `news_risk_high->index_24h` score `2.2875` n `36` status `ready` deltaP `14.5833` edge `0.0934` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7043` n `36` status `ready` deltaP `20.0711` edge `0.0214` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.629` n `36` status `ready` deltaP `8.4332` edge `0.1114` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.533` n `150` status `ready` deltaP `16.7399` edge `0.08` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.3042` n `32` status `ready` deltaP `13.8099` edge `0.0399` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3042` n `32` status `ready` deltaP `13.8099` edge `0.0399` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2203` n `32` status `ready` deltaP `11.6319` edge `0.1945` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2203` n `32` status `ready` deltaP `11.6319` edge `0.1945` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.1984` n `32` status `ready` deltaP `14.2361` edge `0.0234` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1984` n `32` status `ready` deltaP `14.2361` edge `0.0234` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
