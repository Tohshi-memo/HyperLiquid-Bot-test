# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T08:07:26.786850+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11586`

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

- `risk_on_high->crypto_alt_24h` score `22.0199` n `55` status `ready` deltaP `48.6205` edge `1.5589` maxDD `-3.1772`
- `risk_on_and_context->crypto_alt_24h` score `22.0199` n `55` status `ready` deltaP `48.6205` edge `1.5589` maxDD `-3.1772`
- `risk_on_high->crypto_major_24h` score `10.6023` n `55` status `ready` deltaP `30.6029` edge `0.8213` maxDD `-9.0103`
- `risk_on_and_context->crypto_major_24h` score `10.6023` n `55` status `ready` deltaP `30.6029` edge `0.8213` maxDD `-9.0103`
- `risk_on_high->unknown_4h` score `8.0676` n `107` status `ready` deltaP `25.4032` edge `0.5646` maxDD `-2.266`
- `risk_on_and_context->unknown_4h` score `8.0676` n `107` status `ready` deltaP `25.4032` edge `0.5646` maxDD `-2.266`
- `market_context_high->unknown_4h` score `6.5216` n `159` status `ready` deltaP `22.0998` edge `0.4655` maxDD `-2.5493`
- `risk_on_high->fx_24h` score `6.428` n `55` status `ready` deltaP `71.875` edge `0.0565` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.428` n `55` status `ready` deltaP `71.875` edge `0.0565` maxDD `0.0`
- `market_context_high->metal_24h` score `5.242` n `96` status `ready` deltaP `37.1527` edge `0.25` maxDD `-1.8678`
- `market_context_high->crypto_major_24h` score `4.663` n `96` status `ready` deltaP `21.7014` edge `0.493` maxDD `-17.2607`
- `market_context_high->crypto_alt_24h` score `4.6026` n `96` status `ready` deltaP `23.0902` edge `0.8551` maxDD `-27.517`
- `risk_on_high->metal_24h` score `4.4224` n `55` status `ready` deltaP `40.5808` edge `0.1452` maxDD `-0.7767`
- `risk_on_and_context->metal_24h` score `4.4224` n `55` status `ready` deltaP `40.5808` edge `0.1452` maxDD `-0.7767`
- `risk_on_high->unknown_1h` score `2.503` n `107` status `ready` deltaP `6.5155` edge `0.2228` maxDD `-1.9453`
- `risk_on_and_context->unknown_1h` score `2.503` n `107` status `ready` deltaP `6.5155` edge `0.2228` maxDD `-1.9453`
- `market_context_high->unknown_1h` score `2.2804` n `159` status `ready` deltaP `5.8572` edge `0.214` maxDD `-2.041`
- `market_context_high->fx_24h` score `1.1207` n `96` status `ready` deltaP `38.5417` edge `0.0326` maxDD `-1.6688`
- `risk_on_high->equity_24h` score `0.999` n `55` status `ready` deltaP `20.1042` edge `0.03` maxDD `-3.7955`
- `risk_on_and_context->equity_24h` score `0.999` n `55` status `ready` deltaP `20.1042` edge `0.03` maxDD `-3.7955`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
