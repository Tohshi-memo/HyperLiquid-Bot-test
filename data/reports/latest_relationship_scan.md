# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T12:22:32.839303+00:00`
- Price records: `672`
- Market context records: `2039`
- Flow alert records: `7764`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `8.9335` n `205` status `ready` deltaP `31.118` edge `0.59` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4414` n `205` status `ready` deltaP `24.8573` edge `0.6522` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.0198` n `205` status `ready` deltaP `19.315` edge `0.4478` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9491` n `205` status `ready` deltaP `17.1458` edge `0.2409` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6864` n `203` status `ready` deltaP `17.3205` edge `0.5571` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.5824` n `205` status `ready` deltaP `12.7775` edge `0.1453` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.428` n `205` status `ready` deltaP `12.8194` edge `0.1019` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.2852` n `205` status `ready` deltaP `10.2402` edge `0.1502` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.6413` n `203` status `ready` deltaP `16.4374` edge `0.4337` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.4867` n `203` status `ready` deltaP `4.7696` edge `0.1316` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.2162` n `205` status `ready` deltaP `6.9385` edge `0.0506` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.0923` n `205` status `ready` deltaP `4.2082` edge `0.0516` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.2791` n `205` status `ready` deltaP `2.7266` edge `0.0176` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5383` n `203` status `ready` deltaP `10.7302` edge `0.0219` maxDD `-2.7303`
- `market_context_high->metal_1h` score `-0.7773` n `205` status `ready` deltaP `4.4048` edge `0.0246` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8396` n `205` status `ready` deltaP `-1.1394` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-1.0539` n `205` status `ready` deltaP `9.321` edge `0.1123` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.4841` n `205` status `ready` deltaP `-5.1954` edge `-0.0009` maxDD `-1.0513`
- `market_context_high->crypto_major_24h` score `-1.6957` n `203` status `ready` deltaP `16.7811` edge `0.6054` maxDD `-62.3533`
- `market_context_high->metal_24h` score `-1.761` n `203` status `ready` deltaP `10.0317` edge `0.1349` maxDD `-20.5491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
