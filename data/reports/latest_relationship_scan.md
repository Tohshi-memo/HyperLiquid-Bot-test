# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T19:22:26.646680+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5618`

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

- `market_context_high->unknown_4h` score `69.6874` n `39` status `ready` deltaP `-4.6591` edge `5.8831` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.6138` n `37` status `ready` deltaP `12.8097` edge `0.8119` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3565` n `42` status `ready` deltaP `12.6533` edge `0.2413` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.6916` n `39` status `ready` deltaP `28.768` edge `0.0415` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8164` n `39` status `ready` deltaP `24.0268` edge `0.0382` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.3873` n `42` status `ready` deltaP `14.3142` edge `0.1017` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1737` n `42` status `ready` deltaP `12.0687` edge `0.0759` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0977` n `37` status `ready` deltaP `13.6496` edge `0.1128` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.815` n `37` status `ready` deltaP `10.9422` edge `0.0038` maxDD `-0.0397`
- `market_context_high->index_1h` score `0.5964` n `42` status `ready` deltaP `5.9595` edge `0.037` maxDD `-0.1621`
- `market_context_high->metal_1h` score `0.2059` n `42` status `ready` deltaP `5.211` edge `0.0152` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `0.1652` n `37` status `ready` deltaP `3.0875` edge `0.1201` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.1484` n `42` status `ready` deltaP `4.1346` edge `0.0119` maxDD `-0.1681`
- `market_context_high->commodity_1h` score `-0.0513` n `42` status `ready` deltaP `6.3801` edge `0.0055` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0987` n `39` status `ready` deltaP `1.2547` edge `0.0244` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6546` n `39` status `ready` deltaP `22.4047` edge `0.0947` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7991` n `39` status `ready` deltaP `-3.3615` edge `-0.035` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-1.0011` n `39` status `ready` deltaP `15.8615` edge `0.0102` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.8175` n `37` status `ready` deltaP `5.6166` edge `-0.1336` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8944` n `39` status `ready` deltaP `1.6416` edge `-0.1105` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
