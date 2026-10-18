# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T17:07:25.031686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9294`

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

- `market_context_high->commodity_24h` score `2.056` n `122` status `ready` deltaP `18.8368` edge `0.1309` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9025` n `87` status `ready` deltaP `20.7776` edge `0.0998` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9025` n `87` status `ready` deltaP `20.7776` edge `0.0998` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.2419` n `123` status `ready` deltaP `16.8699` edge `0.3872` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.9945` n `88` status `ready` deltaP `18.0709` edge `0.2551` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.9945` n `88` status `ready` deltaP `18.0709` edge `0.2551` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.316` n `123` status `ready` deltaP `5.0703` edge `0.0956` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0727` n `88` status `ready` deltaP `5.7705` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0727` n `88` status `ready` deltaP `5.7705` edge `0.006` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.3201` n `88` status `ready` deltaP `0.0` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3201` n `88` status `ready` deltaP `0.0` edge `-0.003` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.4059` n `88` status `ready` deltaP `9.6744` edge `0.0313` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4059` n `88` status `ready` deltaP `9.6744` edge `0.0313` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.4383` n `123` status `ready` deltaP `2.4354` edge `0.0024` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.4848` n `123` status `ready` deltaP `1.1319` edge `0.0803` maxDD `-7.3329`
- `market_context_high->metal_1h` score `-0.5333` n `123` status `ready` deltaP `1.6455` edge `0.0076` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.5445` n `88` status `ready` deltaP `-0.0545` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5445` n `88` status `ready` deltaP `-0.0545` edge `0.0037` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5732` n `123` status `ready` deltaP `-2.8455` edge `-0.0024` maxDD `-0.503`
- `risk_on_high->crypto_major_1h` score `-0.6592` n `88` status `ready` deltaP `-0.5376` edge `0.011` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
