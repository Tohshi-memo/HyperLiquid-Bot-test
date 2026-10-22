# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T10:37:34.086923+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7500`

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

- `risk_on_high->commodity_24h` score `0.6378` n `37` status `ready` deltaP `16.7611` edge `0.0498` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6378` n `37` status `ready` deltaP `16.7611` edge `0.0498` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.6031` n `37` status `ready` deltaP `16.3457` edge `0.0107` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.6031` n `37` status `ready` deltaP `16.3457` edge `0.0107` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5768` n `37` status `ready` deltaP `14.3996` edge `0.005` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5768` n `37` status `ready` deltaP `14.3996` edge `0.005` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.3435` n `78` status `ready` deltaP `13.7119` edge `0.0602` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.097` n `37` status `ready` deltaP `5.5511` edge `0.0013` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.097` n `37` status `ready` deltaP `5.5511` edge `0.0013` maxDD `-0.0698`
- `market_context_high->index_1h` score `0.0512` n `78` status `ready` deltaP `6.2222` edge `0.0006` maxDD `-0.5082`
- `risk_on_high->fx_4h` score `-0.2626` n `37` status `ready` deltaP `-0.8941` edge `-0.0013` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2626` n `37` status `ready` deltaP `-0.8941` edge `-0.0013` maxDD `-0.1126`
- `risk_on_high->index_4h` score `-0.3005` n `37` status `ready` deltaP `6.6868` edge `0.0014` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3005` n `37` status `ready` deltaP `6.6868` edge `0.0014` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4197` n `78` status `ready` deltaP `0.7677` edge `0.0076` maxDD `-0.9891`
- `market_context_high->commodity_4h` score `-0.4199` n `78` status `ready` deltaP `5.4057` edge `0.0133` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.6386` n `78` status `ready` deltaP `-5.8307` edge `-0.0055` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.8213` n `37` status `ready` deltaP `-6.3158` edge `-0.0003` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.8213` n `37` status `ready` deltaP `-6.3158` edge `-0.0003` maxDD `-0.0831`
- `risk_on_high->commodity_1h` score `-0.8495` n `37` status `ready` deltaP `-3.1478` edge `-0.0214` maxDD `-0.9891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
