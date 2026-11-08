# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T18:37:27.347815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5607`

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

- `market_context_high->unknown_4h` score `63.145` n `39` status `ready` deltaP `-4.6591` edge `5.3379` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.773` n `37` status `ready` deltaP `13.3306` edge `0.8217` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3523` n `39` status `ready` deltaP `12.5864` edge `0.2414` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7294` n `39` status `ready` deltaP `29.2253` edge `0.0416` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8577` n `39` status `ready` deltaP `24.4841` edge `0.0386` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1537` n `39` status `ready` deltaP `14.0642` edge `0.0839` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1153` n `39` status `ready` deltaP `11.8187` edge `0.0727` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0832` n `37` status `ready` deltaP `13.476` edge `0.1121` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8018` n `37` status `ready` deltaP `10.9422` edge `0.0027` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5075` n `39` status `ready` deltaP `8.2643` edge `0.0143` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.234` n `39` status `ready` deltaP `2.9288` edge `0.0375` maxDD `-0.1621`
- `market_context_high->commodity_24h` score `0.2183` n `37` status `ready` deltaP `3.0875` edge `0.1269` maxDD `-6.5601`
- `market_context_high->commodity_1h` score `0.0738` n `39` status `ready` deltaP `8.0954` edge `0.0101` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0191` n `39` status `ready` deltaP `2.1803` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1295` n `39` status `ready` deltaP `0.7974` edge `0.0235` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6175` n `39` status `ready` deltaP `22.862` edge `0.0964` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9863` n `39` status `ready` deltaP `15.8615` edge `0.0121` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.8808` n `37` status `ready` deltaP `5.0958` edge `-0.1354` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.886` n `39` status `ready` deltaP `1.6416` edge `-0.1098` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
