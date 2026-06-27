# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T00:52:25.841526+00:00`
- Price records: `672`
- Market context records: `4882`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7586`

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

- `market_context_high->unknown_1h` score `16.0447` n `110` status `ready` deltaP `9.7224` edge `1.314` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5141` n `110` status `ready` deltaP `22.7051` edge `0.6946` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4194` n `110` status `ready` deltaP `21.056` edge `0.5298` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1856` n `110` status `ready` deltaP `18.4922` edge `0.5146` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.0284` n `91` status `ready` deltaP `24.2541` edge `0.2916` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1235` n `110` status `ready` deltaP `8.0627` edge `0.1061` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.868` n `110` status `ready` deltaP `12.439` edge `0.1665` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5905` n `110` status `ready` deltaP `12.1452` edge `0.041` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4718` n `110` status `ready` deltaP `6.4698` edge `0.1212` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4285` n `110` status `ready` deltaP `8.0212` edge `0.1037` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.1966` n `110` status `ready` deltaP `3.9358` edge `0.0587` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1939` n `110` status `ready` deltaP `0.3946` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2557` n `110` status `ready` deltaP `2.8334` edge `0.0143` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5172` n `110` status `ready` deltaP `-0.2885` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6704` n `110` status `ready` deltaP `0.9146` edge `0.005` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.9386` n `110` status `ready` deltaP `5.6624` edge `0.0027` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3226` n `110` status `ready` deltaP `-6.7175` edge `-0.0041` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.7602` n `91` status `ready` deltaP `-5.4678` edge `-0.0092` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5612` n `91` status `ready` deltaP `-5.5823` edge `-0.139` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.9422` n `91` status `ready` deltaP `13.8049` edge `0.007` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
