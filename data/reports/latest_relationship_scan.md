# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T01:52:27.477761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2633.9772` n `139` status `ready` deltaP `1.2153` edge `219.49` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.06` n `139` status `ready` deltaP `29.4627` edge `1.2871` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.3064` n `139` status `ready` deltaP `29.0605` edge `0.7541` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `7.5367` n `139` status `ready` deltaP `24.7202` edge `0.9067` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.7596` n `139` status `ready` deltaP `34.5186` edge `0.1527` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.2387` n `139` status `ready` deltaP `27.0721` edge `0.2749` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.5443` n `139` status `ready` deltaP `27.1736` edge `0.1918` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9575` n `139` status `ready` deltaP `8.4982` edge `0.2891` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7718` n `139` status `ready` deltaP `7.4667` edge `0.1056` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6291` n `139` status `ready` deltaP `8.1528` edge `0.0642` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4875` n `139` status `ready` deltaP `9.051` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1197` n `139` status `ready` deltaP `7.2678` edge `0.0269` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4944` n `139` status `ready` deltaP `1.6402` edge `0.0108` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5544` n `139` status `ready` deltaP `0.5966` edge `0.0532` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3581` n `139` status `ready` deltaP `8.0003` edge `-0.0061` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4422` n `139` status `ready` deltaP `-9.3086` edge `0.0266` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9024` n `139` status `ready` deltaP `-5.7006` edge `0.0656` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0131` n `139` status `ready` deltaP `-11.5668` edge `-0.0135` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7302` n `139` status `ready` deltaP `-10.4075` edge `0.0004` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
