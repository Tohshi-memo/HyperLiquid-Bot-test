# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T23:07:25.700441+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4790`

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

- `market_context_high->unknown_1h` score `364.0306` n `50` status `ready` deltaP `10.5749` edge `30.2703` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.8899` n `50` status `ready` deltaP `10.8232` edge `24.252` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.1709` n `70` status `ready` deltaP `42.9762` edge `1.1653` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.5994` n `50` status `ready` deltaP `19.8333` edge `0.9214` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.057` n `50` status `ready` deltaP `31.8264` edge `0.6842` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.9846` n `70` status `ready` deltaP `33.7351` edge `0.5723` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.8951` n `50` status `ready` deltaP `19.5244` edge `0.5981` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `6.5914` n `113` status `ready` deltaP `25.5895` edge `0.5131` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.3897` n `50` status `ready` deltaP `17.7134` edge `0.5433` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.3777` n `50` status `ready` deltaP `15.4012` edge `0.2451` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1176` n `50` status `ready` deltaP `14.1497` edge `0.2105` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7653` n `50` status `ready` deltaP `30.8598` edge `0.0382` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.7321` n `113` status `ready` deltaP `23.0911` edge `0.135` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.4868` n `70` status `ready` deltaP `8.3978` edge `0.5301` maxDD `-13.0476`
- `news_risk_high->crypto_major_4h` score `2.0929` n `113` status `ready` deltaP `17.8961` edge `0.3563` maxDD `-9.5829`
- `news_risk_high->metal_24h` score `1.4971` n `70` status `ready` deltaP `14.6528` edge `0.2208` maxDD `-2.1236`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.3232` n `50` status `ready` deltaP `6.0208` edge `0.3157` maxDD `-11.8957`
- `news_risk_high->crypto_alt_1h` score `1.1363` n `113` status `ready` deltaP `5.1534` edge `0.1164` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9926` n `50` status `ready` deltaP `20.3333` edge `0.0935` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
