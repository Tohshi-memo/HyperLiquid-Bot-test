# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T17:37:26.459171+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `737.766` n `136` status `ready` deltaP `1.2153` edge `61.4724` maxDD `0.0`
- `market_context_high->unknown_1h` score `212.9202` n `30` status `ready` deltaP `9.3913` edge `17.6854` maxDD `-0.0395`
- `market_context_high->equity_4h` score `4.7486` n `30` status `ready` deltaP `25.8435` edge `0.2569` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `3.8006` n `30` status `ready` deltaP `19.9187` edge `0.2382` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.6297` n `30` status `ready` deltaP `38.5874` edge `0.0523` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `3.2228` n `30` status `ready` deltaP `18.5874` edge `0.2351` maxDD `-5.2359`
- `market_context_high->equity_1h` score `2.3606` n `30` status `ready` deltaP `24.9102` edge `0.0626` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.3741` n `30` status `ready` deltaP `18.5429` edge `0.0104` maxDD `-0.2275`
- `market_context_high->metal_4h` score `1.2211` n `30` status `ready` deltaP `21.3923` edge `0.031` maxDD `-0.3647`
- `news_risk_high->index_24h` score `1.1212` n `136` status `ready` deltaP `17.5143` edge `0.0462` maxDD `-2.2287`
- `market_context_high->fx_1h` score `0.5994` n `30` status `ready` deltaP `15.5389` edge `0.0089` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.5806` n `136` status `ready` deltaP `16.6463` edge `0.1229` maxDD `-6.8392`
- `market_context_high->crypto_major_1h` score `0.5608` n `30` status `ready` deltaP `10.9381` edge `0.0596` maxDD `-4.8632`
- `news_risk_high->crypto_alt_24h` score `0.0352` n `136` status `ready` deltaP `14.2973` edge `0.3028` maxDD `-29.2814`
- `market_context_high->fx_4h` score `-0.064` n `30` status `ready` deltaP `7.9674` edge `0.0055` maxDD `-0.6787`
- `news_risk_high->index_1h` score `-0.0863` n `139` status `ready` deltaP `2.7636` edge `0.0034` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.1133` n `139` status `ready` deltaP `4.323` edge `0.0528` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `-0.2211` n `139` status `ready` deltaP `15.4358` edge `0.0396` maxDD `-9.2079`
- `market_context_high->metal_1h` score `-0.2572` n `30` status `ready` deltaP `-1.5769` edge `0.0126` maxDD `-0.215`
- `news_risk_high->equity_1h` score `-0.3168` n `139` status `ready` deltaP `2.4642` edge `0.0233` maxDD `-1.957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
