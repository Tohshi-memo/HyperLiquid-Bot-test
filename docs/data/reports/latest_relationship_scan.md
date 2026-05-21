# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T19:22:18.223549+00:00`
- Price records: `672`
- Market context records: `1452`
- Flow alert records: `6094`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8809`

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

- `market_context_high->crypto_alt_24h` score `13.279` n `162` status `ready` deltaP `28.8773` edge `1.1157` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `12.0786` n `162` status `ready` deltaP `27.5463` edge `0.9361` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.5676` n `162` status `ready` deltaP `14.892` edge `1.0314` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.4058` n `162` status `ready` deltaP `13.0402` edge `0.5129` maxDD `-14.2815`
- `market_context_high->index_24h` score `4.4012` n `162` status `ready` deltaP `19.8302` edge `0.3432` maxDD `-5.3574`
- `market_context_high->equity_4h` score `1.5996` n `224` status `ready` deltaP `7.3497` edge `0.1673` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2413` n `162` status `ready` deltaP `11.4776` edge `0.0485` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.065` n `228` status `ready` deltaP `3.9737` edge `0.0146` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0674` n `228` status `ready` deltaP `2.4451` edge `0.0381` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.3637` n `224` status `ready` deltaP `10.8667` edge `0.2292` maxDD `-19.5565`
- `market_context_high->index_4h` score `-0.4236` n `224` status `ready` deltaP `1.3502` edge `0.0646` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.4677` n `228` status `ready` deltaP `0.8352` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5289` n `228` status `ready` deltaP `2.0985` edge `0.0443` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0021` n `224` status `ready` deltaP `-3.4516` edge `-0.0084` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1171` n `228` status `ready` deltaP `5.1581` edge `0.0061` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.1513` n `224` status `ready` deltaP `5.3463` edge `0.1393` maxDD `-13.3376`
- `market_context_high->commodity_1h` score `-1.2201` n `228` status `ready` deltaP `-1.3263` edge `-0.0007` maxDD `-4.7041`
- `market_context_high->crypto_major_1h` score `-1.6223` n `228` status `ready` deltaP `-0.9612` edge `0.0069` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7654` n `224` status `ready` deltaP `8.1555` edge `0.0677` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-3.77` n `224` status `ready` deltaP `-12.0427` edge `-0.0692` maxDD `-14.3745`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
