# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T10:37:28.654627+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_24h` score `531.7612` n `66` status `ready` deltaP `2.5997` edge `44.2961` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.381` n `50` status `ready` deltaP `48.8319` edge `3.4435` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1499` n `66` status `ready` deltaP `42.6501` edge `3.049` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.0384` n `66` status `ready` deltaP `57.8121` edge `2.3088` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.7496` n `50` status `ready` deltaP `46.3882` edge `2.8499` maxDD `-6.8139`
- `market_context_high->unknown_4h` score `16.7393` n `79` status `ready` deltaP `8.8415` edge `1.336` maxDD `0.0`
- `news_risk_high->equity_4h` score `12.3407` n `50` status `ready` deltaP `39.6768` edge `0.8769` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.2831` n `50` status `ready` deltaP `16.9636` edge `1.3994` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5232` n `66` status `ready` deltaP `44.9372` edge `0.3365` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.192` n `50` status `ready` deltaP `47.6603` edge `0.2816` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3269` n `50` status `ready` deltaP `40.513` edge `0.2875` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.2314` n `66` status `ready` deltaP `58.852` edge `0.4957` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5857` n `50` status `ready` deltaP `23.7378` edge `0.4448` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0401` n `50` status `ready` deltaP `45.7561` edge `0.1526` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.9329` n `50` status `ready` deltaP `28.6707` edge `0.3635` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0271` n `50` status `ready` deltaP `21.7964` edge `0.2533` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5466` n `50` status `ready` deltaP `32.6098` edge `0.1035` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0689` n `66` status `ready` deltaP `12.6306` edge `1.2041` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.79` n `50` status `ready` deltaP `27.3902` edge `0.0849` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `26.0419` edge `0.0413` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
