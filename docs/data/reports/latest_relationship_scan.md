# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T22:52:25.777147+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8896`

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

- `market_context_high->unknown_4h` score `39.82` n `91` status `ready` deltaP `-3.5965` edge `3.3962` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.135` n `49` status `ready` deltaP `43.2927` edge `0.8893` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `13.6898` n `49` status `ready` deltaP `44.5464` edge `0.8506` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.1558` n `49` status `ready` deltaP `26.8454` edge `0.6773` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.0293` n `90` status `ready` deltaP `21.9122` edge `1.3089` maxDD `-16.7906`
- `market_context_high->equity_24h` score `7.4873` n `90` status `ready` deltaP `26.1198` edge `0.4927` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.5642` n `49` status `ready` deltaP `46.9671` edge `0.2339` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.8977` n `49` status `ready` deltaP `32.3855` edge `0.2961` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5575` n `49` status `ready` deltaP `45.5202` edge `0.0808` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.0486` n `49` status `ready` deltaP `11.863` edge `0.2105` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.927` n `90` status `ready` deltaP `13.6145` edge `0.8783` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.5855` n `49` status `ready` deltaP `6.04` edge `0.2069` maxDD `-1.2034`
- `news_risk_high->index_1h` score `2.4266` n `49` status `ready` deltaP `29.986` edge `0.0163` maxDD `-0.1194`
- `news_risk_high->commodity_24h` score `2.2726` n `49` status `ready` deltaP `29.5406` edge `0.0009` maxDD `-0.0096`
- `market_context_high->crypto_major_4h` score `1.699` n `91` status `ready` deltaP `17.8588` edge `0.2318` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.3558` n `90` status `ready` deltaP `22.952` edge `0.1693` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2473` n `49` status `ready` deltaP `19.3629` edge `0.0724` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.5807` n `91` status `ready` deltaP `16.6008` edge `0.0124` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4643` n `91` status `ready` deltaP `9.0923` edge `0.0023` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.2701` n `91` status `ready` deltaP `10.2932` edge `0.0549` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
