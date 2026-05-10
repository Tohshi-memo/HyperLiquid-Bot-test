# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T06:07:14.778868+00:00`
- Price records: `672`
- Market context records: `947`
- Flow alert records: `2651`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `1320`

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

- `risk_on_high->crypto_major_24h` score `22.4384` n `31` status `ready` deltaP `34.375` edge `1.6407` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `22.4384` n `31` status `ready` deltaP `34.375` edge `1.6407` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.7484` n `168` status `ready` deltaP `31.3988` edge `1.0531` maxDD `-1.3382`
- `risk_on_high->crypto_alt_24h` score `14.1423` n `31` status `ready` deltaP `7.6389` edge `1.1276` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `14.1423` n `31` status `ready` deltaP `7.6389` edge `1.1276` maxDD `0.0`
- `risk_on_high->equity_24h` score `13.2008` n `31` status `ready` deltaP `25.0` edge `0.9334` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `13.2008` n `31` status `ready` deltaP `25.0` edge `0.9334` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `7.9335` n `168` status `ready` deltaP `7.6389` edge `0.6102` maxDD `0.0`
- `risk_on_high->index_24h` score `4.1441` n `31` status `ready` deltaP `26.7361` edge `0.1671` maxDD `0.0`
- `risk_on_and_context->index_24h` score `4.1441` n `31` status `ready` deltaP `26.7361` edge `0.1671` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4228` n `31` status `ready` deltaP `5.9501` edge `0.2761` maxDD `-0.7761`
- `risk_on_and_context->equity_4h` score `3.4228` n `31` status `ready` deltaP `5.9501` edge `0.2761` maxDD `-0.7761`
- `risk_on_high->crypto_alt_4h` score `3.3709` n `31` status `ready` deltaP `24.0116` edge `0.1413` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `3.3709` n `31` status `ready` deltaP `24.0116` edge `0.1413` maxDD `-0.6377`
- `risk_on_high->crypto_major_4h` score `2.801` n `31` status `ready` deltaP `20.6874` edge `0.1327` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.801` n `31` status `ready` deltaP `20.6874` edge `0.1327` maxDD `-0.9758`
- `risk_on_high->index_4h` score `2.174` n `31` status `ready` deltaP `9.1759` edge `0.1288` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.174` n `31` status `ready` deltaP `9.1759` edge `0.1288` maxDD `-0.038`
- `risk_on_high->commodity_24h` score `1.0176` n `31` status `ready` deltaP `-12.1584` edge `0.2861` maxDD `-1.9668`
- `risk_on_and_context->commodity_24h` score `1.0176` n `31` status `ready` deltaP `-12.1584` edge `0.2861` maxDD `-1.9668`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
