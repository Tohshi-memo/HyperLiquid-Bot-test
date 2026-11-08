# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T22:52:28.083426+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6527`

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

- `market_context_high->unknown_4h` score `31.9715` n `44` status `ready` deltaP `-2.633` edge `2.7266` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.752` n `37` status `ready` deltaP `11.2472` edge `0.7505` maxDD `-31.3588`
- `market_context_high->fx_4h` score `1.5842` n `44` status `ready` deltaP `19.7894` edge `0.0322` maxDD `-0.2358`
- `market_context_high->index_24h` score `1.169` n `37` status `ready` deltaP `14.6913` edge `0.115` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.8834` n `37` status `ready` deltaP `10.9422` edge `0.0095` maxDD `-0.0397`
- `market_context_high->index_4h` score `0.5694` n `44` status `ready` deltaP `16.3525` edge `0.0235` maxDD `-2.4279`
- `market_context_high->commodity_1h` score `0.3875` n `56` status `ready` deltaP `12.6283` edge `0.0201` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `0.299` n `44` status `ready` deltaP `4.6841` edge `0.0391` maxDD `-1.633`
- `market_context_high->equity_1h` score `0.0243` n `56` status `ready` deltaP `1.497` edge `0.1083` maxDD `-5.2128`
- `market_context_high->commodity_24h` score `-0.1303` n `37` status `ready` deltaP `2.2195` edge `0.088` maxDD `-6.5601`
- `market_context_high->metal_1h` score `-0.209` n `56` status `ready` deltaP `0.4491` edge `0.003` maxDD `-0.6226`
- `market_context_high->fx_1h` score `-0.5045` n `56` status `ready` deltaP `-5.2395` edge `0.006` maxDD `-0.1928`
- `market_context_high->index_1h` score `-0.5055` n `56` status `ready` deltaP `-3.7104` edge `0.0181` maxDD `-0.6537`
- `market_context_high->metal_24h` score `-1.5439` n `37` status `ready` deltaP `8.0472` edge `-0.127` maxDD `-1.4245`
- `market_context_high->metal_4h` score `-1.7474` n `44` status `ready` deltaP `-7.8575` edge `-0.0407` maxDD `-1.2025`
- `market_context_high->crypto_alt_1h` score `-2.0863` n `56` status `ready` deltaP `0.4812` edge `-0.0814` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-2.7382` n `56` status `ready` deltaP `-1.914` edge `-0.1284` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-2.7895` n `44` status `ready` deltaP `15.3132` edge `-0.0024` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-4.6166` n `44` status `ready` deltaP `10.061` edge `-0.195` maxDD `-17.5435`
- `market_context_high->crypto_major_4h` score `-8.1824` n `44` status `ready` deltaP `-1.9263` edge `-0.3486` maxDD `-23.6342`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
