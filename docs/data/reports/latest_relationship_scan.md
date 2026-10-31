# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T14:52:28.925439+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7287`

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

- `market_context_high->unknown_24h` score `2566.7062` n `106` status `ready` deltaP `-8.2252` edge `213.99` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `99.2132` n `105` status `ready` deltaP `-5.5203` edge `8.3332` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `70.884` n `106` status `ready` deltaP `1.0182` edge `5.9135` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.6406` n `53` status `ready` deltaP `45.0111` edge `1.1751` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.2137` n `106` status `ready` deltaP `27.2832` edge `1.0283` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.8046` n `106` status `ready` deltaP `43.0195` edge `0.1319` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.489` n `98` status `ready` deltaP `16.5039` edge `0.4027` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.859` n `106` status `ready` deltaP `22.8601` edge `0.045` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.4433` n `106` status `ready` deltaP `8.6718` edge `0.2018` maxDD `-4.48`
- `market_context_high->metal_1h` score `1.0323` n `106` status `ready` deltaP `14.4051` edge `0.019` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.8593` n `106` status `ready` deltaP `11.366` edge `0.0986` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.7614` n `106` status `ready` deltaP `7.5472` edge `0.1007` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.4295` n `105` status `ready` deltaP `6.8848` edge `0.0853` maxDD `-3.9659`
- `market_context_high->crypto_major_4h` score `0.3328` n `106` status `ready` deltaP `17.8871` edge `0.1825` maxDD `-14.5879`
- `market_context_high->metal_24h` score `0.1961` n `106` status `ready` deltaP `14.9601` edge `0.1901` maxDD `-10.5088`
- `market_context_high->fx_1h` score `0.1768` n `106` status `ready` deltaP `7.4879` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.0927` n `106` status `ready` deltaP `6.995` edge `0.0002` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `-0.009` n `106` status `ready` deltaP `10.2048` edge `0.0527` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2496` n `106` status `ready` deltaP `4.8074` edge `0.003` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.4936` n `106` status `ready` deltaP `3.5335` edge `0.0907` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
