# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T15:22:37.561365+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6615`

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

- `market_context_high->unknown_24h` score `7054.9291` n `55` status `ready` deltaP `1.3889` edge `587.9015` maxDD `0.0`
- `market_context_high->unknown_4h` score `379.7849` n `55` status `ready` deltaP `5.4989` edge `31.6164` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `74.6955` n `55` status `ready` deltaP `3.4622` edge `6.2126` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.034` n `55` status `ready` deltaP `42.7999` edge `1.4911` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.051` n `95` status `ready` deltaP `30.2394` edge `1.0216` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.7222` n `55` status `ready` deltaP `54.6875` edge `0.1956` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.3165` n `55` status `ready` deltaP `44.5739` edge `0.2603` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.0721` n `55` status `ready` deltaP `23.75` edge `0.3771` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6671` n `55` status `ready` deltaP `31.1974` edge `0.2979` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.473` n `55` status `ready` deltaP `6.0477` edge `0.3193` maxDD `-2.283`
- `news_risk_high->crypto_alt_4h` score `3.4544` n `116` status `ready` deltaP `15.3017` edge `0.3245` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3126` n `55` status `ready` deltaP `31.0671` edge `0.094` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.3928` n `55` status `ready` deltaP `10.685` edge `0.3032` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7547` n `55` status `ready` deltaP `-5.1673` edge `0.4112` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.6214` n `55` status `ready` deltaP `18.9606` edge `0.0512` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.5273` n `55` status `ready` deltaP `3.0267` edge `0.1596` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.3952` n `55` status `ready` deltaP `8.0321` edge `0.1237` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.3751` n `55` status `ready` deltaP `3.9249` edge `0.1555` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.9367` n `55` status `ready` deltaP `11.6249` edge `0.0254` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.563` n `55` status `ready` deltaP `13.6364` edge `-0.0003` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
