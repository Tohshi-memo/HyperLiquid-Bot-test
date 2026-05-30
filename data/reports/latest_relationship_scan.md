# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T09:32:10.939341+00:00`
- Price records: `672`
- Market context records: `2335`
- Flow alert records: `8613`
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

- `news_risk_high->crypto_alt_24h` score `20.8453` n `43` status `ready` deltaP `50.0363` edge `1.4624` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.6139` n `43` status `ready` deltaP `43.5077` edge `1.1384` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.3215` n `43` status `ready` deltaP `29.7925` edge `1.0263` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.5962` n `43` status `ready` deltaP `19.7674` edge `0.8093` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.5274` n `132` status `ready` deltaP `18.1818` edge `1.062` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.2921` n `43` status `ready` deltaP `27.6405` edge `0.446` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `7.2068` n `132` status `ready` deltaP `23.9584` edge `0.482` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.6374` n `159` status `ready` deltaP `22.9368` edge `0.6681` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `6.589` n `159` status `ready` deltaP `26.0824` edge `0.5562` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `5.3687` n `159` status `ready` deltaP `21.6981` edge `0.3637` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.4212` n `43` status `ready` deltaP `11.8823` edge `0.3311` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `4.0065` n `43` status `ready` deltaP `33.9868` edge `0.3542` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4186` n `43` status `ready` deltaP `36.1879` edge `0.0621` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.4096` n `132` status `ready` deltaP `15.3883` edge `0.2333` maxDD `-1.4737`
- `news_risk_high->fx_4h` score `2.1086` n `43` status `ready` deltaP `26.8221` edge `0.0153` maxDD `-0.1382`
- `market_context_high->equity_24h` score `2.0659` n `132` status `ready` deltaP `19.2393` edge `0.1966` maxDD `-6.8828`
- `market_context_high->index_4h` score `1.9894` n `159` status `ready` deltaP `19.585` edge `0.1178` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `1.845` n `160` status `ready` deltaP `12.1033` edge `0.1918` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.5849` n `160` status `ready` deltaP `12.1033` edge `0.1708` maxDD `-4.2199`
- `news_risk_high->commodity_24h` score `1.4099` n `43` status `ready` deltaP `4.2878` edge `0.1706` maxDD `-3.202`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
