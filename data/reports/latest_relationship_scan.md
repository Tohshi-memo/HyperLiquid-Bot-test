# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T10:52:18.398953+00:00`
- Price records: `672`
- Market context records: `1519`
- Flow alert records: `6285`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `14.2043` n `160` status `ready` deltaP `24.2014` edge `1.1224` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2731` n `160` status `ready` deltaP `28.8542` edge `0.9487` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7037` n `160` status `ready` deltaP `28.0903` edge `0.8179` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.7134` n `160` status `ready` deltaP `19.7222` edge `0.2866` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.3955` n `160` status `ready` deltaP `12.9167` edge `0.3462` maxDD `-14.2815`
- `market_context_high->fx_24h` score `1.0277` n `160` status `ready` deltaP `19.1319` edge `0.063` maxDD `-1.3925`
- `market_context_high->equity_4h` score `0.7526` n `185` status `ready` deltaP `5.3873` edge `0.1098` maxDD `-3.6396`
- `market_context_high->index_1h` score `-0.5778` n `197` status `ready` deltaP `0.6429` edge `0.0024` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.6022` n `197` status `ready` deltaP `-0.4103` edge `0.0279` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.7905` n `197` status `ready` deltaP `-1.4787` edge `0.0165` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.8273` n `185` status `ready` deltaP `9.0442` edge `0.1656` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-0.8719` n `185` status `ready` deltaP `4.6366` edge `0.1282` maxDD `-13.3376`
- `market_context_high->fx_1h` score `-0.8787` n `197` status `ready` deltaP `-1.035` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-1.0529` n `197` status `ready` deltaP `-1.3344` edge `0.0096` maxDD `-6.1883`
- `market_context_high->metal_1h` score `-1.097` n `197` status `ready` deltaP `5.5898` edge `0.0049` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.177` n `185` status `ready` deltaP `10.8454` edge `0.0988` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.223` n `197` status `ready` deltaP `-1.0023` edge `-0.0031` maxDD `-4.7041`
- `market_context_high->index_4h` score `-1.3523` n `185` status `ready` deltaP `-4.4537` edge `0.0259` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-1.7126` n `185` status `ready` deltaP `-5.8693` edge `-0.0107` maxDD `-1.4313`
- `market_context_high->unknown_24h` score `-1.9297` n `160` status `ready` deltaP `-2.3611` edge `0.1279` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
