# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T14:37:48.155442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3908`

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

- `market_context_high->unknown_24h` score `1641.2576` n `92` status `ready` deltaP `3.4602` edge `136.7484` maxDD `0.0`
- `news_risk_high->equity_24h` score `59.338` n `50` status `ready` deltaP `67.2388` edge `4.5672` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.0809` n `50` status `ready` deltaP `28.9343` edge `2.1113` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `14.8336` n `92` status `ready` deltaP `44.8473` edge `1.9298` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `14.0298` n `50` status `ready` deltaP `43.0305` edge `0.9953` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `13.9821` n `92` status `ready` deltaP `29.976` edge `1.8051` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.2501` n `50` status `ready` deltaP `58.5882` edge `0.4106` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `9.1637` n `50` status `ready` deltaP `52.9412` edge `0.4107` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0707` n `50` status `ready` deltaP `15.2803` edge `1.3834` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `4.8776` n `50` status `ready` deltaP `43.4695` edge `0.1543` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.429` n `50` status `ready` deltaP `22.5449` edge `0.2818` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.1368` n `50` status `ready` deltaP `25.4695` edge `0.3185` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.645` n `50` status `ready` deltaP `33.5244` edge `0.1056` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.361` n `50` status `ready` deltaP `19.1646` edge `0.2899` maxDD `-9.0062`
- `news_risk_high->index_4h` score `3.0312` n `50` status `ready` deltaP `28.3049` edge `0.0989` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1419` n `50` status `ready` deltaP `24.0958` edge `0.0433` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4688` n `50` status `ready` deltaP `18.8443` edge `0.0269` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9899` n `50` status `ready` deltaP `20.699` edge `0.2062` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7282` n `50` status `ready` deltaP `16.3952` edge `0.082` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6276` n `50` status `ready` deltaP `17.7964` edge `0.067` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
