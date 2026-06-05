# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T21:52:22.305808+00:00`
- Price records: `672`
- Market context records: `3009`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `20.4877` n `98` status `ready` deltaP `8.0676` edge `2.0452` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.7386` n `98` status `ready` deltaP `42.9883` edge `0.786` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.378` n `98` status `ready` deltaP `20.3054` edge `0.9426` maxDD `-1.7175`
- `market_context_high->equity_24h` score `10.5632` n `98` status `ready` deltaP `19.0406` edge `0.9537` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.5672` n `98` status `ready` deltaP `18.6508` edge `0.521` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.445` n `105` status `ready` deltaP `18.2651` edge `0.1467` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6083` n `105` status `ready` deltaP `13.1606` edge `0.1707` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.3074` n `105` status `ready` deltaP `17.8107` edge `0.0987` maxDD `-9.9084`
- `market_context_high->commodity_1h` score `-0.1297` n `113` status `ready` deltaP `0.4292` edge `0.0193` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.2061` n `113` status `ready` deltaP `5.1137` edge `0.0473` maxDD `-5.6254`
- `market_context_high->crypto_alt_4h` score `-0.2991` n `105` status `ready` deltaP `22.1182` edge `0.369` maxDD `-38.7172`
- `market_context_high->index_1h` score `-0.3718` n `113` status `ready` deltaP `4.7308` edge `0.0222` maxDD `-4.1126`
- `market_context_high->fx_1h` score `-0.3895` n `113` status `ready` deltaP `-2.0759` edge `0.0005` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.5821` n `113` status `ready` deltaP `7.958` edge `0.1114` maxDD `-14.7034`
- `market_context_high->crypto_major_1h` score `-0.8906` n `113` status `ready` deltaP `5.6422` edge `0.0745` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-1.0657` n `113` status `ready` deltaP `3.357` edge `-0.0381` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.1855` n `105` status `ready` deltaP `-10.8` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.6323` n `105` status `ready` deltaP `-2.4579` edge `-0.0143` maxDD `-3.7602`
- `market_context_high->metal_1h` score `-1.8145` n `113` status `ready` deltaP `-2.1594` edge `-0.005` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.8314` n `98` status `ready` deltaP `-5.9594` edge `-0.0257` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
