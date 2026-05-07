# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T10:22:20.611178+00:00`
- Price records: `541`
- Market context records: `637`
- Flow alert records: `1804`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `6.1812` n `146` status `ready` deltaP `17.3988` edge `0.4325` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.5819` n `146` status `ready` deltaP `7.8544` edge `0.4176` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0941` n `146` status `ready` deltaP `8.891` edge `0.0158` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3396` n `146` status `ready` deltaP `1.6898` edge `0.003` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5023` n `146` status `ready` deltaP `1.979` edge `0.0424` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6822` n `146` status `ready` deltaP `-0.0167` edge `-0.002` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1593` n `146` status `ready` deltaP `-4.3162` edge `-0.0075` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.184` n `146` status `ready` deltaP `5.9106` edge `-0.0066` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3387` n `146` status `ready` deltaP `-2.6434` edge `-0.0129` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.6947` n `146` status `ready` deltaP `5.7715` edge `-0.0074` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.1139` n `146` status `ready` deltaP `3.9178` edge `0.0547` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.3702` n `146` status `ready` deltaP `-1.3422` edge `-0.0363` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5623` n `146` status `ready` deltaP `13.0607` edge `0.07` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0434` n `146` status `ready` deltaP `-8.5811` edge `0.0031` maxDD `-5.9609`
- `market_context_high->commodity_4h` score `-3.3574` n `146` status `ready` deltaP `-5.2927` edge `0.1056` maxDD `-13.0076`
- `market_context_high->metal_1h` score `-3.4592` n `146` status `ready` deltaP `-5.3609` edge `-0.0566` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4767` n `146` status `ready` deltaP `-4.4133` edge `-0.0451` maxDD `-10.5498`
- `market_context_high->fx_24h` score `-4.3647` n `146` status `ready` deltaP `-3.6592` edge `-0.018` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.806` n `146` status `ready` deltaP `1.4129` edge `-0.2221` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.8899` n `146` status `ready` deltaP `-11.7323` edge `-0.0688` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
