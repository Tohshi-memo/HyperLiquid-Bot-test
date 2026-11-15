# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T18:52:26.339050+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8274`

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

- `market_context_high->unknown_24h` score `549.5133` n `63` status `ready` deltaP `3.9861` edge `45.7662` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.6645` n `50` status `ready` deltaP `50.565` edge `3.5389` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.8661` n `63` status `ready` deltaP `46.692` edge `3.2484` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `33.9099` n `63` status `ready` deltaP `63.2115` edge `2.5121` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.2374` n `50` status `ready` deltaP `46.2149` edge `2.7854` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.2365` n `50` status `ready` deltaP `38.9146` edge `0.8733` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.437` n `50` status `ready` deltaP `19.9099` edge `1.5277` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1726` n `63` status `ready` deltaP `49.4842` edge `0.3598` maxDD `-0.0251`
- `market_context_high->metal_24h` score `6.744` n `63` status `ready` deltaP `63.8497` edge `0.5281` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.5939` n `50` status `ready` deltaP `42.2461` edge `0.2982` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.5838` n `50` status `ready` deltaP `43.3276` edge `0.2598` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.3807` n `50` status `ready` deltaP `22.9756` edge `0.4328` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.1356` n `63` status `ready` deltaP `13.6117` edge `1.2371` maxDD `-66.6572`
- `news_risk_high->metal_4h` score `4.932` n `50` status `ready` deltaP `44.689` edge `0.1507` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.7288` n `50` status `ready` deltaP `27.6037` edge `0.3536` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0355` n `50` status `ready` deltaP `21.6467` edge `0.255` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6772` n `50` status `ready` deltaP `34.2866` edge `0.1032` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5817` n `50` status `ready` deltaP `24.9512` edge `0.0838` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1849` n `50` status `ready` deltaP `24.994` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.307` n `50` status `ready` deltaP `17.3473` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
