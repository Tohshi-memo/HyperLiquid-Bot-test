# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T13:07:35.354891+00:00`
- Price records: `672`
- Market context records: `3485`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `55.4589` n `32` status `ready` deltaP `58.5069` edge `4.2358` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.4589` n `32` status `ready` deltaP `58.5069` edge `4.2358` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.1908` n `32` status `ready` deltaP `59.8958` edge `4.0484` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.1908` n `32` status `ready` deltaP `59.8958` edge `4.0484` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.9393` n `32` status `ready` deltaP `56.0764` edge `3.3711` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.9393` n `32` status `ready` deltaP `56.0764` edge `3.3711` maxDD `0.0`
- `risk_on_high->index_24h` score `24.4679` n `32` status `ready` deltaP `51.3889` edge `1.6964` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.4679` n `32` status `ready` deltaP `51.3889` edge `1.6964` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `20.2633` n `155` status `ready` deltaP `24.2125` edge `2.3003` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.3518` n `155` status `ready` deltaP `32.8506` edge `2.0349` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `19.2839` n `155` status `ready` deltaP `20.4402` edge `2.2708` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.5865` n `32` status `ready` deltaP `30.0305` edge `1.2109` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.5865` n `32` status `ready` deltaP `30.0305` edge `1.2109` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `15.3788` n `32` status `ready` deltaP `29.3403` edge `1.1121` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.3788` n `32` status `ready` deltaP `29.3403` edge `1.1121` maxDD `-0.7574`
- `market_context_high->index_24h` score `13.0945` n `155` status `ready` deltaP `35.905` edge `1.0735` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.8785` n `32` status `ready` deltaP `10.8994` edge `0.7683` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.8785` n `32` status `ready` deltaP `10.8994` edge `0.7683` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.5697` n `155` status `ready` deltaP `23.8161` edge `1.0093` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.3934` n `32` status `ready` deltaP `18.8262` edge `0.5512` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
