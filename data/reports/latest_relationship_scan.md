# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T12:22:17.595372+00:00`
- Price records: `672`
- Market context records: `1736`
- Flow alert records: `6900`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.9478` n `152` status `ready` deltaP `25.7377` edge `0.65` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7759` n `196` status `ready` deltaP `20.3615` edge `0.5222` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.9713` n `152` status `ready` deltaP `16.2022` edge `0.8383` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.271` n `152` status `ready` deltaP `18.2181` edge `0.3573` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.2048` n `196` status `ready` deltaP `21.805` edge `0.4456` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0723` n `196` status `ready` deltaP `13.6417` edge `0.3922` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9693` n `196` status `ready` deltaP `15.9594` edge `0.2505` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.4612` n `152` status `ready` deltaP `16.6264` edge `0.5841` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7453` n `196` status `ready` deltaP `7.4209` edge `0.115` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6393` n `196` status `ready` deltaP `9.7313` edge `0.0973` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.2763` n `152` status `ready` deltaP `21.8154` edge `1.0585` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.2076` n `196` status `ready` deltaP `4.8974` edge `0.092` maxDD `-3.9211`
- `market_context_high->crypto_major_24h` score `0.1413` n `152` status `ready` deltaP `20.5737` edge `0.7332` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.0466` n `196` status `ready` deltaP `4.9707` edge `0.0516` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3449` n `196` status `ready` deltaP `2.4197` edge `0.0183` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3479` n `196` status `ready` deltaP `11.6818` edge `0.1467` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5448` n `196` status `ready` deltaP `5.6459` edge `0.0261` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.649` n `196` status `ready` deltaP `-2.8168` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7162` n `152` status `ready` deltaP `5.8389` edge `0.0063` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.548` n `196` status `ready` deltaP `1.0876` edge `0.0107` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
