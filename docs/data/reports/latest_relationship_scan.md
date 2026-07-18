# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T18:33:08.305887+00:00`
- Price records: `672`
- Market context records: `7168`
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

- `risk_on_high->commodity_1h` score `1.6619` n `30` status `ready` deltaP `18.8423` edge `0.0279` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.6619` n `30` status `ready` deltaP `18.8423` edge `0.0279` maxDD `-0.2021`
- `risk_on_high->equity_1h` score `0.3081` n `30` status `ready` deltaP `3.4032` edge `0.033` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3081` n `30` status `ready` deltaP `3.4032` edge `0.033` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.1068` n `30` status `ready` deltaP `3.7824` edge `0.0175` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.1068` n `30` status `ready` deltaP `3.7824` edge `0.0175` maxDD `-0.9888`
- `market_context_high->fx_4h` score `-0.2151` n `159` status `ready` deltaP `9.9757` edge `0.0109` maxDD `-0.9596`
- `market_context_high->fx_1h` score `-0.4319` n `171` status `ready` deltaP `1.6257` edge `0.0011` maxDD `-0.5009`
- `market_context_high->crypto_major_1h` score `-0.5703` n `171` status `ready` deltaP `4.2503` edge `0.0396` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.5997` n `171` status `ready` deltaP `-0.105` edge `-0.0141` maxDD `-1.9668`
- `market_context_high->unknown_1h` score `-0.6058` n `171` status `ready` deltaP `-1.2283` edge `0.0219` maxDD `-1.4688`
- `risk_on_high->crypto_alt_1h` score `-0.719` n `30` status `ready` deltaP `-8.6527` edge `0.0077` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-0.719` n `30` status `ready` deltaP `-8.6527` edge `0.0077` maxDD `-1.3755`
- `risk_on_high->fx_1h` score `-0.8126` n `30` status `ready` deltaP `-5.9182` edge `-0.0012` maxDD `-0.1648`
- `risk_on_and_context->fx_1h` score `-0.8126` n `30` status `ready` deltaP `-5.9182` edge `-0.0012` maxDD `-0.1648`
- `market_context_high->crypto_alt_1h` score `-0.8154` n `171` status `ready` deltaP `1.0549` edge `0.0289` maxDD `-5.9775`
- `market_context_high->index_1h` score `-0.8363` n `171` status `ready` deltaP `0.147` edge `-0.0042` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.3453` n `171` status `ready` deltaP `-7.4553` edge `-0.005` maxDD `-2.0882`
- `risk_on_high->index_1h` score `-1.4869` n `30` status `ready` deltaP `-13.7126` edge `-0.0001` maxDD `-0.2582`
- `risk_on_and_context->index_1h` score `-1.4869` n `30` status `ready` deltaP `-13.7126` edge `-0.0001` maxDD `-0.2582`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
