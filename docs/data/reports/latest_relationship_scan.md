# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T01:37:24.589643+00:00`
- Price records: `672`
- Market context records: `8149`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `23.3546` n `80` status `ready` deltaP `44.1667` edge `1.7428` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0824` n `81` status `ready` deltaP `37.1199` edge `0.6162` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8942` n `80` status `ready` deltaP `38.3681` edge `0.4854` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.1848` n `43` status `ready` deltaP `31.6648` edge `0.4915` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.9384` n `43` status `ready` deltaP `18.3565` edge `0.3497` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.0367` n `80` status `ready` deltaP `25.2778` edge `0.2349` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.9469` n `81` status `ready` deltaP `35.458` edge `0.0968` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.7907` n `43` status `ready` deltaP `29.3796` edge `0.1509` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.2403` n `81` status `ready` deltaP `17.2636` edge `0.1852` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6303` n `81` status `ready` deltaP `24.4542` edge `0.1184` maxDD `-0.979`
- `news_risk_high->index_4h` score `2.5911` n `43` status `ready` deltaP `21.7916` edge `0.0897` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `2.5488` n `81` status `ready` deltaP `12.0032` edge `0.2441` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.3053` n `81` status `ready` deltaP `13.8776` edge `0.2714` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.1956` n `80` status `ready` deltaP `29.6875` edge `0.0554` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.8304` n `80` status `ready` deltaP `33.0903` edge `0.3026` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6583` n `81` status `ready` deltaP `19.4722` edge `0.028` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.4061` n `43` status `ready` deltaP `13.9747` edge `0.0708` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.3307` n `43` status `ready` deltaP `6.183` edge `0.1094` maxDD `-1.1783`
- `market_context_high->metal_1h` score `0.9945` n `81` status `ready` deltaP `13.1866` edge `0.0328` maxDD `-0.6936`
- `news_risk_high->crypto_alt_4h` score `0.8492` n `43` status `ready` deltaP `10.8834` edge `0.1755` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
