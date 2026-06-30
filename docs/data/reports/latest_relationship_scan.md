# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T18:07:27.472037+00:00`
- Price records: `672`
- Market context records: `5272`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9652`

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

- `market_context_high->unknown_24h` score `26.3165` n `152` status `ready` deltaP `29.2398` edge `2.0071` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `8.3473` n `152` status `ready` deltaP `26.1696` edge `0.9069` maxDD `-24.1937`
- `market_context_high->crypto_alt_4h` score `4.3621` n `167` status `ready` deltaP `16.1083` edge `0.4202` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8041` n `167` status `ready` deltaP `14.8888` edge `0.447` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.6364` n `152` status `ready` deltaP `19.8922` edge `0.7333` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `1.2071` n `167` status `ready` deltaP `15.8564` edge `0.0971` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.8267` n `167` status `ready` deltaP `9.0085` edge `0.1727` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5675` n `152` status `ready` deltaP `13.2036` edge `0.0488` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5072` n `177` status `ready` deltaP `4.9376` edge `0.1055` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.262` n `177` status `ready` deltaP `5.6379` edge `0.1088` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.257` n `152` status `ready` deltaP `21.0069` edge `0.0564` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0529` n `177` status `ready` deltaP `6.5598` edge `0.0572` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0051` n `177` status `ready` deltaP `5.8789` edge `0.0116` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.306` n `177` status `ready` deltaP `3.3585` edge `0.0113` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3348` n `177` status `ready` deltaP `0.263` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.5618` n `167` status `ready` deltaP `5.9277` edge `0.0254` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.6826` n `167` status `ready` deltaP `1.9205` edge `0.0026` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4407` n `177` status `ready` deltaP `-3.257` edge `-0.0074` maxDD `-3.2759`
- `market_context_high->metal_4h` score `-1.5572` n `167` status `ready` deltaP `-1.7252` edge `0.0122` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-1.9344` n `177` status `ready` deltaP `6.7577` edge `-0.1421` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
