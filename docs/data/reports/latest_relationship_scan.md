# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T14:52:27.740888+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4781`

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

- `market_context_high->unknown_4h` score `30.1696` n `39` status `ready` deltaP `-4.2018` edge `2.5869` maxDD `-0.9139`
- `market_context_high->equity_24h` score `6.1437` n `37` status `ready` deltaP `15.4139` edge `0.8387` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.3392` n `39` status `ready` deltaP `12.287` edge `0.2423` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.783` n `39` status `ready` deltaP `29.8351` edge `0.042` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8491` n `39` status `ready` deltaP `24.3316` edge `0.0389` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.2616` n `39` status `ready` deltaP `14.9624` edge `0.0869` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1836` n `39` status `ready` deltaP `12.5672` edge `0.0734` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.8963` n `37` status `ready` deltaP `10.8718` edge `0.1055` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7358` n `37` status `ready` deltaP `10.9422` edge `-0.0028` maxDD `-0.0397`
- `market_context_high->commodity_24h` score `0.5564` n `37` status `ready` deltaP `5.3445` edge `0.1552` maxDD `-6.5601`
- `market_context_high->fx_1h` score `0.5207` n `39` status `ready` deltaP `8.414` edge `0.0144` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.2254` n `39` status `ready` deltaP `2.7791` edge `0.0374` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0738` n `39` status `ready` deltaP `8.0954` edge `0.0101` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0362` n `39` status `ready` deltaP `1.8809` edge `0.0156` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1049` n `39` status `ready` deltaP `1.2547` edge `0.0236` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5789` n `39` status `ready` deltaP `23.3193` edge `0.0983` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.8173` n `39` status `ready` deltaP `-3.6664` edge `-0.0353` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.8979` n `39` status `ready` deltaP `16.1664` edge `0.0214` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.2139` n `37` status `ready` deltaP `2.4916` edge `-0.1458` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.7834` n `39` status `ready` deltaP `2.0989` edge `-0.1043` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
