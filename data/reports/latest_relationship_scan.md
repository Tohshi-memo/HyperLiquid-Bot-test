# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T18:52:23.220782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6735`

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

- `market_context_high->unknown_24h` score `7284.1903` n `55` status `ready` deltaP `1.3889` edge `607.0066` maxDD `0.0`
- `market_context_high->unknown_4h` score `380.6662` n `55` status `ready` deltaP `6.8708` edge `31.6807` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `52.6658` n `55` status `ready` deltaP `4.2107` edge `4.3718` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.1636` n `55` status `ready` deltaP `42.7999` edge `1.5019` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.2168` n `94` status `ready` deltaP `30.9619` edge `1.0306` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.5159` n `55` status `ready` deltaP `52.6042` edge `0.1923` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.2043` n `55` status `ready` deltaP `43.5322` edge `0.2579` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.1846` n `55` status `ready` deltaP `24.5122` edge `0.3814` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.6721` n `55` status `ready` deltaP `31.3498` edge `0.2973` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.5068` n `55` status `ready` deltaP `6.2001` edge `0.3211` maxDD `-2.283`
- `market_context_high->commodity_4h` score `3.3395` n `55` status `ready` deltaP `31.5244` edge `0.0932` maxDD `-0.3387`
- `news_risk_high->crypto_alt_4h` score `2.5067` n `126` status `ready` deltaP `10.3852` edge `0.2783` maxDD `-7.4246`
- `market_context_high->crypto_major_24h` score `2.4084` n `55` status `ready` deltaP `10.685` edge `0.3052` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.9013` n `55` status `ready` deltaP `-4.2992` edge `0.4242` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7054` n `55` status `ready` deltaP `19.8752` edge `0.0521` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6495` n `55` status `ready` deltaP `4.2243` edge `0.1618` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.501` n `55` status `ready` deltaP `4.5237` edge `0.162` maxDD `-2.3659`
- `market_context_high->crypto_major_1h` score `1.4779` n `55` status `ready` deltaP `8.6309` edge `0.1266` maxDD `-2.2118`
- `market_context_high->metal_1h` score `0.951` n `55` status `ready` deltaP `11.7746` edge `0.0256` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.5389` n `55` status `ready` deltaP `13.1873` edge `-0.0004` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
