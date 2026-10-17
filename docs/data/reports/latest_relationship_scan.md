# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T06:22:25.821243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8268`

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

- `market_context_high->crypto_alt_4h` score `8.1445` n `127` status `ready` deltaP `20.7389` edge `0.6319` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0821` n `54` status `ready` deltaP `38.5017` edge `0.3335` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0821` n `54` status `ready` deltaP `38.5017` edge `0.3335` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3389` n `127` status `ready` deltaP `23.8645` edge `0.5013` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.1635` n `54` status `ready` deltaP `23.1595` edge `0.4039` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1635` n `54` status `ready` deltaP `23.1595` edge `0.4039` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3719` n `54` status `ready` deltaP `36.0547` edge `0.4054` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3719` n `54` status `ready` deltaP `36.0547` edge `0.4054` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6258` n `137` status `ready` deltaP `13.6533` edge `0.1509` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0235` n `137` status `ready` deltaP `6.9529` edge `0.1195` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5571` n `127` status `ready` deltaP `14.6941` edge `0.053` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.0977` n `63` status `ready` deltaP `3.9253` edge `0.0041` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0977` n `63` status `ready` deltaP `3.9253` edge `0.0041` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2063` n `137` status `ready` deltaP `6.6713` edge `0.0039` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2222` n `137` status `ready` deltaP `8.899` edge `0.0091` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4444` n `63` status `ready` deltaP `1.9009` edge `0.0035` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4444` n `63` status `ready` deltaP `1.9009` edge `0.0035` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.458` n `63` status `ready` deltaP `3.1295` edge `0.0132` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.458` n `63` status `ready` deltaP `3.1295` edge `0.0132` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.4791` n `63` status `ready` deltaP `4.118` edge `0.0134` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
