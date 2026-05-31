# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T10:37:18.442307+00:00`
- Price records: `672`
- Market context records: `2448`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.2887` n `43` status `ready` deltaP `43.6127` edge `1.3755` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.1214` n `43` status `ready` deltaP `54.2716` edge `1.2756` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7283` n `43` status `ready` deltaP `29.7925` edge `1.0602` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.385` n `43` status `ready` deltaP `16.6424` edge `0.7292` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `6.9329` n `43` status `ready` deltaP `23.3002` edge `0.445` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.9794` n `108` status `ready` deltaP `22.3958` edge `0.3818` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.9821` n `125` status `ready` deltaP `23.0659` edge `0.4424` maxDD `-10.1468`
- `news_risk_high->index_24h` score `4.9591` n `43` status `ready` deltaP `8.9309` edge `0.3956` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.7482` n `125` status `ready` deltaP `23.0671` edge `0.5098` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.1823` n `43` status `ready` deltaP `28.6514` edge `0.2841` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.1396` n `43` status `ready` deltaP `32.7156` edge `0.062` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.5161` n `108` status `ready` deltaP `11.6898` edge `0.6339` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.4957` n `125` status `ready` deltaP `12.5915` edge `0.185` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6707` n `43` status `ready` deltaP `15.3822` edge `0.109` maxDD `-2.7857`
- `market_context_high->index_24h` score `1.5668` n `108` status `ready` deltaP `7.6389` edge `0.1152` maxDD `-0.5117`
- `news_risk_high->unknown_1h` score `1.19` n `43` status `ready` deltaP `20.7457` edge `0.0078` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `0.8321` n `136` status `ready` deltaP `9.0833` edge `0.1282` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.726` n `136` status `ready` deltaP `7.7756` edge `0.1274` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5356` n `125` status `ready` deltaP `12.5122` edge `0.0438` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
