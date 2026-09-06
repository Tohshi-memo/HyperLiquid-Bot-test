# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T12:51:30.057356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10703`

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

- `risk_on_high->unknown_24h` score `102.6353` n `110` status `ready` deltaP `20.9849` edge `8.4387` maxDD `-0.7193`
- `risk_on_and_context->unknown_24h` score `102.6353` n `110` status `ready` deltaP `20.9849` edge `8.4387` maxDD `-0.7193`
- `risk_on_high->crypto_major_24h` score `5.2839` n `110` status `ready` deltaP `18.1724` edge `0.9837` maxDD `-43.4952`
- `risk_on_and_context->crypto_major_24h` score `5.2839` n `110` status `ready` deltaP `18.1724` edge `0.9837` maxDD `-43.4952`
- `market_context_high->equity_24h` score `1.2681` n `196` status `ready` deltaP `12.9925` edge `0.3292` maxDD `-14.8115`
- `risk_on_high->index_1h` score `-0.1328` n `142` status `ready` deltaP `4.6471` edge `-0.0033` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1328` n `142` status `ready` deltaP `4.6471` edge `-0.0033` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1638` n `142` status `ready` deltaP `7.5799` edge `-0.0003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1638` n `142` status `ready` deltaP `7.5799` edge `-0.0003` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4809` n `142` status `ready` deltaP `5.851` edge `-0.0132` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4809` n `142` status `ready` deltaP `5.851` edge `-0.0132` maxDD `-2.6638`
- `risk_on_high->crypto_alt_1h` score `-0.4868` n `142` status `ready` deltaP `1.204` edge `0.0531` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4868` n `142` status `ready` deltaP `1.204` edge `0.0531` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.6002` n `142` status `ready` deltaP `0.0506` edge `0.0` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.6002` n `142` status `ready` deltaP `0.0506` edge `0.0` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7911` n `250` status `ready` deltaP `0.1126` edge `-0.0017` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.8686` n `142` status `ready` deltaP `0.1835` edge `0.0175` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.8686` n `142` status `ready` deltaP `0.1835` edge `0.0175` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9459` n `250` status `ready` deltaP `3.5461` edge `-0.0067` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.0925` n `250` status `ready` deltaP `2.8048` edge `0.0007` maxDD `-3.1683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
