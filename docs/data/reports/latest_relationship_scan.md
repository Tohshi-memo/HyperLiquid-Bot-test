# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T15:22:28.961295+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3992`

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

- `market_context_high->unknown_24h` score `1566.8612` n `95` status `ready` deltaP `3.4602` edge `130.5487` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.7107` n `50` status `ready` deltaP `67.7578` edge `4.5948` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `16.9673` n `50` status `ready` deltaP `28.4152` edge `2.1002` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.95` n `95` status `ready` deltaP `45.152` edge `1.9427` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.1485` n `95` status `ready` deltaP `30.7612` edge `1.8212` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `13.954` n `50` status `ready` deltaP `42.878` edge `0.99` maxDD `-7.0416`
- `news_risk_high->index_24h` score `9.3252` n `50` status `ready` deltaP `59.1073` edge `0.4134` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.2796` n `50` status `ready` deltaP `53.4602` edge `0.4169` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9915` n `50` status `ready` deltaP `14.7612` edge `1.3767` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8462` n `50` status `ready` deltaP `43.3171` edge `0.1527` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.4745` n `50` status `ready` deltaP `22.6946` edge `0.2846` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `3.9719` n `50` status `ready` deltaP `25.0122` edge `0.3078` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6654` n `50` status `ready` deltaP `33.5244` edge `0.1073` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1541` n `50` status `ready` deltaP `18.7073` edge `0.2757` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.013` n `50` status `ready` deltaP `28.1524` edge `0.0984` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1107` n `50` status `ready` deltaP `23.7964` edge `0.0427` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4832` n `50` status `ready` deltaP `18.994` edge `0.0271` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0219` n `50` status `ready` deltaP `21.045` edge `0.208` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7586` n `50` status `ready` deltaP `16.6946` edge `0.0839` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6253` n `50` status `ready` deltaP `17.7964` edge `0.0667` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
