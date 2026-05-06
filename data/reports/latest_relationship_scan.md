# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T15:52:27.006262+00:00`
- Price records: `467`
- Market context records: `558`
- Flow alert records: `1574`
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

- `market_context_high->crypto_alt_24h` score `4.9169` n `140` status `ready` deltaP `7.6415` edge `0.3636` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0162` n `140` status `ready` deltaP `10.027` edge `0.2179` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0072` n `146` status `ready` deltaP `10.1208` edge `0.0206` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3153` n `146` status `ready` deltaP `1.9473` edge `0.0044` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5313` n `146` status `ready` deltaP `1.9757` edge `0.04` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6133` n `146` status `ready` deltaP `1.2639` edge `-0.0017` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.144` n `146` status `ready` deltaP `-0.9147` edge `-0.0082` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2106` n `146` status `ready` deltaP `-3.8166` edge `-0.0151` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3211` n `146` status `ready` deltaP `4.5564` edge `-0.009` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8267` n `140` status `ready` deltaP `-5.8525` edge `0.0863` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.0089` n `146` status `ready` deltaP `3.4335` edge `-0.018` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.0596` n `146` status `ready` deltaP `1.3101` edge `-0.0281` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.4292` n `146` status `ready` deltaP `1.8513` edge `0.0422` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.0746` n `146` status `ready` deltaP `-2.7167` edge `-0.0229` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3566` n `146` status `ready` deltaP `-5.1437` edge `-0.0495` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-3.5193` n `146` status `ready` deltaP `9.1684` edge `0.0162` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.5669` n `146` status `ready` deltaP `-6.0219` edge `0.093` maxDD `-13.0076`
- `market_context_high->equity_24h` score `-3.7255` n `140` status `ready` deltaP `-10.183` edge `0.0179` maxDD `-10.5047`
- `market_context_high->fx_24h` score `-4.3657` n `140` status `ready` deltaP `-5.4223` edge `-0.0406` maxDD `-18.3035`
- `market_context_high->unknown_4h` score `-4.4919` n `146` status `ready` deltaP `0.284` edge `-0.1884` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
