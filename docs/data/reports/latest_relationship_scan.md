# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T16:07:35.128560+00:00`
- Price records: `672`
- Market context records: `2156`
- Flow alert records: `8104`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `market_context_high->crypto_alt_4h` score `13.6985` n `145` status `ready` deltaP `37.7964` edge `0.9832` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.988` n `145` status `ready` deltaP `41.7893` edge `0.7734` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.203` n `145` status `ready` deltaP `24.6204` edge `0.4277` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.5621` n `145` status `ready` deltaP `25.6087` edge `0.3189` maxDD `-5.0894`
- `news_risk_high->commodity_4h` score `4.0945` n `39` status `ready` deltaP `31.164` edge `0.3843` maxDD `-3.0367`
- `market_context_high->index_24h` score `3.4719` n `145` status `ready` deltaP `13.5548` edge `0.3218` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `3.4441` n `145` status `ready` deltaP `18.0033` edge `0.2147` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.2936` n `145` status `ready` deltaP `16.656` edge `0.2498` maxDD `-4.9097`
- `market_context_high->index_4h` score `3.2602` n `145` status `ready` deltaP `23.9318` edge `0.1805` maxDD `-1.8022`
- `market_context_high->unknown_24h` score `2.818` n `145` status `ready` deltaP `27.4006` edge `0.5842` maxDD `-35.8966`
- `market_context_high->metal_4h` score `2.7444` n `145` status `ready` deltaP `20.4825` edge `0.2309` maxDD `-4.7664`
- `market_context_high->equity_24h` score `2.698` n `145` status `ready` deltaP `25.346` edge `0.5457` maxDD `-33.1875`
- `news_risk_high->fx_4h` score `2.5282` n `39` status `ready` deltaP `31.6917` edge `0.0178` maxDD `-0.1382`
- `market_context_high->crypto_major_24h` score `2.1818` n `145` status `ready` deltaP `20.4454` edge `1.002` maxDD `-62.3533`
- `news_risk_high->unknown_4h` score `1.4545` n `39` status `ready` deltaP `14.4348` edge `0.0973` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.0459` n `43` status `ready` deltaP `19.0189` edge `0.0073` maxDD `-1.7548`
- `news_risk_high->commodity_1h` score `0.7869` n `43` status `ready` deltaP `10.4651` edge `0.0991` maxDD `-2.1052`
- `market_context_high->equity_1h` score `0.6996` n `145` status `ready` deltaP `9.711` edge `0.0724` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.6596` n `145` status `ready` deltaP `9.7594` edge `0.0569` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
