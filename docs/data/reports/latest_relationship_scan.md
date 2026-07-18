# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T20:22:23.592707+00:00`
- Price records: `672`
- Market context records: `7177`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->commodity_1h` score `2.0125` n `34` status `ready` deltaP `21.8299` edge `0.0372` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0125` n `34` status `ready` deltaP `21.8299` edge `0.0372` maxDD `-0.2021`
- `risk_on_high->crypto_major_1h` score `0.4297` n `34` status `ready` deltaP `8.9732` edge `0.0243` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4297` n `34` status `ready` deltaP `8.9732` edge `0.0243` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.403` n `34` status `ready` deltaP `4.3941` edge `0.0343` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.403` n `34` status `ready` deltaP `4.3941` edge `0.0343` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.2625` n `174` status `ready` deltaP `2.1732` edge `0.0008` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5468` n `174` status `ready` deltaP `4.7474` edge `0.0393` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.5848` n `174` status `ready` deltaP `-0.043` edge `-0.0126` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.585` n `174` status `ready` deltaP `0.222` edge `0.0274` maxDD `-5.9775`
- `market_context_high->unknown_1h` score `-0.7071` n `174` status `ready` deltaP `-1.7293` edge `0.0168` maxDD `-1.4688`
- `market_context_high->fx_4h` score `-0.7461` n `163` status `ready` deltaP `8.8433` edge `0.0087` maxDD `-1.3866`
- `market_context_high->index_1h` score `-0.8024` n `174` status `ready` deltaP `0.5403` edge `-0.004` maxDD `-2.3175`
- `risk_on_high->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `risk_on_and_context->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `market_context_high->metal_1h` score `-1.37` n `174` status `ready` deltaP `-7.9307` edge `-0.005` maxDD `-2.0882`
- `risk_on_high->crypto_alt_1h` score `-1.5355` n `34` status `ready` deltaP `-12.7598` edge `-0.0007` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.5355` n `34` status `ready` deltaP `-12.7598` edge `-0.0007` maxDD `-1.3755`
- `risk_on_high->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`
- `risk_on_and_context->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
