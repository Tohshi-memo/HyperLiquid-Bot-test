# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T06:37:33.089837+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4404`

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

- `market_context_high->unknown_24h` score `2367.8999` n `65` status `ready` deltaP `3.4483` edge `197.302` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.1639` n `50` status `ready` deltaP `61.7931` edge `4.339` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.6296` n `50` status `ready` deltaP `34.2069` edge `2.2747` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9573` n `65` status `ready` deltaP `18.0902` edge `1.5882` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.48` n `50` status `ready` deltaP `44.0976` edge `1.0257` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.1231` n `65` status `ready` deltaP `39.2838` edge `1.7476` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.1264` n `50` status `ready` deltaP `20.5517` edge `1.4836` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.5216` n `50` status `ready` deltaP `53.1724` edge `0.386` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.8833` n `50` status `ready` deltaP `47.5862` edge `0.3397` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0882` n `50` status `ready` deltaP `44.8415` edge `0.1627` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6436` n `50` status `ready` deltaP `23.4431` edge `0.2937` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.5036` n `50` status `ready` deltaP `26.9939` edge `0.3389` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.1716` n `50` status `ready` deltaP `21.4512` edge `0.3422` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1057` n `50` status `ready` deltaP `37.1829` edge `0.1196` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2233` n `50` status `ready` deltaP `30.2866` edge `0.1017` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2198` n `50` status `ready` deltaP `24.8443` edge `0.0448` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5862` n `50` status `ready` deltaP `20.1916` edge `0.0277` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8054` n `50` status `ready` deltaP `16.994` edge `0.0879` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7742` n `50` status `ready` deltaP `18.8443` edge `0.0788` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7396` n `50` status `ready` deltaP `17.6552` edge `0.1944` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
