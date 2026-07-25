# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T10:22:27.638958+00:00`
- Price records: `672`
- Market context records: `7868`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14667`

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

- `market_context_high->equity_24h` score `12.2804` n `121` status `ready` deltaP `29.1225` edge `0.9634` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.3416` n `122` status `ready` deltaP `13.852` edge `0.2604` maxDD `-1.9426`
- `market_context_high->equity_4h` score `2.1872` n `122` status `ready` deltaP `8.8208` edge `0.3526` maxDD `-5.8127`
- `market_context_high->crypto_major_4h` score `1.5392` n `122` status `ready` deltaP `16.8708` edge `0.1876` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.3625` n `121` status `ready` deltaP `21.2088` edge `0.1305` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.2999` n `122` status `ready` deltaP `14.4547` edge `0.0519` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.29` n `122` status `ready` deltaP `11.8378` edge `0.1403` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.0096` n `121` status `ready` deltaP `28.4556` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7085` n `122` status `ready` deltaP `10.4243` edge `0.1031` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.4182` n `122` status `ready` deltaP `5.4457` edge `0.0418` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.3401` n `122` status `ready` deltaP `7.2743` edge `0.0392` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.2146` n `122` status `ready` deltaP `8.0589` edge `0.0168` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.0209` n `122` status `ready` deltaP `5.0313` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1831` n `122` status `ready` deltaP `10.4051` edge `0.0524` maxDD `-1.2861`
- `market_context_high->fx_1h` score `-0.2802` n `122` status `ready` deltaP `0.4628` edge `-0.0003` maxDD `-0.4304`
- `market_context_high->metal_4h` score `-0.732` n `122` status `ready` deltaP `4.3832` edge `0.0853` maxDD `-1.3749`
- `market_context_high->metal_1h` score `-0.9197` n `122` status `ready` deltaP `0.3141` edge `0.0216` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.3` n `121` status `ready` deltaP `-3.5487` edge `0.1027` maxDD `-1.9901`
- `market_context_high->fx_4h` score `-1.3378` n `122` status `ready` deltaP `-2.7046` edge `0.0004` maxDD `-1.644`
- `market_context_high->crypto_alt_24h` score `-1.5201` n `122` status `ready` deltaP `14.6163` edge `0.2372` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
