# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T15:52:30.833537+00:00`
- Price records: `672`
- Market context records: `8000`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11806`

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

- `market_context_high->equity_24h` score `15.9378` n `91` status `ready` deltaP `26.345` edge `1.2867` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.741` n `91` status `ready` deltaP `35.9375` edge `0.4055` maxDD `0.0`
- `market_context_high->equity_4h` score `6.173` n `104` status `ready` deltaP `24.7655` edge `0.4386` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5917` n `104` status `ready` deltaP `24.1675` edge `0.1171` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4352` n `104` status `ready` deltaP `25.5629` edge `0.0685` maxDD `-0.8791`
- `market_context_high->index_24h` score `2.116` n `91` status `ready` deltaP `13.0438` edge `0.1564` maxDD `-1.3621`
- `market_context_high->commodity_24h` score `2.0653` n `91` status `ready` deltaP `20.5605` edge `0.1883` maxDD `-6.5945`
- `market_context_high->equity_1h` score `1.6224` n `104` status `ready` deltaP `13.7782` edge `0.1251` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2848` n `91` status `ready` deltaP `26.8238` edge `0.037` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9001` n `104` status `ready` deltaP `14.6131` edge `0.0206` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.7308` n `104` status `ready` deltaP `10.2603` edge `0.1643` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7176` n `104` status `ready` deltaP `10.3409` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6527` n `104` status `ready` deltaP `6.7659` edge `0.121` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5436` n `104` status `ready` deltaP `10.79` edge `0.0388` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0504` n `104` status `ready` deltaP `0.7485` edge `0.0318` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2652` n `104` status `ready` deltaP `0.2591` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4021` n `104` status `ready` deltaP `5.5582` edge `0.0042` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5475` n `104` status `ready` deltaP `-0.5355` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1928` n `104` status `ready` deltaP `0.2931` edge `-0.0047` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9598` n `104` status `ready` deltaP `6.7538` edge `-0.166` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
