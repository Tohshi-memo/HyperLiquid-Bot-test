# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T08:07:31.155670+00:00`
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

- `market_context_high->unknown_24h` score `2329.2455` n `71` status `ready` deltaP `3.4483` edge `194.0808` maxDD `0.0`
- `news_risk_high->equity_24h` score `56.7411` n `50` status `ready` deltaP `62.8276` edge `4.3802` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.3012` n `50` status `ready` deltaP `33.1724` edge `2.2395` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.6163` n `50` status `ready` deltaP `44.7073` edge `1.033` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `13.6808` n `71` status `ready` deltaP `41.3696` edge `1.8052` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.3886` n `71` status `ready` deltaP `21.9961` edge `1.654` maxDD `-13.3222`
- `news_risk_high->crypto_alt_24h` score `8.9447` n `50` status `ready` deltaP `19.5172` edge `1.4672` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.6608` n `50` status `ready` deltaP `54.2069` edge `0.3907` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.1329` n `50` status `ready` deltaP `48.6207` edge `0.3536` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.052` n `50` status `ready` deltaP `44.689` edge `0.1607` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5849` n `50` status `ready` deltaP `22.994` edge `0.2918` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4612` n `50` status `ready` deltaP `26.689` edge `0.3374` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.0558` n `50` status `ready` deltaP `20.9939` edge `0.3356` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0041` n `50` status `ready` deltaP `36.5732` edge `0.1152` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.2293` n `50` status `ready` deltaP `30.2866` edge `0.1022` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2054` n `50` status `ready` deltaP `24.6946` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5371` n `50` status `ready` deltaP `19.5928` edge `0.0276` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7944` n `50` status `ready` deltaP `16.8443` edge `0.0875` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7562` n `50` status `ready` deltaP `18.6946` edge `0.0775` maxDD `-7.0808`
- `news_risk_high->metal_24h` score `0.7115` n `50` status `ready` deltaP `17.3103` edge `0.1931` maxDD `-7.3825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
