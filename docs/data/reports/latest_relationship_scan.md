# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T09:22:25.223835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4096`

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

- `market_context_high->unknown_24h` score `2136.1643` n `76` status `ready` deltaP `3.4483` edge `177.9907` maxDD `0.0`
- `news_risk_high->equity_24h` score `57.2852` n `50` status `ready` deltaP `63.6897` edge `4.4198` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.0115` n `50` status `ready` deltaP `32.3103` edge `2.2081` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6655` n `50` status `ready` deltaP `44.7073` edge `1.0371` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.0161` n `76` status `ready` deltaP `42.7314` edge `1.8391` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.81` n `76` status `ready` deltaP `24.6552` edge `1.6903` maxDD `-13.3222`
- `news_risk_high->index_24h` score `8.7849` n `50` status `ready` deltaP `55.069` edge `0.3953` maxDD `-0.4279`
- `news_risk_high->crypto_alt_24h` score `8.7478` n `50` status `ready` deltaP `18.6552` edge `1.4477` maxDD `-29.0448`
- `news_risk_high->commodity_24h` score `8.335` n `50` status `ready` deltaP `49.4828` edge `0.3647` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.04` n `50` status `ready` deltaP `44.689` edge `0.1597` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.6724` n `50` status `ready` deltaP `23.4431` edge `0.2961` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4588` n `50` status `ready` deltaP `26.689` edge `0.3372` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0318` n `50` status `ready` deltaP `20.9939` edge `0.3336` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.9301` n `50` status `ready` deltaP `35.9634` edge `0.1131` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2183` n `50` status `ready` deltaP `30.1341` edge `0.1023` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2186` n `50` status `ready` deltaP `24.8443` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5658` n `50` status `ready` deltaP `19.8922` edge `0.028` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8186` n `50` status `ready` deltaP `16.994` edge `0.0896` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.789` n `50` status `ready` deltaP `18.994` edge `0.0797` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7349` n `50` status `ready` deltaP `17.6552` edge `0.1938` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
