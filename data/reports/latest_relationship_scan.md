# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T15:37:26.504923+00:00`
- Price records: `672`
- Market context records: `7999`
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

- `market_context_high->equity_24h` score `15.983` n `90` status `ready` deltaP `26.25` edge `1.2911` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.783` n `90` status `ready` deltaP `35.9375` edge `0.409` maxDD `0.0`
- `market_context_high->equity_4h` score `6.1876` n `104` status `ready` deltaP `24.9179` edge `0.4388` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5795` n `104` status `ready` deltaP `24.015` edge `0.1171` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4486` n `104` status `ready` deltaP `25.7153` edge `0.0686` maxDD `-0.8791`
- `market_context_high->commodity_24h` score `2.2296` n `90` status `ready` deltaP `21.3541` edge `0.1967` maxDD `-6.5945`
- `market_context_high->index_24h` score `2.0772` n `90` status `ready` deltaP `12.6042` edge `0.1561` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6368` n `104` status `ready` deltaP `13.9279` edge `0.1253` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2503` n `90` status `ready` deltaP `26.4236` edge `0.0368` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9001` n `104` status `ready` deltaP `14.6131` edge `0.0206` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.7562` n `104` status `ready` deltaP `10.4127` edge `0.1654` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7176` n `104` status `ready` deltaP `10.3409` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_alt_4h` score `0.6757` n `104` status `ready` deltaP `6.9184` edge `0.1219` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5451` n `104` status `ready` deltaP `10.79` edge `0.039` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0481` n `104` status `ready` deltaP `0.7485` edge `0.0321` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.273` n `104` status `ready` deltaP `0.1094` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4143` n `104` status `ready` deltaP `5.4057` edge `0.0042` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5475` n `104` status `ready` deltaP `-0.5355` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1841` n `104` status `ready` deltaP `0.4456` edge `-0.0046` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9598` n `104` status `ready` deltaP `6.7538` edge `-0.166` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
