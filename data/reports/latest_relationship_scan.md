# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T17:37:34.358869+00:00`
- Price records: `672`
- Market context records: `8535`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5914`

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

- `news_risk_high->unknown_24h` score `6279.8131` n `52` status `ready` deltaP `43.1758` edge `523.072` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.8244` n `64` status `ready` deltaP `21.2652` edge `0.4033` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0495` n `64` status `ready` deltaP `16.8064` edge `0.0778` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.729` n `64` status `ready` deltaP `15.9525` edge `0.0854` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0383` n `64` status `ready` deltaP `6.8979` edge `0.1647` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8221` n `64` status `ready` deltaP `14.7866` edge `0.146` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.489` n `64` status `ready` deltaP `8.561` edge `0.0583` maxDD `-1.8813`
- `market_context_high->crypto_alt_4h` score `0.4736` n `51` status `ready` deltaP `7.1886` edge `0.1085` maxDD `-5.323`
- `news_risk_high->crypto_major_1h` score `0.3477` n `64` status `ready` deltaP `6.7646` edge `0.0507` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0714` n `64` status `ready` deltaP `4.9869` edge `0.004` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.0361` n `64` status `ready` deltaP `2.6296` edge `0.0347` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.027` n `64` status `ready` deltaP `3.9203` edge `0.009` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.007` n `64` status `ready` deltaP `11.1662` edge `0.0219` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.0988` n `64` status `ready` deltaP `3.5554` edge `0.0084` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2934` n `62` status `ready` deltaP `1.9123` edge `-0.0001` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3176` n `62` status `ready` deltaP `3.7087` edge `-0.0029` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.4878` n `62` status `ready` deltaP `-2.4773` edge `0.0167` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7417` n `62` status `ready` deltaP `0.9465` edge `-0.0152` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9397` n `62` status `ready` deltaP `-2.6946` edge `-0.0109` maxDD `-1.6224`
- `market_context_high->commodity_4h` score `-1.1514` n `51` status `ready` deltaP `0.0389` edge `0.0036` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
