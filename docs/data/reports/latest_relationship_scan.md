# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T17:52:27.892284+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.4377` n `32` status `ready` deltaP `40.3963` edge `0.3505` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.5635` n `32` status `ready` deltaP `17.7083` edge `0.3262` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.5635` n `32` status `ready` deltaP `17.7083` edge `0.3262` maxDD `-6.2481`
- `news_risk_high->index_4h` score `2.3622` n `32` status `ready` deltaP `25.6098` edge `0.0393` maxDD `-0.0546`
- `risk_on_high->commodity_4h` score `2.1904` n `32` status `ready` deltaP `14.7104` edge `0.1027` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1904` n `32` status `ready` deltaP `14.7104` edge `0.1027` maxDD `-0.1258`
- `risk_on_high->commodity_24h` score `1.764` n `32` status `ready` deltaP `16.3194` edge `0.0382` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.764` n `32` status `ready` deltaP `16.3194` edge `0.0382` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7454` n `36` status `ready` deltaP `8.7326` edge `0.1191` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.6807` n `32` status `ready` deltaP `18.75` edge `0.0335` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6807` n `32` status `ready` deltaP `18.75` edge `0.0335` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1437` n `32` status `ready` deltaP `12.4626` edge `0.0355` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1437` n `32` status `ready` deltaP `12.4626` edge `0.0355` maxDD `-0.1957`
- `risk_on_high->equity_24h` score `1.1339` n `32` status `ready` deltaP `3.6458` edge `0.299` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `1.1339` n `32` status `ready` deltaP `3.6458` edge `0.299` maxDD `-11.2348`
- `risk_on_high->index_24h` score `1.0766` n `32` status `ready` deltaP `10.7639` edge `0.0484` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.0766` n `32` status `ready` deltaP `10.7639` edge `0.0484` maxDD `-0.4355`
- `risk_on_high->fx_4h` score `0.9243` n `32` status `ready` deltaP `10.5945` edge `0.0205` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9243` n `32` status `ready` deltaP `10.5945` edge `0.0205` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7193` n `172` status `ready` deltaP `10.4226` edge `0.0543` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
