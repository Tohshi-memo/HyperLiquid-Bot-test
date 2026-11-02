# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T04:22:30.292922+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8080`

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

- `market_context_high->unknown_24h` score `7180.9843` n `43` status `ready` deltaP `1.3889` edge `598.4061` maxDD `0.0`
- `market_context_high->unknown_4h` score `453.2325` n `46` status `ready` deltaP `9.1463` edge `37.7084` maxDD `0.0`
- `market_context_high->unknown_1h` score `72.0995` n `48` status `ready` deltaP `5.0025` edge `5.986` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.1082` n `43` status `ready` deltaP `42.2925` edge `1.334` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.8268` n `94` status `ready` deltaP `34.0869` edge `1.0606` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.8207` n `43` status `ready` deltaP `44.7271` edge `0.3013` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.7092` n `46` status `ready` deltaP `29.9443` edge `0.3889` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.4086` n `43` status `ready` deltaP `49.1319` edge `0.2065` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.3601` n `46` status `ready` deltaP `28.9502` edge `0.2873` maxDD `-1.6901`
- `market_context_high->equity_4h` score `4.1397` n `46` status `ready` deltaP `5.0372` edge `0.3816` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.9421` n `46` status `ready` deltaP `30.2824` edge `0.069` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2348` n `126` status `ready` deltaP `8.8608` edge `0.2658` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.0061` n `48` status `ready` deltaP `5.6512` edge `0.182` maxDD `-1.5336`
- `market_context_high->crypto_alt_24h` score `1.5067` n `43` status `ready` deltaP `-10.2228` edge `0.3455` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.3915` n `48` status `ready` deltaP `4.017` edge `0.1504` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.2826` n `48` status `ready` deltaP `5.5015` edge `0.1211` maxDD `-1.4048`
- `market_context_high->fx_1h` score `1.156` n `48` status `ready` deltaP `15.7685` edge `0.0088` maxDD `-0.0736`
- `market_context_high->metal_4h` score `0.8905` n `46` status `ready` deltaP `16.3574` edge `0.0476` maxDD `-0.7323`
- `market_context_high->crypto_major_24h` score `0.7018` n `43` status `ready` deltaP `0.7106` edge `0.1529` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.3395` n `48` status `ready` deltaP `8.0589` edge `0.0155` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
