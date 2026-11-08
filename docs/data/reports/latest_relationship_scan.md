# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T20:52:25.168542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6597`

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

- `market_context_high->unknown_4h` score `81.8254` n `39` status `ready` deltaP `-4.6591` edge `6.8946` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.2112` n `37` status `ready` deltaP `11.7681` edge `0.7853` maxDD `-31.3588`
- `market_context_high->fx_4h` score `2.6916` n `39` status `ready` deltaP `28.768` edge `0.0415` maxDD `-0.0521`
- `market_context_high->equity_1h` score `2.436` n `48` status `ready` deltaP `9.0818` edge `0.1884` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.803` n `39` status `ready` deltaP `23.8743` edge `0.0381` maxDD `-2.4279`
- `market_context_high->index_24h` score `1.1416` n `37` status `ready` deltaP `14.3441` edge `0.1138` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8402` n `37` status `ready` deltaP `10.9422` edge `0.0059` maxDD `-0.0397`
- `market_context_high->crypto_alt_1h` score `0.468` n `48` status `ready` deltaP `7.3228` edge `0.0717` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.2837` n `48` status `ready` deltaP `3.2809` edge `0.0292` maxDD `-0.1947`
- `market_context_high->crypto_major_1h` score `0.2192` n `48` status `ready` deltaP `4.9276` edge `0.0523` maxDD `-3.0172`
- `market_context_high->commodity_1h` score `0.1191` n `48` status `ready` deltaP `9.2066` edge `0.0085` maxDD `-1.7019`
- `market_context_high->metal_1h` score `0.1091` n `48` status `ready` deltaP `4.4661` edge `0.0121` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.0646` n `37` status `ready` deltaP `3.0875` edge `0.1072` maxDD `-6.5601`
- `market_context_high->commodity_4h` score `-0.0663` n `39` status `ready` deltaP `1.7121` edge `0.0255` maxDD `-1.633`
- `market_context_high->fx_1h` score `-0.1519` n `48` status `ready` deltaP `0.7111` edge `0.0097` maxDD `-0.1681`
- `market_context_high->equity_4h` score `-0.6687` n `39` status `ready` deltaP `22.2522` edge `0.0939` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8126` n `39` status `ready` deltaP `-3.6664` edge `-0.0347` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9627` n `39` status `ready` deltaP `16.1664` edge `0.0131` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.7018` n `37` status `ready` deltaP `6.6583` edge `-0.1309` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8242` n `39` status `ready` deltaP `2.0989` edge `-0.1077` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
