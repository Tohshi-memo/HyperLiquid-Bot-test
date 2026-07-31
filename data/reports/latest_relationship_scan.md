# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T09:22:24.535550+00:00`
- Price records: `672`
- Market context records: `8501`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->unknown_24h` score `6273.9535` n `52` status `ready` deltaP `44.391` edge `522.5756` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0534` n `64` status `ready` deltaP `22.0274` edge `0.4173` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0509` n `64` status `ready` deltaP `16.9588` edge `0.0769` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7098` n `64` status `ready` deltaP `15.8028` edge `0.0848` maxDD `-2.4803`
- `market_context_high->equity_1h` score `1.1632` n `30` status `ready` deltaP `9.032` edge `0.0617` maxDD `-0.9985`
- `news_risk_high->crypto_major_4h` score `0.9509` n `64` status `ready` deltaP `5.8308` edge `0.1606` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.9201` n `64` status `ready` deltaP `14.4817` edge `0.1606` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6113` n `64` status `ready` deltaP `9.9083` edge `0.065` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3875` n `64` status `ready` deltaP `7.3634` edge `0.0518` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.335` n `30` status `ready` deltaP `9.5908` edge `-0.0013` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1609` n `64` status `ready` deltaP `6.6336` edge `0.0045` maxDD `-0.2475`
- `market_context_high->crypto_major_1h` score `0.1534` n `30` status `ready` deltaP `6.2176` edge `0.0064` maxDD `-0.9216`
- `news_risk_high->fx_4h` score `0.0778` n `64` status `ready` deltaP `12.0808` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0301` n `64` status `ready` deltaP `4.07` edge `0.0084` maxDD `-0.5338`
- `market_context_high->metal_1h` score `-0.0243` n `30` status `ready` deltaP `3.523` edge `-0.0051` maxDD `-0.3866`
- `news_risk_high->metal_4h` score `-0.0808` n `64` status `ready` deltaP `0.9527` edge `0.0309` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1467` n `64` status `ready` deltaP `3.1063` edge `0.0074` maxDD `-0.5599`
- `market_context_high->crypto_alt_1h` score `-0.5057` n `30` status `ready` deltaP `-7.9042` edge `0.0262` maxDD `-1.0671`
- `market_context_high->commodity_1h` score `-1.6322` n `30` status `ready` deltaP `-4.5709` edge `-0.043` maxDD `-2.0038`
- `news_risk_high->commodity_1h` score `-1.6903` n `64` status `ready` deltaP `-4.1542` edge `-0.0346` maxDD `-2.9516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
