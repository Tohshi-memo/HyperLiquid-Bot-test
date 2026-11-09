# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T00:22:29.344516+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6537`

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

- `market_context_high->equity_24h` score `4.4856` n `37` status `ready` deltaP `11.2472` edge `0.7283` maxDD `-31.3588`
- `market_context_high->index_24h` score `1.2047` n `37` status `ready` deltaP `15.2121` edge `0.1161` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.9424` n `37` status `ready` deltaP `11.2894` edge `0.0121` maxDD `-0.0397`
- `market_context_high->unknown_4h` score `0.562` n `50` status `ready` deltaP `-0.4512` edge `0.0946` maxDD `-0.9139`
- `market_context_high->fx_4h` score `0.2914` n `50` status `ready` deltaP `11.1585` edge `0.0236` maxDD `-0.517`
- `market_context_high->commodity_4h` score `0.1969` n `50` status `ready` deltaP `3.4085` edge `0.0391` maxDD `-1.633`
- `market_context_high->metal_1h` score `0.1832` n `62` status `ready` deltaP `5.2878` edge `0.0128` maxDD `-0.6226`
- `market_context_high->equity_1h` score `0.002` n `62` status `ready` deltaP `1.7964` edge `0.1038` maxDD `-5.2418`
- `market_context_high->commodity_1h` score `-0.016` n `62` status `ready` deltaP `6.5337` edge `0.009` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.094` n `50` status `ready` deltaP `9.0854` edge `0.0119` maxDD `-2.4279`
- `market_context_high->commodity_24h` score `-0.234` n `37` status `ready` deltaP `2.2195` edge `0.0747` maxDD `-6.5601`
- `market_context_high->index_1h` score `-0.4762` n `62` status `ready` deltaP `-3.0423` edge `0.0174` maxDD `-0.6537`
- `market_context_high->fx_1h` score `-0.5858` n `62` status `ready` deltaP `-6.2536` edge `0.0037` maxDD `-0.3023`
- `market_context_high->metal_4h` score `-0.7899` n `50` status `ready` deltaP `-2.6463` edge `-0.0311` maxDD `-1.2025`
- `market_context_high->metal_24h` score `-1.5096` n `37` status `ready` deltaP `8.2208` edge `-0.1253` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.5948` n `62` status `ready` deltaP `2.6125` edge `-0.0326` maxDD `-10.1421`
- `market_context_high->crypto_major_1h` score `-2.3953` n `62` status `ready` deltaP `-1.2459` edge `-0.0889` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-4.6317` n `50` status `ready` deltaP `8.5915` edge `-0.0861` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-8.2237` n `37` status `ready` deltaP `-9.0841` edge `-0.1487` maxDD `-32.0839`
- `market_context_high->crypto_alt_4h` score `-8.2938` n `50` status `ready` deltaP `4.9756` edge `-0.3278` maxDD `-26.7215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
