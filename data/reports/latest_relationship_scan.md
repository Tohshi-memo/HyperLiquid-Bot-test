# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T06:37:24.589362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11466`

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

- `risk_on_high->unknown_4h` score `21.0257` n `133` status `ready` deltaP `8.846` edge `1.755` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `21.0257` n `133` status `ready` deltaP `8.846` edge `1.755` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `14.8516` n `173` status `ready` deltaP `11.1712` edge `1.2327` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `12.5864` n `133` status `ready` deltaP `-0.9039` edge `1.1126` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `12.5864` n `133` status `ready` deltaP `-0.9039` edge `1.1126` maxDD `-1.95`
- `market_context_high->unknown_1h` score `10.8566` n `183` status `ready` deltaP `0.8957` edge `0.9618` maxDD `-2.0446`
- `market_context_high->equity_24h` score `1.4261` n `154` status `ready` deltaP `16.7861` edge `0.4415` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `1.3827` n `132` status `ready` deltaP `13.4311` edge `0.4402` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `1.3827` n `132` status `ready` deltaP `13.4311` edge `0.4402` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.2711` n `67` status `ready` deltaP `5.1852` edge `0.0361` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.1296` n `133` status `ready` deltaP `12.5625` edge `0.0041` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1296` n `133` status `ready` deltaP `12.5625` edge `0.0041` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.124` n `67` status `ready` deltaP `3.4275` edge `-0.0034` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1621` n `133` status `ready` deltaP `3.8427` edge `-0.0019` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1621` n `133` status `ready` deltaP `3.8427` edge `-0.0019` maxDD `-0.5605`
- `news_risk_high->commodity_1h` score `-0.1741` n `67` status `ready` deltaP `4.4575` edge `0.0004` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.1862` n `133` status `ready` deltaP `5.0504` edge `0.0525` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1862` n `133` status `ready` deltaP `5.0504` edge `0.0525` maxDD `-5.4685`
- `news_risk_high->commodity_24h` score `-0.1961` n `67` status `ready` deltaP `4.2781` edge `-0.0256` maxDD `-0.2074`
- `market_context_high->metal_1h` score `-0.36` n `183` status `ready` deltaP `6.0297` edge `-0.0007` maxDD `-2.1858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
