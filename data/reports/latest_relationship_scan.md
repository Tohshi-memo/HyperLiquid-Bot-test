# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T07:37:29.467881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9414`

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

- `market_context_high->crypto_alt_4h` score `7.826` n `130` status `ready` deltaP `19.3972` edge `0.6143` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0617` n `54` status `ready` deltaP `38.5017` edge `0.3318` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0617` n `54` status `ready` deltaP `38.5017` edge `0.3318` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.2542` n `130` status `ready` deltaP `23.811` edge `0.4946` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.6429` n `56` status `ready` deltaP `20.0566` edge `0.3812` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.6429` n `56` status `ready` deltaP `20.0566` edge `0.3812` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.312` n `56` status `ready` deltaP `35.9539` edge `0.3984` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.312` n `56` status `ready` deltaP `35.9539` edge `0.3984` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3845` n `142` status `ready` deltaP `11.9718` edge `0.142` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1157` n `142` status `ready` deltaP `8.1956` edge `0.1189` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5035` n `130` status `ready` deltaP `14.144` edge `0.0522` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.075` n `68` status `ready` deltaP `6.3315` edge `0.0204` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.075` n `68` status `ready` deltaP `6.3315` edge `0.0204` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.1665` n `68` status `ready` deltaP `3.0648` edge `0.0041` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.1665` n `68` status `ready` deltaP `3.0648` edge `0.0041` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.1864` n `142` status `ready` deltaP `9.332` edge `0.0092` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.2409` n `142` status `ready` deltaP `6.006` edge `0.0039` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.3828` n `68` status `ready` deltaP `2.994` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3828` n `68` status `ready` deltaP `2.994` edge `0.0041` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.483` n `142` status `ready` deltaP `8.2117` edge `0.0343` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
