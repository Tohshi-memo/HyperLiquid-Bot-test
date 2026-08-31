# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T19:37:26.203506+00:00`
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

- `risk_on_high->unknown_4h` score `7.8574` n `107` status `ready` deltaP `23.7264` edge `0.5583` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.8574` n `107` status `ready` deltaP `23.7264` edge `0.5583` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.3102` n `159` status `ready` deltaP `20.423` edge `0.4591` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.4451` n `107` status `ready` deltaP `6.6652` edge `0.217` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.4451` n `107` status `ready` deltaP `6.6652` edge `0.217` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `2.2212` n `159` status `ready` deltaP `6.0069` edge `0.2081` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `2.0412` n `84` status `ready` deltaP `13.7401` edge `0.1773` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `2.0412` n `84` status `ready` deltaP `13.7401` edge `0.1773` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `1.8005` n `84` status `ready` deltaP `17.2619` edge `0.7398` maxDD `-39.5903`
- `risk_on_and_context->crypto_alt_24h` score `1.8005` n `84` status `ready` deltaP `17.2619` edge `0.7398` maxDD `-39.5903`
- `news_risk_high->unknown_1h` score `1.5394` n `61` status `ready` deltaP `3.7695` edge `0.1378` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `1.3193` n `84` status `ready` deltaP `44.8165` edge `0.0266` maxDD `-2.8322`
- `risk_on_and_context->fx_24h` score `1.3193` n `84` status `ready` deltaP `44.8165` edge `0.0266` maxDD `-2.8322`
- `market_context_high->fx_24h` score `0.5475` n `127` status `ready` deltaP `29.734` edge `0.0203` maxDD `-3.4986`
- `market_context_high->commodity_1h` score `0.2486` n `159` status `ready` deltaP `10.0789` edge `0.0185` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.2486` n `61` status `ready` deltaP `7.3396` edge `0.0246` maxDD `-1.3325`
- `news_risk_high->fx_4h` score `0.1585` n `61` status `ready` deltaP `10.8057` edge `0.0005` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `0.0465` n `107` status `ready` deltaP `6.37` edge `0.0157` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `0.0465` n `107` status `ready` deltaP `6.37` edge `0.0157` maxDD `-0.8428`
- `market_context_high->commodity_4h` score `0.0142` n `159` status `ready` deltaP `6.8138` edge `0.0455` maxDD `-2.1795`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
