# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T11:52:32.089350+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0353` n `54` status `ready` deltaP `38.5017` edge `0.3296` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0353` n `54` status `ready` deltaP `38.5017` edge `0.3296` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.4873` n `147` status `ready` deltaP `21.0054` edge `0.4494` maxDD `-5.906`
- `market_context_high->crypto_alt_4h` score `5.1587` n `147` status `ready` deltaP `13.0423` edge `0.5221` maxDD `-7.999`
- `risk_on_high->crypto_major_4h` score `5.0873` n `73` status `ready` deltaP `27.6311` edge `0.325` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.0873` n `73` status `ready` deltaP `27.6311` edge `0.325` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `1.0491` n `73` status `ready` deltaP `5.2518` edge `0.2307` maxDD `-7.9298`
- `risk_on_and_context->crypto_alt_4h` score `1.0491` n `73` status `ready` deltaP `5.2518` edge `0.2307` maxDD `-7.9298`
- `market_context_high->crypto_major_1h` score `0.758` n `159` status `ready` deltaP `6.0944` edge `0.1031` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.4737` n `159` status `ready` deltaP `7.6517` edge `0.1199` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.4283` n `147` status `ready` deltaP `13.8045` edge `0.0482` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.274` n `85` status `ready` deltaP `8.1965` edge `0.0066` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.274` n `85` status `ready` deltaP `8.1965` edge `0.0066` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1234` n `159` status `ready` deltaP `8.0855` edge `0.0051` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2705` n `159` status `ready` deltaP `8.3399` edge `0.0088` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.2834` n `85` status `ready` deltaP `11.475` edge `0.0295` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2834` n `85` status `ready` deltaP `11.475` edge `0.0295` maxDD `-5.3696`
- `market_context_high->equity_4h` score `-0.345` n `147` status `ready` deltaP `14.6508` edge `0.2007` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.3468` n `159` status `ready` deltaP `10.1876` edge `0.0386` maxDD `-7.0778`
- `risk_on_high->fx_1h` score `-0.3722` n `85` status `ready` deltaP `-0.9133` edge `-0.0036` maxDD `-0.376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
