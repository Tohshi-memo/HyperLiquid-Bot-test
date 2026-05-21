# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T18:22:16.143530+00:00`
- Price records: `672`
- Market context records: `1448`
- Flow alert records: `6082`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `12.9392` n `158` status `ready` deltaP `28.8305` edge `1.0877` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.8948` n `158` status `ready` deltaP `14.4075` edge `1.0619` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.8719` n `158` status `ready` deltaP `27.4525` edge `0.9195` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.3405` n `158` status `ready` deltaP `19.6114` edge `0.3396` maxDD `-5.3574`
- `market_context_high->equity_24h` score `4.0786` n `158` status `ready` deltaP `12.7901` edge `0.4873` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5202` n `220` status `ready` deltaP `7.2866` edge `0.1611` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2531` n `158` status `ready` deltaP `11.2649` edge `0.0509` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1153` n `228` status `ready` deltaP `3.5246` edge `0.0134` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1309` n `228` status `ready` deltaP `1.996` edge `0.0358` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4599` n `228` status `ready` deltaP `0.9849` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.5232` n `220` status `ready` deltaP `10.4185` edge `0.2189` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.5289` n `220` status `ready` deltaP `0.7982` edge `0.0595` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.6188` n `228` status `ready` deltaP `1.6494` edge `0.0398` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.06` n `220` status `ready` deltaP `-4.4013` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.0628` n `220` status `ready` deltaP `5.5682` edge `0.1452` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.1867` n `228` status `ready` deltaP `4.709` edge `0.0033` maxDD `-6.3532`
- `market_context_high->commodity_1h` score `-1.1937` n `228` status `ready` deltaP `-1.1766` edge `0.0005` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.7158` n `228` status `ready` deltaP `-1.56` edge `0.0031` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.9925` n `220` status `ready` deltaP `7.4169` edge `0.0537` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-2.9867` n `220` status `ready` deltaP `-11.3609` edge `-0.0494` maxDD `-8.2885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
