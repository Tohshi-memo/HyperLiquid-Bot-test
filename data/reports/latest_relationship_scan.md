# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T14:52:29.694736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `1.9916` n `76` status `ready` deltaP `18.3479` edge `0.1288` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5379` n `43` status `ready` deltaP `14.0475` edge `0.009` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5379` n `43` status `ready` deltaP `14.0475` edge `0.009` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4447` n `43` status `ready` deltaP `10.1553` edge `-0.0003` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.1409` n `43` status `ready` deltaP `13.7274` edge `0.0` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1409` n `43` status `ready` deltaP `13.7274` edge `0.0` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.1204` n `77` status `ready` deltaP `3.3873` edge `0.3333` maxDD `-15.2359`
- `risk_on_high->fx_4h` score `-0.1007` n `43` status `ready` deltaP `1.7726` edge `0.0062` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1007` n `43` status `ready` deltaP `1.7726` edge `0.0062` maxDD `-0.1126`
- `market_context_high->crypto_major_24h` score `-0.1739` n `76` status `ready` deltaP `-1.3798` edge `0.5966` maxDD `-35.1086`
- `risk_on_high->fx_1h` score `-0.2387` n `43` status `ready` deltaP `0.7137` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2387` n `43` status `ready` deltaP `0.7137` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.269` n `84` status `ready` deltaP `1.6182` edge `0.0564` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.5129` n `84` status `ready` deltaP `-4.2986` edge `0.0004` maxDD `-0.6669`
- `market_context_high->fx_4h` score `-0.5361` n `77` status `ready` deltaP `-1.3383` edge `0.0039` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.5833` n `77` status `ready` deltaP `-0.3505` edge `0.0498` maxDD `-0.7797`
- `risk_on_high->index_4h` score `-0.5902` n `43` status `ready` deltaP `5.0872` edge `0.0036` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5902` n `43` status `ready` deltaP `5.0872` edge `0.0036` maxDD `-0.9359`
- `market_context_high->fx_1h` score `-0.6959` n `84` status `ready` deltaP `-5.211` edge `-0.0018` maxDD `-0.5477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
