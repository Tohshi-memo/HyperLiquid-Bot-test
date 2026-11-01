# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T14:37:28.893751+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6613`

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

- `market_context_high->unknown_24h` score `7032.8899` n `55` status `ready` deltaP `1.3889` edge `586.0649` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.5855` n `55` status `ready` deltaP `5.3464` edge `31.6008` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.8503` n `55` status `ready` deltaP `3.7616` edge `6.2235` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.0467` n `55` status `ready` deltaP `42.9735` edge `1.491` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.0994` n `98` status `ready` deltaP `30.4847` edge `1.024` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7572` n `55` status `ready` deltaP `55.0347` edge `0.1962` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3869` n `55` status `ready` deltaP `45.0947` edge `0.2627` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.0301` n `55` status `ready` deltaP `23.75` edge `0.3736` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6223` n `55` status `ready` deltaP `30.8925` edge `0.2962` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `3.65` n `116` status `ready` deltaP `15.3017` edge `0.3408` maxDD `-7.4246`
- `market_context_high->equity_4h` score `3.4404` n `55` status `ready` deltaP `5.8952` edge `0.3176` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3539` n `55` status `ready` deltaP `31.5244` edge `0.0944` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4014` n `55` status `ready` deltaP `10.685` edge `0.3043` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7262` n `55` status `ready` deltaP `-5.3409` edge `0.4087` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5824` n `55` status `ready` deltaP `18.5033` edge `0.051` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5081` n `55` status `ready` deltaP `2.877` edge `0.159` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.358` n `55` status `ready` deltaP `7.7327` edge `0.1226` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.314` n `55` status `ready` deltaP `3.6255` edge `0.1524` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9367` n `55` status `ready` deltaP `11.6249` edge `0.0254` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5872` n `55` status `ready` deltaP `14.0855` edge `-0.0002` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
