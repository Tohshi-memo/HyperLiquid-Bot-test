# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T14:37:30.283130+00:00`
- Price records: `672`
- Market context records: `7994`
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

- `market_context_high->equity_24h` score `16.0057` n `88` status `ready` deltaP `25.6944` edge `1.2967` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8658` n `88` status `ready` deltaP `35.9375` edge `0.4159` maxDD `0.0`
- `market_context_high->equity_4h` score `6.235` n `104` status `ready` deltaP `25.3752` edge `0.4397` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5795` n `104` status `ready` deltaP `24.015` edge `0.1171` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.5685` n `88` status `ready` deltaP `22.9955` edge `0.214` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.5033` n `104` status `ready` deltaP `26.3251` edge `0.0691` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.6919` n `104` status `ready` deltaP `14.5267` edge `0.1259` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.292` n `88` status `ready` deltaP `11.6951` edge `0.1547` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2086` n `88` status `ready` deltaP `25.9312` edge `0.0366` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9001` n `104` status `ready` deltaP `14.6131` edge `0.0206` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.8033` n `104` status `ready` deltaP `10.7176` edge `0.1673` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.718` n `104` status `ready` deltaP `7.2232` edge `0.1234` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7045` n `104` status `ready` deltaP `10.1912` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5498` n `104` status `ready` deltaP `10.79` edge `0.0396` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.052` n `104` status `ready` deltaP `0.5988` edge `0.0326` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2808` n `104` status `ready` deltaP `-0.0403` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4399` n `104` status `ready` deltaP `5.1008` edge `0.0041` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5662` n `104` status `ready` deltaP `-0.8349` edge `-0.0047` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1746` n `104` status `ready` deltaP `0.598` edge `-0.0044` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9706` n `104` status `ready` deltaP `6.6041` edge `-0.1659` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
