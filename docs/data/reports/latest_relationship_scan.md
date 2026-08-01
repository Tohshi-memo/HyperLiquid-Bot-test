# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T21:06:52.369560+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5932`

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

- `news_risk_high->unknown_24h` score `5188.8999` n `60` status `ready` deltaP `31.9815` edge `432.2372` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.6169` n `53` status `ready` deltaP `57.2708` edge `1.126` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `4.8341` n `68` status `ready` deltaP `16.831` edge `0.367` maxDD `-3.4427`
- `market_context_high->commodity_24h` score `1.7833` n `53` status `ready` deltaP `27.6577` edge `0.2301` maxDD `-10.2019`
- `news_risk_high->index_4h` score `1.7148` n `68` status `ready` deltaP `16.3737` edge `0.0718` maxDD `-0.3783`
- `market_context_high->crypto_alt_4h` score `0.7395` n `53` status `ready` deltaP `9.3477` edge `0.1282` maxDD `-5.323`
- `news_risk_high->equity_1h` score `0.6996` n `68` status `ready` deltaP `9.6425` edge `0.0763` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.247` n `53` status `ready` deltaP `14.3207` edge `0.0158` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.1392` n `68` status `ready` deltaP `5.3174` edge `0.03` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `0.1225` n `68` status `ready` deltaP `6.4812` edge `0.0407` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0091` n `53` status `ready` deltaP `7.502` edge `0.001` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `0.0021` n `68` status `ready` deltaP `11.0743` edge `0.0221` maxDD `-0.6604`
- `news_risk_high->index_1h` score `-0.0435` n `68` status `ready` deltaP `2.7651` edge `0.0083` maxDD `-0.5845`
- `market_context_high->fx_24h` score `-0.0755` n `53` status `ready` deltaP `6.8866` edge `0.0424` maxDD `-2.506`
- `market_context_high->commodity_1h` score `-0.0878` n `53` status `ready` deltaP `4.0278` edge `0.016` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `-0.0957` n `68` status `ready` deltaP `2.3688` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1341` n `68` status `ready` deltaP `2.4657` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->crypto_major_1h` score `-0.1937` n `68` status `ready` deltaP `2.0694` edge `0.0334` maxDD `-3.762`
- `market_context_high->commodity_4h` score `-0.3007` n `53` status `ready` deltaP `2.9625` edge `0.0292` maxDD `-3.0005`
- `market_context_high->crypto_alt_1h` score `-0.5887` n `53` status `ready` deltaP `-4.1182` edge `0.0147` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
