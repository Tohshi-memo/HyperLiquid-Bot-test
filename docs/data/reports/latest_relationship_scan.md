# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T05:22:26.922556+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4434`

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

- `market_context_high->unknown_24h` score `2127.2327` n `60` status `ready` deltaP `3.4483` edge `177.2464` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.6797` n `50` status `ready` deltaP `60.931` edge `4.3044` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.8975` n `50` status `ready` deltaP `35.069` edge `2.3033` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.7233` n `60` status `ready` deltaP `13.7357` edge `1.5144` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.3544` n `50` status `ready` deltaP `43.4878` edge `1.0193` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.3387` n `60` status `ready` deltaP `37.069` edge `1.6618` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2141` n `50` status `ready` deltaP `21.069` edge `1.4914` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.401` n `50` status `ready` deltaP `52.3103` edge `0.3817` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.6571` n `50` status `ready` deltaP `46.7241` edge `0.3266` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.1659` n `50` status `ready` deltaP `45.6037` edge `0.1641` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5252` n `50` status `ready` deltaP `26.9939` edge `0.3407` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5069` n `50` status `ready` deltaP `22.6946` edge `0.2873` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.2405` n `50` status `ready` deltaP `21.9085` edge `0.3449` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1445` n `50` status `ready` deltaP `37.4878` edge `0.1208` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.148` n `50` status `ready` deltaP `29.5244` edge `0.1005` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.179` n `50` status `ready` deltaP `24.3952` edge `0.0444` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5179` n `50` status `ready` deltaP `19.4431` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7934` n `50` status `ready` deltaP `18.3448` edge `0.1967` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7407` n `50` status `ready` deltaP `16.3952` edge `0.0836` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7009` n `50` status `ready` deltaP `18.2455` edge `0.0734` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
