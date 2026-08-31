# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T18:37:24.934874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `risk_on_high->unknown_4h` score `7.8694` n `107` status `ready` deltaP `23.7264` edge `0.5593` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8694` n `107` status `ready` deltaP `23.7264` edge `0.5593` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3222` n `159` status `ready` deltaP `20.423` edge `0.4601` maxDD `-2.5526`
- `risk_on_high->crypto_alt_24h` score `3.0404` n `80` status `ready` deltaP `20.4167` edge `0.8074` maxDD `-35.2973`
- `risk_on_and_context->crypto_alt_24h` score `3.0404` n `80` status `ready` deltaP `20.4167` edge `0.8074` maxDD `-35.2973`
- `risk_on_high->unknown_1h` score `2.493` n `107` status `ready` deltaP `7.1143` edge `0.218` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.493` n `107` status `ready` deltaP `7.1143` edge `0.218` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2691` n `159` status `ready` deltaP `6.456` edge `0.2091` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.9584` n `80` status `ready` deltaP `13.125` edge `0.1745` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.9584` n `80` status `ready` deltaP `13.125` edge `0.1745` maxDD `-0.5706`
- `risk_on_high->fx_24h` score `1.6397` n `80` status `ready` deltaP `47.3958` edge `0.0292` maxDD `-2.4629`
- `risk_on_and_context->fx_24h` score `1.6397` n `80` status `ready` deltaP `47.3958` edge `0.0292` maxDD `-2.4629`
- `news_risk_high->unknown_1h` score `1.5874` n `61` status `ready` deltaP `4.2186` edge `0.1388` maxDD `-1.1049`
- `market_context_high->fx_24h` score `0.7417` n `123` status `ready` deltaP `30.6783` edge `0.0214` maxDD `-3.1293`
- `news_risk_high->commodity_4h` score `0.285` n `61` status `ready` deltaP `7.9493` edge `0.0252` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.2198` n `159` status `ready` deltaP `9.7795` edge `0.0181` maxDD `-1.5315`
- `news_risk_high->fx_4h` score `0.1451` n `61` status `ready` deltaP `10.6533` edge `0.0004` maxDD `-0.7461`
- `news_risk_high->commodity_24h` score `0.1027` n `44` status `ready` deltaP `4.2614` edge `0.0163` maxDD `-1.1904`
- `market_context_high->commodity_4h` score `0.0702` n `159` status `ready` deltaP `7.4235` edge `0.0461` maxDD `-2.1795`
- `risk_on_high->commodity_1h` score `0.0278` n `107` status `ready` deltaP `6.0706` edge `0.0153` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
