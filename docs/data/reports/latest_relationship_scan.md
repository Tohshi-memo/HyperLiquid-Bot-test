# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T09:37:29.117197+00:00`
- Price records: `672`
- Market context records: `8502`
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

- `news_risk_high->unknown_24h` score `6274.2434` n `52` status `ready` deltaP `44.5646` edge `522.5986` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0716` n `64` status `ready` deltaP `22.1799` edge `0.4178` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0655` n `64` status `ready` deltaP `17.1113` edge `0.0771` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7302` n `64` status `ready` deltaP `15.9525` edge `0.0855` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9501` n `64` status `ready` deltaP `5.8308` edge `0.1605` maxDD `-3.5385`
- `market_context_high->equity_1h` score `0.9431` n `31` status `ready` deltaP `7.0311` edge `0.0567` maxDD `-0.9985`
- `news_risk_high->crypto_alt_4h` score `0.9147` n `64` status `ready` deltaP `14.4817` edge `0.1599` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6152` n `64` status `ready` deltaP `9.9083` edge `0.0655` maxDD `-1.8813`
- `market_context_high->index_1h` score `0.3989` n `31` status `ready` deltaP `10.7736` edge `-0.001` maxDD `-0.2417`
- `news_risk_high->crypto_major_1h` score `0.3898` n `64` status `ready` deltaP `7.3634` edge `0.0521` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1531` n `64` status `ready` deltaP `6.4839` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0778` n `64` status `ready` deltaP `12.0808` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0309` n `64` status `ready` deltaP `4.07` edge `0.0085` maxDD `-0.5338`
- `market_context_high->crypto_major_1h` score `-0.0584` n `31` status `ready` deltaP `4.3896` edge `-0.0043` maxDD `-1.2625`
- `news_risk_high->metal_4h` score `-0.0697` n `64` status `ready` deltaP `1.1052` edge `0.0313` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1311` n `64` status `ready` deltaP `3.256` edge `0.0077` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.1843` n `31` status `ready` deltaP `1.8447` edge `-0.0087` maxDD `-0.5119`
- `market_context_high->crypto_alt_1h` score `-0.7042` n `31` status `ready` deltaP `-9.1945` edge `0.0142` maxDD `-1.4551`
- `market_context_high->commodity_1h` score `-1.3984` n `31` status `ready` deltaP `-2.8926` edge `-0.0347` maxDD `-2.0038`
- `news_risk_high->commodity_1h` score `-1.7071` n `64` status `ready` deltaP `-4.3039` edge `-0.035` maxDD `-2.9516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
