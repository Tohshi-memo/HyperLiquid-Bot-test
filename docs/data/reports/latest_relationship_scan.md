# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T18:37:27.635158+00:00`
- Price records: `672`
- Market context records: `4854`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7632`

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

- `market_context_high->unknown_1h` score `13.5053` n `110` status `ready` deltaP `10.6206` edge `1.0964` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.0305` n `104` status `ready` deltaP `28.0253` edge `0.7855` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `5.9093` n `104` status `ready` deltaP `18.8203` edge `0.5022` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.743` n `104` status `ready` deltaP `15.6895` edge `0.4964` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2134` n `91` status `ready` deltaP `25.8166` edge `0.2966` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.5474` n `104` status `ready` deltaP `11.5619` edge `0.1181` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8287` n `104` status `ready` deltaP `11.3391` edge `0.1688` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5335` n `104` status `ready` deltaP `10.9874` edge `0.0414` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4235` n `110` status `ready` deltaP `6.0207` edge `0.118` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3926` n `110` status `ready` deltaP `7.8715` edge `0.1001` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.209` n `110` status `ready` deltaP `4.0855` edge `0.0593` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.195` n `110` status `ready` deltaP `3.7316` edge `0.0161` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.1954` n `110` status `ready` deltaP `0.3946` edge `0.0303` maxDD `-1.3057`
- `market_context_high->fx_4h` score `-0.3113` n `104` status `ready` deltaP `3.6468` edge `0.0068` maxDD `-1.0153`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `0.0109` edge `0.0103` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7386` n `104` status `ready` deltaP `7.3288` edge `0.0068` maxDD `-4.377`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-2.0165` n `91` status `ready` deltaP `-8.072` edge `-0.0132` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.9074` n `91` status `ready` deltaP `-9.749` edge `-0.1556` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.5978` n `91` status `ready` deltaP `9.4646` edge `-0.0187` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
