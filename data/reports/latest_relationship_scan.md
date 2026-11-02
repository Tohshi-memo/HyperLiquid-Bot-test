# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T01:22:40.431733+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7501`

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

- `market_context_high->unknown_24h` score `7688.7379` n `55` status `ready` deltaP `1.3889` edge `640.7189` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.1608` n `55` status `ready` deltaP `7.3281` edge `27.5522` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `22.5333` n `58` status `ready` deltaP `5.0744` edge `1.855` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.394` n `55` status `ready` deltaP `42.7999` edge `1.5211` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.5247` n `94` status `ready` deltaP `32.3508` edge `1.047` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1578` n `55` status `ready` deltaP `49.1319` edge `0.1856` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `5.9905` n `55` status `ready` deltaP `23.75` edge `0.3703` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8849` n `55` status `ready` deltaP `40.7545` edge `0.2498` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.3813` n `55` status `ready` deltaP `30.1303` edge `0.2812` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.1046` n `55` status `ready` deltaP `5.133` edge `0.2947` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.9916` n `55` status `ready` deltaP `28.7805` edge `0.0825` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4712` n `55` status `ready` deltaP `10.8586` edge `0.3121` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.3125` n `126` status `ready` deltaP `9.623` edge `0.2672` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `2.1014` n `55` status `ready` deltaP `-2.9103` edge `0.4406` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7531` n `55` status `ready` deltaP `20.6374` edge `0.051` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.687` n `58` status `ready` deltaP `5.0227` edge `0.1596` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `0.9696` n `58` status `ready` deltaP `5.0227` edge `0.1083` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `0.845` n `58` status `ready` deltaP `0.7485` edge `0.1325` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.841` n `58` status `ready` deltaP `10.6391` edge `0.024` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.671` n `58` status `ready` deltaP `15.0681` edge `0.004` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
