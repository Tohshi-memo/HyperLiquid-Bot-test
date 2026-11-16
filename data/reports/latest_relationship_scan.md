# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T14:23:37.298615+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4064`

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

- `market_context_high->unknown_24h` score `78.5199` n `30` status `ready` deltaP `3.9792` edge `6.5168` maxDD `0.0`
- `news_risk_high->equity_24h` score `52.5274` n `50` status `ready` deltaP `57.3772` edge `4.0654` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.5941` n `50` status `ready` deltaP `42.6021` edge `2.5988` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.742` n `30` status `ready` deltaP `15.3402` edge `1.614` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `13.4392` n `50` status `ready` deltaP `41.6474` edge `0.9553` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7296` n `30` status `ready` deltaP `44.6021` edge `1.6617` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.4069` n `50` status `ready` deltaP `26.0069` edge `1.6114` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.7927` n `50` status `ready` deltaP `48.3806` edge `0.3572` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0901` n `50` status `ready` deltaP `41.1765` edge `0.233` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `5.2191` n `50` status `ready` deltaP `29.3982` edge `0.3825` maxDD `-9.4848`
- `news_risk_high->metal_4h` score `5.101` n `50` status `ready` deltaP `45.4225` edge `0.1599` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.8022` n `50` status `ready` deltaP `23.0942` edge `0.3838` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.105` n `50` status `ready` deltaP `21.2706` edge `0.2633` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.8572` n `30` status `ready` deltaP `47.2895` edge `0.2684` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.8145` n `50` status `ready` deltaP `35.3435` edge `0.1076` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.8144` n `50` status `ready` deltaP `26.4802` edge `0.093` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2469` n `50` status `ready` deltaP `25.3632` edge `0.0436` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3356` n `50` status `ready` deltaP `17.5695` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9787` n `50` status `ready` deltaP `18.6228` edge `0.2186` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9343` n `50` status `ready` deltaP `18.559` edge `0.094` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
