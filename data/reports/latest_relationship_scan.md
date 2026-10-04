# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T03:52:33.713150+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4662`

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

- `market_context_high->unknown_4h` score `323.6574` n `50` status `ready` deltaP `13.5671` edge `26.881` maxDD `0.0`
- `market_context_high->unknown_1h` score `283.7179` n `61` status `ready` deltaP `4.5426` edge `23.6429` maxDD `-0.7351`
- `market_context_high->crypto_alt_24h` score `12.7855` n `50` status `ready` deltaP `27.8995` edge `1.0498` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `11.8957` n `59` status `ready` deltaP `31.1752` edge `0.7935` maxDD `-0.1353`
- `news_risk_high->crypto_major_4h` score `10.9452` n `65` status `ready` deltaP `40.1736` edge `0.6646` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `10.6654` n `50` status `ready` deltaP `33.6464` edge `0.8061` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.4186` n `65` status `ready` deltaP `24.6646` edge `0.5882` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.03` n `50` status `ready` deltaP `15.8659` edge `0.5504` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.5278` n `50` status `ready` deltaP `14.6646` edge `0.4918` maxDD `-7.6465`
- `news_risk_high->index_24h` score `5.0248` n `59` status `ready` deltaP `34.8354` edge `0.1865` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9023` n `65` status `ready` deltaP `26.9793` edge `0.2066` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.0892` n `65` status `ready` deltaP `33.5906` edge `0.0597` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0456` n `50` status `ready` deltaP `34.2134` edge `0.0392` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.0083` n `65` status `ready` deltaP `13.6089` edge `0.1955` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5658` n `65` status `ready` deltaP `21.9747` edge `0.1089` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.3628` n `61` status `ready` deltaP `11.3895` edge `0.166` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0577` n `61` status `ready` deltaP `8.7023` edge `0.1881` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5127` n `65` status `ready` deltaP `4.8687` edge `0.1455` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.252` n `50` status `ready` deltaP `24.0451` edge `0.102` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
