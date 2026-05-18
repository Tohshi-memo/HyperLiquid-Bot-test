# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T06:22:17.540431+00:00`
- Price records: `672`
- Market context records: `1091`
- Flow alert records: `5046`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->crypto_major_24h` score `16.5802` n `153` status `ready` deltaP `35.8258` edge `1.1892` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.7552` n `153` status `ready` deltaP `12.2998` edge `0.521` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.7283` n `153` status `ready` deltaP `14.9277` edge `0.4275` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.8852` n `153` status `ready` deltaP `-2.953` edge `0.5935` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.6862` n `153` status `ready` deltaP `15.0632` edge `0.3209` maxDD `-2.1308`
- `market_context_high->equity_4h` score `2.0129` n `164` status `ready` deltaP `10.9756` edge `0.1609` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.0265` n `164` status `ready` deltaP `8.8415` edge `0.0949` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.8752` n `164` status `ready` deltaP `10.6708` edge `0.1704` maxDD `-6.4882`
- `market_context_high->index_1h` score `0.6337` n `171` status `ready` deltaP `8.5644` edge `0.0274` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.501` n `171` status `ready` deltaP `3.5726` edge `0.0557` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.2038` n `171` status `ready` deltaP `7.5533` edge `0.0432` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0491` n `171` status `ready` deltaP `7.2399` edge `0.0014` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.112` n `171` status `ready` deltaP `7.3056` edge `0.003` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2408` n `171` status `ready` deltaP `2.9266` edge `0.0447` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.5722` n `164` status `ready` deltaP `7.0122` edge `0.156` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6174` n `164` status `ready` deltaP `2.7439` edge `0.0022` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6868` n `171` status `ready` deltaP `-0.9849` edge `-0.0007` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.6516` n `164` status `ready` deltaP `6.25` edge `-0.058` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.4199` n `164` status `ready` deltaP `9.2988` edge `-0.142` maxDD `-6.7322`
- `market_context_high->commodity_4h` score `-3.004` n `164` status `ready` deltaP `-10.0609` edge `-0.0013` maxDD `-13.0076`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
