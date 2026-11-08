# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T18:52:27.119616+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `56`

- Symbol pattern count: `5608`

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

- `market_context_high->unknown_4h` score `66.1642` n `39` status `ready` deltaP `-4.6591` edge `5.5895` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.7159` n `37` status `ready` deltaP `13.157` edge `0.8181` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.4665` n `40` status `ready` deltaP `13.3982` edge `0.2455` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.7172` n `39` status `ready` deltaP `29.0729` edge `0.0416` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8443` n `39` status `ready` deltaP `24.3316` edge `0.0385` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.4026` n `40` status `ready` deltaP `14.9401` edge `0.0988` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.2754` n `40` status `ready` deltaP `12.6946` edge `0.0802` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0847` n `37` status `ready` deltaP `13.476` edge `0.1123` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8066` n `37` status `ready` deltaP `10.9422` edge `0.0031` maxDD `-0.0397`
- `market_context_high->index_1h` score `0.4442` n `40` status `ready` deltaP `3.997` edge `0.0374` maxDD `-0.1621`
- `market_context_high->fx_1h` score `0.3805` n `40` status `ready` deltaP `6.8114` edge `0.0134` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.2003` n `37` status `ready` deltaP `3.0875` edge `0.1246` maxDD `-6.5601`
- `market_context_high->metal_1h` score `0.0525` n `40` status `ready` deltaP `3.2485` edge `0.0155` maxDD `-0.6226`
- `market_context_high->commodity_1h` score `-0.0249` n `40` status `ready` deltaP `6.7066` edge `0.0067` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.1192` n `39` status `ready` deltaP `0.9499` edge `0.0238` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.6294` n `39` status `ready` deltaP `22.7095` edge `0.0959` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9926` n `39` status `ready` deltaP `15.8615` edge `0.0113` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-1.8597` n `37` status `ready` deltaP `5.2694` edge `-0.1348` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8872` n `39` status `ready` deltaP `1.6416` edge `-0.1099` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
