# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T18:22:48.605086+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4250`

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

- `news_risk_high->equity_24h` score `53.4962` n `50` status `ready` deltaP `59.1073` edge `4.1346` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `20.9335` n `50` status `ready` deltaP `40.3529` edge `2.5291` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `18.1992` n `30` status `ready` deltaP `13.6101` edge `1.5803` maxDD `-8.6878`
- `news_risk_high->equity_4h` score `14.2922` n `50` status `ready` deltaP `43.6402` edge `1.0131` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.069` n `30` status `ready` deltaP `42.3529` edge `1.592` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `10.0541` n `50` status `ready` deltaP `24.2768` edge `1.5777` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.0175` n `50` status `ready` deltaP `50.1107` edge `0.3644` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.1825` n `50` status `ready` deltaP `41.1765` edge `0.2407` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2437` n `50` status `ready` deltaP `46.3659` edge `0.1655` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9183` n `50` status `ready` deltaP `28.5183` edge `0.3633` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.5387` n `50` status `ready` deltaP `22.3659` edge `0.3667` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `4.483` n `50` status `ready` deltaP `22.0958` edge `0.2893` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `4.0223` n `50` status `ready` deltaP `36.7256` edge `0.1157` maxDD `-0.3611`
- `market_context_high->metal_24h` score `3.7947` n `30` status `ready` deltaP `46.9435` edge `0.2627` maxDD `-3.7989`
- `news_risk_high->index_4h` score `3.0348` n `50` status `ready` deltaP `28.3049` edge `0.0992` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2784` n `50` status `ready` deltaP `25.5928` edge `0.0447` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.47` n `50` status `ready` deltaP `18.8443` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9162` n `50` status `ready` deltaP `18.2768` edge `0.2129` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.9058` n `50` status `ready` deltaP `18.1916` edge `0.0928` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8342` n `50` status `ready` deltaP `19.4431` edge `0.0825` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
