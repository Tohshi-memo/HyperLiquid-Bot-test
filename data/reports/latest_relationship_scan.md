# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T12:52:27.729655+00:00`
- Price records: `672`
- Market context records: `7986`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11790`

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

- `market_context_high->equity_24h` score `16.0599` n `85` status `ready` deltaP `24.812` edge `1.3071` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.9798` n `85` status `ready` deltaP `35.9375` edge `0.4254` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3931` n `101` status `ready` deltaP `25.7758` edge `0.4502` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.239` n `85` status `ready` deltaP `25.6025` edge `0.2525` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6537` n `101` status `ready` deltaP `27.8299` edge `0.0716` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6005` n `101` status `ready` deltaP `23.8725` edge `0.1198` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.6919` n `104` status `ready` deltaP `14.5267` edge `0.1259` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.2052` n `85` status `ready` deltaP `10.2513` edge `0.1532` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1454` n `85` status `ready` deltaP `25.2615` edge `0.0358` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9372` n `104` status `ready` deltaP `15.0622` edge `0.0207` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9273` n `101` status `ready` deltaP `11.3076` edge `0.1737` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.9142` n `101` status `ready` deltaP `8.5652` edge `0.1308` maxDD `-3.9374`
- `market_context_high->metal_1h` score `0.7284` n `104` status `ready` deltaP `10.4906` edge `0.0286` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5584` n `104` status `ready` deltaP `10.9397` edge `0.0397` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0691` n `104` status `ready` deltaP `0.4491` edge `0.0314` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3041` n `104` status `ready` deltaP `-0.4894` edge `0.001` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.4934` n `101` status `ready` deltaP `4.463` edge `0.0039` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5405` n `104` status `ready` deltaP `-0.3858` edge `-0.0044` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.1447` n `101` status `ready` deltaP `0.0362` edge `-0.004` maxDD `-5.1068`
- `market_context_high->unknown_1h` score `-1.9526` n `104` status `ready` deltaP `6.7538` edge `-0.1654` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
