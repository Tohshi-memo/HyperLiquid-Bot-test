# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T02:37:28.683915+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4392`

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

- `market_context_high->unknown_24h` score `2115.9815` n `58` status `ready` deltaP `3.4483` edge `176.3088` maxDD `0.0`
- `news_risk_high->equity_24h` score `54.8326` n `50` status `ready` deltaP `59.2069` edge `4.2453` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `19.466` n `50` status `ready` deltaP `36.7931` edge `2.3647` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.835` n `58` status `ready` deltaP `13.9655` edge `1.5156` maxDD `-12.7965`
- `news_risk_high->equity_4h` score `14.5368` n `50` status `ready` deltaP `44.4024` edge `1.0284` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.7099` n `58` status `ready` deltaP `39.1379` edge `1.6956` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.3358` n `50` status `ready` deltaP `21.7586` edge `1.5024` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.1677` n `50` status `ready` deltaP `50.4138` edge `0.3749` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.209` n `50` status `ready` deltaP `44.8276` edge `0.3019` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.3175` n `50` status `ready` deltaP `46.8232` edge `0.1686` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.555` n `50` status `ready` deltaP `26.8415` edge `0.3442` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.5441` n `50` status `ready` deltaP `22.6946` edge `0.2904` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.316` n `50` status `ready` deltaP `21.7561` edge `0.3522` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.0997` n `50` status `ready` deltaP `37.1829` edge `0.1191` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.1224` n `50` status `ready` deltaP `29.2195` edge `0.1004` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2761` n `50` status `ready` deltaP `25.4431` edge `0.0455` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5443` n `50` status `ready` deltaP `19.7425` edge `0.0272` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.8402` n `50` status `ready` deltaP `18.3448` edge `0.2027` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8256` n `50` status `ready` deltaP `17.2934` edge `0.0885` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.8092` n `50` status `ready` deltaP `19.1437` edge `0.0813` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
