# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T16:07:18.671874+00:00`
- Price records: `672`
- Market context records: `2366`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.7609` n `43` status `ready` deltaP `50.0363` edge `1.5387` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.6549` n `43` status `ready` deltaP `46.98` edge `1.202` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9875` n `43` status `ready` deltaP `29.7925` edge `1.0818` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.639` n `43` status `ready` deltaP `19.7674` edge `0.8962` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `8.6051` n `141` status `ready` deltaP `20.2128` edge `0.9716` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.9672` n `43` status `ready` deltaP `27.8141` edge `0.5011` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.0725` n `141` status `ready` deltaP `23.9547` edge `0.3875` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.8938` n `151` status `ready` deltaP `24.5922` edge `0.5082` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.2553` n `151` status `ready` deltaP `19.9413` edge `0.5729` maxDD `-15.4319`
- `news_risk_high->index_24h` score `5.1772` n `43` status `ready` deltaP `13.0976` edge `0.386` maxDD `-1.3507`
- `market_context_high->unknown_4h` score `5.1333` n `151` status `ready` deltaP `21.4707` edge `0.3456` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7677` n `43` status `ready` deltaP `32.0051` edge `0.3368` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4344` n `43` status `ready` deltaP `36.5351` edge `0.0611` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9345` n `43` status `ready` deltaP `24.8404` edge `0.014` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.788` n `151` status `ready` deltaP `19.3618` edge `0.1025` maxDD `-2.2732`
- `market_context_high->index_24h` score `1.7778` n `141` status `ready` deltaP `12.7512` edge `0.1149` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.7648` n `158` status `ready` deltaP `14.7275` edge `0.1683` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `1.5503` n `158` status `ready` deltaP `11.4947` edge `0.1713` maxDD `-6.1656`
- `market_context_high->equity_24h` score `1.2857` n `141` status `ready` deltaP `20.0614` edge `0.1261` maxDD `-6.8828`
- `news_risk_high->unknown_4h` score `0.9266` n `43` status `ready` deltaP `13.4005` edge `0.0602` maxDD `-2.7857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
