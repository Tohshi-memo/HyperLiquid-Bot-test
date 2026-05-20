# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T04:22:16.488035+00:00`
- Price records: `672`
- Market context records: `1286`
- Flow alert records: `5613`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.6089` n `128` status `ready` deltaP `41.5798` edge `1.3034` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5997` n `128` status `ready` deltaP `8.3333` edge `1.0778` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `9.0926` n `128` status `ready` deltaP `26.302` edge `0.784` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.5813` n `128` status `ready` deltaP `29.1667` edge `0.3793` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9117` n `128` status `ready` deltaP `25.3472` edge `0.5652` maxDD `-14.2815`
- `market_context_high->equity_4h` score `2.4229` n `144` status `ready` deltaP `12.1951` edge `0.1911` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3718` n `128` status `ready` deltaP `1.5625` edge `0.4602` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `2.2726` n `144` status `ready` deltaP `2.9979` edge `0.3667` maxDD `-9.784`
- `market_context_high->commodity_24h` score `1.4105` n `128` status `ready` deltaP `-13.8889` edge `0.3583` maxDD `-6.8535`
- `market_context_high->fx_24h` score `0.3549` n `128` status `ready` deltaP `5.9896` edge `0.0361` maxDD `-0.3831`
- `market_context_high->index_4h` score `0.2932` n `144` status `ready` deltaP `7.3001` edge `0.0914` maxDD `-3.1979`
- `market_context_high->equity_1h` score `0.2864` n `153` status `ready` deltaP `4.2416` edge `0.0383` maxDD `-1.7505`
- `market_context_high->metal_4h` score `0.1957` n `144` status `ready` deltaP `13.7704` edge `0.0676` maxDD `-6.4478`
- `market_context_high->index_1h` score `0.1313` n `153` status `ready` deltaP `6.6368` edge `0.018` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0404` n `153` status `ready` deltaP `9.8607` edge `0.0066` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3491` n `153` status `ready` deltaP `0.9002` edge `0.0363` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.518` n `153` status `ready` deltaP `0.9002` edge `-0.0036` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7731` n `153` status `ready` deltaP `-0.2319` edge `0.0045` maxDD `-5.8323`
- `market_context_high->crypto_alt_4h` score `-0.8872` n `144` status `ready` deltaP `8.9261` edge `0.1587` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.9458` n `144` status `ready` deltaP `4.2344` edge `0.1214` maxDD `-13.3376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
