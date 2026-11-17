# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T11:52:30.064248+00:00`
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

- `market_context_high->unknown_24h` score `1847.1975` n `85` status `ready` deltaP `3.4542` edge `153.9101` maxDD `0.0`
- `news_risk_high->equity_24h` score `58.3152` n `50` status `ready` deltaP `65.3748` edge `4.4944` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `17.5875` n `50` status `ready` deltaP `30.7116` edge `2.1644` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `14.5128` n `50` status `ready` deltaP `44.4024` edge `1.0264` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `14.2613` n `85` status `ready` deltaP `44.4763` edge `1.8589` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `13.2721` n `85` status `ready` deltaP `28.3511` edge `1.7249` maxDD `-13.3222`
- `news_risk_high->index_24h` score `9.0122` n `50` status `ready` deltaP `56.7392` edge `0.4031` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `8.7446` n `50` status `ready` deltaP `51.1226` edge `0.3879` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.4564` n `50` status `ready` deltaP `17.057` edge `1.421` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.017` n `50` status `ready` deltaP `44.5366` edge `0.1588` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `4.5741` n `50` status `ready` deltaP `23.1437` edge `0.2899` maxDD `-3.7082`
- `news_risk_high->crypto_alt_4h` score `4.4634` n `50` status `ready` deltaP `26.5366` edge `0.3386` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `3.963` n `50` status `ready` deltaP `20.689` edge `0.3299` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `3.7821` n `50` status `ready` deltaP `34.7439` edge `0.1089` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1698` n `50` status `ready` deltaP `29.6768` edge `0.1013` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1539` n `50` status `ready` deltaP `24.2455` edge `0.0433` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4964` n `50` status `ready` deltaP `19.1437` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8303` n `50` status `ready` deltaP `18.829` edge `0.1982` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7454` n `50` status `ready` deltaP `16.3952` edge `0.0842` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.7032` n `50` status `ready` deltaP `18.3952` edge `0.0727` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
