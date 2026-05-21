# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T11:51:10.943785+00:00`
- Price records: `672`
- Market context records: `1420`
- Flow alert records: `6002`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.8484` n `154` status `ready` deltaP `27.3539` edge `0.9182` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.5733` n `154` status `ready` deltaP `28.7811` edge `0.9742` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5245` n `154` status `ready` deltaP `11.2937` edge `1.0518` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7449` n `154` status `ready` deltaP `19.3813` edge `0.2915` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3943` n `154` status `ready` deltaP `12.5271` edge `0.3487` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8651` n `202` status `ready` deltaP `4.9324` edge `0.1222` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0503` n `154` status `ready` deltaP `9.3592` edge `0.0467` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1038` n `206` status `ready` deltaP `4.0434` edge `0.0109` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2136` n `206` status `ready` deltaP `2.5827` edge `0.025` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3287` n `206` status `ready` deltaP `3.1306` edge `-0.0017` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.521` n `206` status `ready` deltaP `0.9622` edge `0.026` maxDD `-3.9365`
- `market_context_high->commodity_1h` score `-0.7106` n `206` status `ready` deltaP `-0.7848` edge `0.0075` maxDD `-2.252`
- `market_context_high->index_4h` score `-0.7954` n `202` status `ready` deltaP `-0.7773` edge `0.0478` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.861` n `206` status `ready` deltaP `4.3966` edge `-0.0095` maxDD `-6.0825`
- `market_context_high->crypto_major_1h` score `-1.1275` n `206` status `ready` deltaP `-1.7237` edge `-0.0057` maxDD `-6.1883`
- `market_context_high->crypto_alt_4h` score `-1.3223` n `202` status `ready` deltaP `7.3442` edge `0.1728` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3768` n `202` status `ready` deltaP `5.1376` edge `0.1219` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.6396` n `202` status `ready` deltaP `-4.4207` edge `-0.0101` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5852` n `202` status `ready` deltaP `-10.0896` edge `-0.0095` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8531` n `202` status `ready` deltaP `4.149` edge `-0.0056` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
