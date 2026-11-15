# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T20:52:31.363374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8260`

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

- `market_context_high->unknown_24h` score `673.6293` n `55` status `ready` deltaP `3.9861` edge `56.1092` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.1133` n `50` status `ready` deltaP `50.565` edge `3.5763` maxDD `-3.6503`
- `market_context_high->equity_24h` score `41.0342` n `55` status `ready` deltaP `44.3832` edge `3.2778` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.4764` n `55` status `ready` deltaP `62.0576` edge `2.567` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.8519` n `50` status `ready` deltaP `45.175` edge `2.7429` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9146` n `50` status `ready` deltaP `37.6951` edge `0.8546` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.9028` n `55` status `ready` deltaP `16.2659` edge `1.4265` maxDD `-45.4429`
- `news_risk_high->crypto_alt_24h` score `9.4824` n `50` status `ready` deltaP `20.6031` edge `1.5289` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1388` n `55` status `ready` deltaP `48.7916` edge `0.3616` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6515` n `50` status `ready` deltaP `42.2461` edge `0.303` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.4986` n `55` status `ready` deltaP `62.5808` edge `0.5051` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.4285` n `50` status `ready` deltaP `41.9411` edge `0.2561` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.853` n `50` status `ready` deltaP `43.9268` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.8512` n `50` status `ready` deltaP `21.7561` edge `0.3968` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.2832` n `50` status `ready` deltaP `26.3841` edge `0.3246` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9348` n `50` status `ready` deltaP `21.0479` edge `0.2506` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6746` n `50` status `ready` deltaP `34.1341` edge `0.104` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4602` n `50` status `ready` deltaP `23.7317` edge `0.0818` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1454` n `50` status `ready` deltaP `24.5449` edge `0.0406` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2651` n `50` status `ready` deltaP `16.8982` edge `0.0229` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
