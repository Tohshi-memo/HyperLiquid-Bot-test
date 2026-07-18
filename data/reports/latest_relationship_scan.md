# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T20:07:25.101355+00:00`
- Price records: `672`
- Market context records: `7176`
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

- `risk_on_high->commodity_1h` score `1.9993` n `34` status `ready` deltaP `21.6802` edge `0.0371` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.9993` n `34` status `ready` deltaP `21.6802` edge `0.0371` maxDD `-0.2021`
- `risk_on_high->crypto_major_1h` score `0.4329` n `34` status `ready` deltaP `8.9732` edge `0.0247` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4329` n `34` status `ready` deltaP `8.9732` edge `0.0247` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3898` n `34` status `ready` deltaP `4.2444` edge `0.0342` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3898` n `34` status `ready` deltaP `4.2444` edge `0.0342` maxDD `-0.7345`
- `market_context_high->fx_1h` score `-0.2625` n `174` status `ready` deltaP `2.1732` edge `0.0008` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5436` n `174` status `ready` deltaP `4.7474` edge `0.0397` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5835` n `174` status `ready` deltaP `0.222` edge `0.0276` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.5933` n `174` status `ready` deltaP `-0.1927` edge `-0.0127` maxDD `-1.9668`
- `market_context_high->fx_4h` score `-0.6796` n `162` status `ready` deltaP `9.0014` edge `0.0088` maxDD `-1.3685`
- `market_context_high->unknown_1h` score `-0.6903` n `174` status `ready` deltaP `-1.5796` edge `0.0172` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.8024` n `174` status `ready` deltaP `0.5403` edge `-0.004` maxDD `-2.3175`
- `risk_on_high->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `risk_on_and_context->fx_1h` score `-1.0315` n `34` status `ready` deltaP `-8.3744` edge `-0.0023` maxDD `-0.2261`
- `market_context_high->metal_1h` score `-1.37` n `174` status `ready` deltaP `-7.9307` edge `-0.005` maxDD `-2.0882`
- `risk_on_high->crypto_alt_1h` score `-1.5331` n `34` status `ready` deltaP `-12.7598` edge `-0.0005` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.5331` n `34` status `ready` deltaP `-12.7598` edge `-0.0005` maxDD `-1.3755`
- `risk_on_high->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`
- `risk_on_and_context->index_1h` score `-1.5454` n `34` status `ready` deltaP `-14.3008` edge `-0.0004` maxDD `-0.3101`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
