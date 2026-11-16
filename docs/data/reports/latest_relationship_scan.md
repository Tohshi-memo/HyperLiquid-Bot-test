# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T03:37:26.113561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8902`

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

- `news_risk_high->equity_24h` score `47.9159` n `50` status `ready` deltaP `50.6736` edge `3.7258` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `39.9309` n `64` status `ready` deltaP `6.1738` edge `3.295` maxDD `-0.02`
- `news_risk_high->crypto_major_24h` score `21.3111` n `50` status `ready` deltaP `41.8542` edge `2.5675` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9082` n `50` status `ready` deltaP `37.3902` edge `0.8561` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.0848` n `50` status `ready` deltaP `20.5625` edge `1.4782` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.8858` n `50` status `ready` deltaP `42.3403` edge `0.3219` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.2394` n `50` status `ready` deltaP `40.9722` edge `0.2468` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.994` n `50` status `ready` deltaP `44.3841` edge `0.1579` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.34` n `50` status `ready` deltaP `20.8415` edge `0.3603` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.1276` n `50` status `ready` deltaP `25.7744` edge `0.3157` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9217` n `50` status `ready` deltaP `20.2994` edge `0.2545` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.8971` n `50` status `ready` deltaP `35.5061` edge `0.1134` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4612` n `50` status `ready` deltaP `23.5793` edge `0.0829` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2569` n `50` status `ready` deltaP `25.4431` edge `0.0439` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2759` n `50` status `ready` deltaP `16.8982` edge `0.0238` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.9987` n `50` status `ready` deltaP `18.9028` edge `0.2193` maxDD `-7.3825`
- `news_risk_high->crypto_major_1h` score `0.8466` n `50` status `ready` deltaP `19.7425` edge `0.0821` maxDD `-7.0808`
- `news_risk_high->crypto_alt_1h` score `0.8091` n `50` status `ready` deltaP `18.0419` edge `0.0814` maxDD `-6.1688`
- `news_risk_high->commodity_1h` score `0.3809` n `50` status `ready` deltaP `4.2455` edge `0.0369` maxDD `-0.3438`
- `market_context_high->metal_1h` score `-0.9679` n `76` status `ready` deltaP `-5.7674` edge `-0.0098` maxDD `-2.067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
