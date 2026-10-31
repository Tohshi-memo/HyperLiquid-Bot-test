# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T20:52:26.414217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7759`

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

- `market_context_high->unknown_24h` score `3122.7553` n `95` status `ready` deltaP `-10.0822` edge `260.3398` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `106.185` n `95` status `ready` deltaP `0.7109` edge `8.8573` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.6657` n `108` status `ready` deltaP `-5.3448` edge `6.5364` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.2848` n `77` status `ready` deltaP `45.4929` edge `1.3089` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7686` n `95` status `ready` deltaP `24.8995` edge `1.0071` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.3821` n `108` status `ready` deltaP `20.122` edge `0.453` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9264` n `95` status `ready` deltaP `43.792` edge `0.1369` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6393` n `95` status `ready` deltaP `20.2792` edge `0.0439` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.8463` n `95` status `ready` deltaP `12.0958` edge `0.0189` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8301` n `108` status `ready` deltaP `8.8767` edge `0.1054` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.6331` n `95` status `ready` deltaP `3.9746` edge `0.194` maxDD `-4.48`
- `market_context_high->equity_1h` score `0.4731` n `95` status `ready` deltaP `6.9918` edge `0.1016` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.4154` n `95` status `ready` deltaP `14.2828` edge `0.0601` maxDD `-0.8321`
- `market_context_high->crypto_major_1h` score `0.3204` n `95` status `ready` deltaP `8.9474` edge `0.0842` maxDD `-5.2213`
- `market_context_high->fx_4h` score `0.305` n `95` status `ready` deltaP `9.5138` edge `0.0011` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.2461` n `95` status `ready` deltaP `8.8071` edge `-0.0004` maxDD `-0.1407`
- `market_context_high->metal_24h` score `-0.1491` n `95` status `ready` deltaP `10.932` edge `0.1727` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.2772` n `95` status `ready` deltaP `15.3723` edge `0.136` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.3429` n `95` status `ready` deltaP `-0.9943` edge `0.0141` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.3498` n `95` status `ready` deltaP `3.6889` edge `0.0021` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
