# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T18:52:28.893890+00:00`
- Price records: `672`
- Market context records: `7170`
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

- `risk_on_high->commodity_1h` score `1.8003` n `31` status `ready` deltaP `19.7025` edge `0.0337` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `1.8003` n `31` status `ready` deltaP `19.7025` edge `0.0337` maxDD `-0.2021`
- `risk_on_high->equity_1h` score `0.1924` n `31` status `ready` deltaP `2.0475` edge `0.0324` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.1924` n `31` status `ready` deltaP `2.0475` edge `0.0324` maxDD `-0.7345`
- `risk_on_high->crypto_major_1h` score `0.1858` n `31` status `ready` deltaP `5.2878` edge `0.0176` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.1858` n `31` status `ready` deltaP `5.2878` edge `0.0176` maxDD `-0.9888`
- `market_context_high->fx_4h` score `-0.2837` n `159` status `ready` deltaP `9.9757` edge `0.0105` maxDD `-1.0516`
- `market_context_high->fx_1h` score `-0.4411` n `171` status `ready` deltaP `1.6257` edge `0.0009` maxDD `-0.5466`
- `market_context_high->crypto_major_1h` score `-0.5742` n `171` status `ready` deltaP `4.2503` edge `0.0391` maxDD `-7.6171`
- `market_context_high->unknown_1h` score `-0.6106` n `171` status `ready` deltaP `-1.2283` edge `0.0215` maxDD `-1.4688`
- `market_context_high->index_1h` score `-0.8363` n `171` status `ready` deltaP `0.147` edge `-0.0042` maxDD `-2.3175`
- `market_context_high->crypto_alt_1h` score `-0.9006` n `171` status `ready` deltaP `0.1847` edge `0.0276` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.9106` n `171` status `ready` deltaP `-0.105` edge `-0.0131` maxDD `-1.9668`
- `risk_on_high->fx_1h` score `-0.9367` n `31` status `ready` deltaP `-7.316` edge `-0.0019` maxDD `-0.191`
- `risk_on_and_context->fx_1h` score `-0.9367` n `31` status `ready` deltaP `-7.316` edge `-0.0019` maxDD `-0.191`
- `risk_on_high->crypto_alt_1h` score `-1.2514` n `31` status `ready` deltaP `-9.6436` edge `0.0022` maxDD `-1.3755`
- `risk_on_and_context->crypto_alt_1h` score `-1.2514` n `31` status `ready` deltaP `-9.6436` edge `0.0022` maxDD `-1.3755`
- `market_context_high->metal_1h` score `-1.3695` n `171` status `ready` deltaP `-7.8904` edge `-0.0052` maxDD `-2.0882`
- `risk_on_high->index_1h` score `-1.5742` n `31` status `ready` deltaP `-14.6803` edge `-0.0006` maxDD `-0.284`
- `risk_on_and_context->index_1h` score `-1.5742` n `31` status `ready` deltaP `-14.6803` edge `-0.0006` maxDD `-0.284`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
