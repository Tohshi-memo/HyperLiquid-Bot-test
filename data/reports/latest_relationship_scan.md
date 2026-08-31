# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T20:07:33.898402+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `risk_on_high->unknown_4h` score `7.8562` n `107` status `ready` deltaP `23.7264` edge `0.5582` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8562` n `107` status `ready` deltaP `23.7264` edge `0.5582` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.309` n `159` status `ready` deltaP `20.423` edge `0.459` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.3587` n `107` status `ready` deltaP `6.3658` edge `0.2118` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.3587` n `107` status `ready` deltaP `6.3658` edge `0.2118` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.1349` n `159` status `ready` deltaP `5.7075` edge `0.2029` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `2.0322` n `86` status `ready` deltaP `14.0019` edge `0.1748` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `2.0322` n `86` status `ready` deltaP `14.0019` edge `0.1748` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.4531` n `61` status `ready` deltaP `3.4701` edge `0.1326` maxDD `-1.1049`
- `risk_on_high->crypto_alt_24h` score `1.252` n `86` status `ready` deltaP `15.7946` edge `0.7116` maxDD `-41.5109`
- `risk_on_and_context->crypto_alt_24h` score `1.252` n `86` status `ready` deltaP `15.7946` edge `0.7116` maxDD `-41.5109`
- `risk_on_high->fx_24h` score `1.1672` n `86` status `ready` deltaP `43.641` edge `0.0255` maxDD `-3.0108`
- `risk_on_and_context->fx_24h` score `1.1672` n `86` status `ready` deltaP `43.641` edge `0.0255` maxDD `-3.0108`
- `market_context_high->fx_24h` score `0.38` n `129` status `ready` deltaP `29.2999` edge `0.0198` maxDD `-3.6771`
- `news_risk_high->commodity_4h` score `0.2281` n `61` status `ready` deltaP `7.0347` edge `0.024` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2198` n `159` status `ready` deltaP `9.7795` edge `0.0181` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1463` n `61` status `ready` deltaP `10.6533` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0278` n `107` status `ready` deltaP `6.0706` edge `0.0153` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0278` n `107` status `ready` deltaP `6.0706` edge `0.0153` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `-0.0174` n `159` status `ready` deltaP `6.5089` edge `0.0449` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
