# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T23:37:29.801034+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6535`

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

- `market_context_high->unknown_4h` score `22.2003` n `47` status `ready` deltaP `-1.4725` edge `1.9046` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.5924` n `37` status `ready` deltaP `11.2472` edge `0.7372` maxDD `-31.3588`
- `market_context_high->index_24h` score `1.1796` n `37` status `ready` deltaP `14.8649` edge `0.1152` maxDD `-2.7123`
- `market_context_high->fx_4h` score `1.0106` n `47` status `ready` deltaP `15.1693` edge `0.0287` maxDD `-0.3153`
- `market_context_high->fx_24h` score `0.899` n `37` status `ready` deltaP `10.9422` edge `0.0108` maxDD `-0.0397`
- `market_context_high->equity_1h` score `0.2876` n `59` status `ready` deltaP `3.8897` edge `0.1261` maxDD `-5.2128`
- `market_context_high->index_4h` score `0.2343` n `47` status `ready` deltaP `12.4578` edge `0.019` maxDD `-2.4279`
- `market_context_high->commodity_4h` score `0.2213` n `47` status `ready` deltaP `5.0078` edge `0.0404` maxDD `-1.633`
- `market_context_high->commodity_1h` score `0.1489` n `59` status `ready` deltaP `9.2688` edge `0.0119` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0233` n `59` status `ready` deltaP `2.9915` edge `0.0109` maxDD `-0.6226`
- `market_context_high->commodity_24h` score `-0.1818` n `37` status `ready` deltaP `2.2195` edge `0.0814` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.3544` n `59` status `ready` deltaP `-1.1951` edge `0.0207` maxDD `-0.6537`
- `market_context_high->fx_1h` score `-0.4526` n `59` status `ready` deltaP `-4.2423` edge `0.006` maxDD `-0.1928`
- `market_context_high->metal_4h` score `-1.3692` n `47` status `ready` deltaP `-3.9407` edge `-0.0353` maxDD `-1.2025`
- `market_context_high->crypto_alt_1h` score `-1.4563` n `59` status `ready` deltaP `3.1462` edge `-0.0184` maxDD `-10.1421`
- `market_context_high->metal_24h` score `-1.5331` n `37` status `ready` deltaP `8.0472` edge `-0.1261` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-2.1004` n `59` status `ready` deltaP `0.751` edge `-0.0644` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.6347` n `47` status `ready` deltaP `11.7086` edge `-0.0363` maxDD `-24.9053`
- `market_context_high->crypto_alt_4h` score `-6.1956` n `47` status `ready` deltaP `7.3268` edge `-0.2512` maxDD `-21.1156`
- `market_context_high->crypto_major_24h` score `-8.3293` n `37` status `ready` deltaP `-9.0841` edge `-0.1575` maxDD `-32.0839`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
