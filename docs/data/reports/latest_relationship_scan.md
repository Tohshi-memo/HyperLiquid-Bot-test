# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T16:07:28.899252+00:00`
- Price records: `672`
- Market context records: `5263`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `26.4861` n `147` status `ready` deltaP `29.8895` edge `2.0169` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `10.3935` n `147` status `ready` deltaP `28.4297` edge `1.037` maxDD `-22.166`
- `market_context_high->crypto_alt_4h` score `4.1235` n `159` status `ready` deltaP `14.6264` edge `0.4102` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8165` n `159` status `ready` deltaP `14.1884` edge `0.4527` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.4344` n `147` status `ready` deltaP `19.5118` edge `0.719` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.8359` n `159` status `ready` deltaP `16.8018` edge `0.1432` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.5913` n `159` status `ready` deltaP `8.5107` edge `0.1564` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5197` n `147` status `ready` deltaP `12.6666` edge `0.0484` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5143` n `171` status `ready` deltaP `4.7414` edge `0.1074` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.2655` n `171` status `ready` deltaP `5.6816` edge `0.1088` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2322` n `147` status `ready` deltaP `21.0247` edge `0.0531` maxDD `-7.413`
- `market_context_high->crypto_alt_24h` score `0.0636` n `147` status `ready` deltaP `15.4018` edge `0.535` maxDD `-38.6949`
- `market_context_high->equity_1h` score `0.0053` n `171` status `ready` deltaP `6.0703` edge `0.0565` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0516` n `171` status `ready` deltaP `5.2001` edge `0.0114` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.2265` n `171` status `ready` deltaP `4.0069` edge `0.0136` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.234` n `171` status `ready` deltaP `2.1265` edge `0.0006` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.7162` n `159` status `ready` deltaP `4.7937` edge `0.0201` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.7826` n `159` status `ready` deltaP `0.2972` edge `0.0006` maxDD `-1.567`
- `market_context_high->unknown_1h` score `-0.9932` n `171` status `ready` deltaP `7.0622` edge `-0.0657` maxDD `-2.7986`
- `market_context_high->commodity_1h` score `-1.3683` n `171` status `ready` deltaP `-2.945` edge `-0.0071` maxDD `-2.9831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
