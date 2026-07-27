# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T08:07:27.279990+00:00`
- Price records: `672`
- Market context records: `8072`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0948` n `81` status `ready` deltaP `36.224` edge `1.5241` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.359` n `87` status `ready` deltaP `32.4205` edge `0.5284` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2808` n `81` status `ready` deltaP `35.8752` edge `0.4509` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.6534` n `41` status `ready` deltaP `30.1264` edge `0.1352` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2833` n `87` status `ready` deltaP `31.5881` edge `0.0818` maxDD `-0.5022`
- `market_context_high->commodity_24h` score `3.0493` n `81` status `ready` deltaP `29.467` edge `0.2599` maxDD `-10.846`
- `news_risk_high->unknown_1h` score `2.9748` n `41` status `ready` deltaP `3.6147` edge `0.2515` maxDD `-0.8826`
- `market_context_high->index_24h` score `2.851` n `81` status `ready` deltaP `17.4466` edge `0.1883` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4128` n `87` status `ready` deltaP `22.2158` edge `0.1152` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.361` n `87` status `ready` deltaP `14.8754` edge `0.1409` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2239` n `81` status `ready` deltaP `30.2074` edge `0.0543` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1278` n `87` status `ready` deltaP `14.9718` edge `0.0209` maxDD `-0.4716`
- `news_risk_high->crypto_major_1h` score `0.7697` n `41` status `ready` deltaP `2.91` edge `0.0775` maxDD `-0.9543`
- `market_context_high->metal_1h` score `0.7679` n `87` status `ready` deltaP `10.9247` edge `0.029` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4944` n `87` status `ready` deltaP `9.0216` edge `0.0221` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.4014` n `87` status `ready` deltaP `3.8951` edge `0.1192` maxDD `-3.9374`
- `news_risk_high->index_1h` score `0.3966` n `41` status `ready` deltaP `5.6923` edge `0.0198` maxDD `-0.3089`
- `news_risk_high->crypto_alt_1h` score `0.3665` n `41` status `ready` deltaP `4.407` edge `0.0526` maxDD `-0.7991`
- `market_context_high->crypto_major_4h` score `0.2362` n `87` status `ready` deltaP `6.7336` edge `0.1466` maxDD `-6.7444`
- `news_risk_high->fx_1h` score `0.1331` n `41` status `ready` deltaP `5.7543` edge `0.0053` maxDD `-0.1283`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
