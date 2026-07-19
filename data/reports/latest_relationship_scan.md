# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T15:37:26.766924+00:00`
- Price records: `672`
- Market context records: `7263`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13759`

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

- `risk_on_high->crypto_major_4h` score `6.2341` n `34` status `ready` deltaP `28.7572` edge `0.3661` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.2341` n `34` status `ready` deltaP `28.7572` edge `0.3661` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.5598` n `34` status `ready` deltaP `19.5391` edge `0.289` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.5598` n `34` status `ready` deltaP `19.5391` edge `0.289` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.1134` n `34` status `ready` deltaP `22.7168` edge `0.0397` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.1134` n `34` status `ready` deltaP `22.7168` edge `0.0397` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.1254` n `34` status `ready` deltaP `5.7744` edge `0.1396` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.1254` n `34` status `ready` deltaP `5.7744` edge `0.1396` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.3448` n `34` status `ready` deltaP `8.3744` edge `0.0174` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.3448` n `34` status `ready` deltaP `8.3744` edge `0.0174` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3075` n `34` status `ready` deltaP `3.6654` edge `0.0312` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3075` n `34` status `ready` deltaP `3.6654` edge `0.0312` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1729` n `34` status `ready` deltaP `2.6094` edge `0.0203` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1729` n `34` status `ready` deltaP `2.6094` edge `0.0203` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2318` n `144` status `ready` deltaP `2.7778` edge `0.0007` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5941` n `144` status `ready` deltaP `-0.2816` edge `-0.0122` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.632` n `34` status `ready` deltaP `-0.045` edge `-0.0096` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.632` n `34` status `ready` deltaP `-0.045` edge `-0.0096` maxDD `-0.7546`
- `market_context_high->crypto_alt_1h` score `-0.83` n `144` status `ready` deltaP `-1.8796` edge `0.01` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9624` n `144` status `ready` deltaP `0.9398` edge `0.0114` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
