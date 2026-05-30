# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T09:22:18.863525+00:00`
- Price records: `672`
- Market context records: `2334`
- Flow alert records: `8611`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `20.8273` n `43` status `ready` deltaP `50.0363` edge `1.4609` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.5748` n `43` status `ready` deltaP `43.3341` edge `1.1363` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.2963` n `43` status `ready` deltaP `29.7925` edge `1.0242` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.571` n `43` status `ready` deltaP `19.7674` edge `0.8072` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.4384` n `131` status `ready` deltaP `17.9389` edge `1.0562` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.2357` n `43` status `ready` deltaP `27.6405` edge `0.4413` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.2077` n `131` status `ready` deltaP `23.8948` edge `0.4825` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.6626` n `159` status `ready` deltaP `22.9368` edge `0.6702` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.6204` n `159` status `ready` deltaP `26.2348` edge `0.5578` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.3651` n `159` status `ready` deltaP `21.6981` edge `0.3634` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.396` n `43` status `ready` deltaP `11.8823` edge `0.329` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0057` n `43` status `ready` deltaP `33.9868` edge `0.3541` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.421` n `43` status `ready` deltaP `36.1879` edge `0.0623` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4182` n `131` status `ready` deltaP `15.2552` edge `0.2349` maxDD `-1.4737`
- `news_risk_high->fx_4h` score `2.1208` n `43` status `ready` deltaP `26.9746` edge `0.0153` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0305` n `131` status `ready` deltaP `19.141` edge `0.1943` maxDD `-6.8828`
- `market_context_high->index_4h` score `2.004` n `159` status `ready` deltaP `19.7375` edge `0.118` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.852` n `159` status `ready` deltaP `12.025` edge `0.1929` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5882` n `159` status `ready` deltaP `12.025` edge `0.1716` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.4687` n `43` status `ready` deltaP `4.2878` edge `0.1755` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
