# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T10:07:18.122855+00:00`
- Price records: `672`
- Market context records: `1209`
- Flow alert records: `5387`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8776`

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

- `market_context_high->crypto_major_24h` score `18.6969` n `130` status `ready` deltaP `44.0946` edge `1.3773` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.1414` n `130` status `ready` deltaP `21.9979` edge `0.6501` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `6.9336` n `130` status `ready` deltaP `2.9175` edge `0.68` maxDD `-6.7322`
- `market_context_high->commodity_24h` score `5.3901` n `130` status `ready` deltaP `-2.9434` edge `0.6391` maxDD `-8.6239`
- `market_context_high->metal_24h` score `4.3822` n `130` status `ready` deltaP `-3.4348` edge `0.5548` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.8445` n `130` status `ready` deltaP `14.681` edge `0.2055` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.148` n `130` status `ready` deltaP `18.0502` edge `0.1673` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.8187` n `130` status `ready` deltaP `18.2479` edge `0.3442` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9607` n `130` status `ready` deltaP `10.5089` edge `0.0783` maxDD `-2.1308`
- `market_context_high->fx_24h` score `0.8649` n `130` status `ready` deltaP `9.7383` edge `0.061` maxDD `-0.9743`
- `market_context_high->index_1h` score `0.5792` n `130` status `ready` deltaP `9.1134` edge `0.0192` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4748` n `130` status `ready` deltaP `4.5601` edge `0.0466` maxDD `-1.3281`
- `market_context_high->metal_1h` score `-0.1223` n `130` status `ready` deltaP `9.0972` edge `-0.0098` maxDD `-2.2164`
- `market_context_high->fx_1h` score `-0.1526` n `130` status `ready` deltaP `4.8687` edge `0.0004` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.1977` n `130` status `ready` deltaP `5.5159` edge `0.13` maxDD `-8.3693`
- `market_context_high->crypto_alt_1h` score `-0.3753` n `130` status `ready` deltaP `0.4445` edge `0.0332` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.3808` n `130` status `ready` deltaP `3.0977` edge `0.0071` maxDD `-4.1256`
- `market_context_high->unknown_24h` score `-0.567` n `130` status `ready` deltaP `0.1523` edge `0.2247` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.766` n `130` status `ready` deltaP `-2.287` edge `0.0129` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.7971` n `130` status `ready` deltaP `10.3963` edge `-0.0284` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
