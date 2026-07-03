# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T20:52:26.464272+00:00`
- Price records: `672`
- Market context records: `5594`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11433`

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

- `market_context_high->equity_24h` score `3.7147` n `174` status `ready` deltaP `15.0084` edge `0.7174` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.2973` n `208` status `ready` deltaP `12.113` edge `0.2566` maxDD `-14.0065`
- `market_context_high->fx_24h` score `1.1014` n `174` status `ready` deltaP `20.0491` edge `0.0555` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.6095` n `208` status `ready` deltaP `6.9536` edge `0.1683` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.6022` n `208` status `ready` deltaP `7.1646` edge `0.1665` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2943` n `220` status `ready` deltaP `1.2248` edge `0.0012` maxDD `-0.4341`
- `market_context_high->crypto_major_24h` score `-0.3123` n `174` status `ready` deltaP `11.7158` edge `0.3499` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.3775` n `220` status `ready` deltaP `5.2259` edge `0.0344` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.428` n `220` status `ready` deltaP `1.7012` edge `0.0065` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.5573` n `220` status `ready` deltaP `4.2461` edge `0.0498` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.5577` n `220` status `ready` deltaP `1.2575` edge `0.0413` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.6033` n `220` status `ready` deltaP `-1.5188` edge `0.0003` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-1.0669` n `208` status `ready` deltaP `3.424` edge `0.0086` maxDD `-0.9601`
- `market_context_high->commodity_1h` score `-1.2` n `220` status `ready` deltaP `-2.4224` edge `-0.0073` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.5081` n `208` status `ready` deltaP `3.1426` edge `0.0143` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.2666` n `174` status `ready` deltaP `11.1291` edge `0.0339` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9272` n `208` status `ready` deltaP `-11.9137` edge `-0.0575` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1482` n `208` status `ready` deltaP `-5.0891` edge `-0.0442` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0415` n `174` status `ready` deltaP `-8.501` edge `-0.2382` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-10.4027` n `174` status `ready` deltaP `1.5026` edge `-0.0072` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
