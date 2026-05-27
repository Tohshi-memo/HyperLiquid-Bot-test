# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T03:07:20.093797+00:00`
- Price records: `672`
- Market context records: `2002`
- Flow alert records: `7655`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7593`

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

- `market_context_high->crypto_major_4h` score `8.7311` n `217` status `ready` deltaP `30.5525` edge `0.5769` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.132` n `217` status `ready` deltaP `24.0798` edge `0.6316` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.3874` n `217` status `ready` deltaP `18.0995` edge `0.4032` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.6218` n `217` status `ready` deltaP `15.5607` edge `0.2242` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.0251` n `185` status `ready` deltaP `15.6599` edge `0.5964` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.442` n `185` status `ready` deltaP `16.3754` edge `0.2536` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `1.3825` n `217` status `ready` deltaP `11.6132` edge `0.1364` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `1.138` n `217` status `ready` deltaP `9.6905` edge `0.1416` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.988` n `185` status `ready` deltaP `14.4715` edge `0.4757` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9631` n `217` status `ready` deltaP `9.5735` edge `0.0848` maxDD `-1.8022`
- `market_context_high->fx_24h` score `0.6884` n `185` status `ready` deltaP `16.2643` edge `0.0295` maxDD `-1.4448`
- `market_context_high->index_24h` score `0.0657` n `185` status `ready` deltaP `2.7472` edge `0.11` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `0.0196` n `185` status `ready` deltaP `19.6825` edge `0.729` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.0156` n `217` status `ready` deltaP `5.2699` edge `0.0424` maxDD `-2.6402`
- `market_context_high->index_1h` score `-0.5656` n `217` status `ready` deltaP `0.1656` edge `0.0108` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.5722` n `217` status `ready` deltaP `-1.5894` edge `0.0` maxDD `-0.3548`
- `market_context_high->unknown_1h` score `-0.7645` n `217` status `ready` deltaP `3.1127` edge `-0.0125` maxDD `-3.0902`
- `market_context_high->metal_1h` score `-0.8498` n `217` status `ready` deltaP `1.7978` edge `0.0027` maxDD `-5.5577`
- `market_context_high->fx_4h` score `-1.0743` n `217` status `ready` deltaP `-7.0936` edge `-0.0023` maxDD `-1.0513`
- `market_context_high->metal_4h` score `-1.7906` n `217` status `ready` deltaP `6.2317` edge `0.0715` maxDD `-11.9812`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
