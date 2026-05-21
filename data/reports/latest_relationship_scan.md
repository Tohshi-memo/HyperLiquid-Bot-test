# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T00:07:15.149861+00:00`
- Price records: `672`
- Market context records: `1371`
- Flow alert records: `5858`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.0605` n `143` status `ready` deltaP `31.3896` edge `0.9923` maxDD `-8.0553`
- `market_context_high->metal_24h` score `12.3106` n `143` status `ready` deltaP `13.5599` edge `1.1022` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `10.4609` n `143` status `ready` deltaP `28.6313` edge `0.8825` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.097` n `143` status `ready` deltaP `22.3279` edge `0.3012` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.5753` n `143` status `ready` deltaP `15.3737` edge `0.3448` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5532` n `168` status `ready` deltaP `8.464` edge `0.156` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.4798` n `143` status `ready` deltaP `10.4155` edge `0.0474` maxDD `-1.148`
- `market_context_high->index_1h` score `-0.0865` n `180` status `ready` deltaP `3.4531` edge `0.0124` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1071` n `168` status `ready` deltaP `10.9611` edge `0.0611` maxDD `-6.4478`
- `market_context_high->equity_1h` score `-0.1731` n `180` status `ready` deltaP `1.7632` edge `0.0219` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.2989` n `168` status `ready` deltaP `1.2412` edge `0.0623` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.4403` n `180` status `ready` deltaP `5.9581` edge `0.0027` maxDD `-3.5762`
- `market_context_high->fx_1h` score `-0.4646` n `180` status `ready` deltaP `1.6866` edge `-0.0034` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.7136` n `180` status `ready` deltaP `-0.4923` edge `0.0053` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8445` n `180` status `ready` deltaP `-0.153` edge `0.0177` maxDD `-3.6309`
- `market_context_high->crypto_major_1h` score `-1.0241` n `180` status `ready` deltaP `-2.2455` edge `-0.0098` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.3588` n `168` status `ready` deltaP `-9.277` edge `-0.0153` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.6964` n `168` status `ready` deltaP `6.3879` edge `0.148` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.9517` n `168` status `ready` deltaP `2.9762` edge `0.0884` maxDD `-13.3376`
- `market_context_high->unknown_4h` score `-3.0252` n `168` status `ready` deltaP `1.0162` edge `-0.1675` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
