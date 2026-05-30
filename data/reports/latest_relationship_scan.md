# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T17:37:15.807398+00:00`
- Price records: `672`
- Market context records: `2373`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `news_risk_high->crypto_alt_24h` score `21.9212` n `43` status `ready` deltaP `50.2099` edge `1.5509` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.8606` n `43` status `ready` deltaP `48.0216` edge `1.2122` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1711` n `43` status `ready` deltaP `29.7925` edge `1.0971` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.8766` n `43` status `ready` deltaP `19.7674` edge `0.916` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.0716` n `43` status `ready` deltaP `27.8141` edge `0.5098` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.7231` n `137` status `ready` deltaP `19.3431` edge `0.9039` maxDD `-25.1408`
- `market_context_high->unknown_24h` score `5.7046` n `137` status `ready` deltaP `23.7062` edge `0.3585` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `5.6649` n `148` status `ready` deltaP `24.1761` edge `0.4919` maxDD `-10.1468`
- `news_risk_high->index_24h` score `5.2998` n `43` status `ready` deltaP `13.4448` edge `0.3939` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.822` n `148` status `ready` deltaP `19.3103` edge `0.541` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `4.7729` n `148` status `ready` deltaP `20.3568` edge `0.323` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7537` n `43` status `ready` deltaP `32.0051` edge `0.335` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4591` n `43` status `ready` deltaP `36.7087` edge `0.062` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `1.9723` n `43` status `ready` deltaP `25.2977` edge `0.0141` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.6917` n `148` status `ready` deltaP `18.3834` edge `0.101` maxDD `-2.2732`
- `market_context_high->index_24h` score `1.6263` n `137` status `ready` deltaP `12.4772` edge `0.1041` maxDD `-1.4737`
- `market_context_high->crypto_major_1h` score `1.5396` n `155` status `ready` deltaP `13.6073` edge `0.157` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `1.2966` n `155` status `ready` deltaP `10.4385` edge `0.1572` maxDD `-6.1656`
- `news_risk_high->unknown_4h` score `1.054` n `43` status `ready` deltaP `13.5529` edge `0.0698` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `0.9227` n `43` status `ready` deltaP `19.099` edge `-0.0035` maxDD `-1.7548`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
