# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T05:37:24.871137+00:00`
- Price records: `672`
- Market context records: `3455`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `56.6109` n `32` status `ready` deltaP `58.5069` edge `4.3318` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.6109` n `32` status `ready` deltaP `58.5069` edge `4.3318` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `56.2292` n `32` status `ready` deltaP `59.8958` edge `4.3016` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `56.2292` n `32` status `ready` deltaP `59.8958` edge `4.3016` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.0089` n `32` status `ready` deltaP `56.0764` edge `3.3769` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.0089` n `32` status `ready` deltaP `56.0764` edge `3.3769` maxDD `0.0`
- `risk_on_high->index_24h` score `23.9579` n `32` status `ready` deltaP `51.3889` edge `1.6539` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.9579` n `32` status `ready` deltaP `51.3889` edge `1.6539` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `22.3223` n `155` status `ready` deltaP `20.4402` edge `2.524` maxDD `-56.6728`
- `market_context_high->crypto_major_24h` score `21.4153` n `155` status `ready` deltaP `24.2125` edge `2.3963` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.4214` n `155` status `ready` deltaP `32.8506` edge `2.0407` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `15.6829` n `32` status `ready` deltaP `29.4207` edge `1.223` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.6829` n `32` status `ready` deltaP `29.4207` edge `1.223` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `13.845` n `32` status `ready` deltaP `28.9931` edge `0.9866` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.845` n `32` status `ready` deltaP `28.9931` edge `0.9866` maxDD `-0.7574`
- `market_context_high->index_24h` score `12.5845` n `155` status `ready` deltaP `35.905` edge `1.031` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.5601` n `32` status `ready` deltaP `9.6799` edge `0.7499` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5601` n `32` status `ready` deltaP `9.6799` edge `0.7499` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `4.6396` n `32` status `ready` deltaP `19.436` edge `0.5787` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.6396` n `32` status `ready` deltaP `19.436` edge `0.5787` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
