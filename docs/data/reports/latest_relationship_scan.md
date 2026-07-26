# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T16:22:23.338392+00:00`
- Price records: `672`
- Market context records: `8002`
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

- `market_context_high->equity_24h` score `15.8903` n `91` status `ready` deltaP `26.1714` edge `1.2839` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.741` n `91` status `ready` deltaP `35.9375` edge `0.4055` maxDD `0.0`
- `market_context_high->equity_4h` score `6.156` n `104` status `ready` deltaP `24.613` edge `0.4382` maxDD `-5.1426`
- `market_context_high->metal_4h` score `2.5917` n `104` status `ready` deltaP `24.1675` edge `0.1171` maxDD `-0.979`
- `market_context_high->index_4h` score `2.4072` n `104` status `ready` deltaP `25.258` edge `0.0682` maxDD `-0.8791`
- `market_context_high->index_24h` score `2.1136` n `91` status `ready` deltaP `13.0438` edge `0.1562` maxDD `-1.3621`
- `market_context_high->commodity_24h` score `2.0605` n `91` status `ready` deltaP `20.5605` edge `0.1879` maxDD `-6.5945`
- `market_context_high->equity_1h` score `1.6092` n `104` status `ready` deltaP `13.6285` edge `0.125` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2522` n `91` status `ready` deltaP `26.4766` edge `0.0366` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.8762` n `104` status `ready` deltaP `14.3137` edge `0.0206` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7057` n `104` status `ready` deltaP `10.1912` edge `0.0287` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.674` n `104` status `ready` deltaP `9.9554` edge `0.1616` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.6019` n `104` status `ready` deltaP `6.461` edge `0.1188` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5311` n `104` status `ready` deltaP `10.6403` edge `0.0382` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0644` n `104` status `ready` deltaP `0.5988` edge `0.031` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2566` n `104` status `ready` deltaP `0.4088` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.3778` n `104` status `ready` deltaP `5.863` edge `0.0042` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.5475` n `104` status `ready` deltaP `-0.5355` edge `-0.0043` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.2102` n `104` status `ready` deltaP `-0.0117` edge `-0.0049` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.9586` n `104` status `ready` deltaP `6.7538` edge `-0.1659` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
