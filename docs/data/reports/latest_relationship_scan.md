# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T08:07:21.004233+00:00`
- Price records: `672`
- Market context records: `3263`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10503`

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

- `risk_on_high->crypto_major_4h` score `16.6235` n `32` status `ready` deltaP `32.0122` edge `1.2841` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.6235` n `32` status `ready` deltaP `32.0122` edge `1.2841` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.7878` n `103` status `ready` deltaP `15.8727` edge `2.646` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `12.7257` n `103` status `ready` deltaP `45.3901` edge `0.8007` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.1067` n `103` status `ready` deltaP `29.406` edge `0.8183` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.969` n `32` status `ready` deltaP `13.186` edge `0.7606` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.969` n `32` status `ready` deltaP `13.186` edge `0.7606` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.2401` n `103` status `ready` deltaP `17.6595` edge `1.5239` maxDD `-53.663`
- `risk_on_high->equity_4h` score `4.0492` n `32` status `ready` deltaP `16.6921` edge `0.5213` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `4.0492` n `32` status `ready` deltaP `16.6921` edge `0.5213` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.3706` n `160` status `ready` deltaP `20.3659` edge `0.1576` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.1608` n `32` status `ready` deltaP `7.7657` edge `0.3322` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.1608` n `32` status `ready` deltaP `7.7657` edge `0.3322` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.4366` n `32` status `ready` deltaP `4.0396` edge `0.216` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.4366` n `32` status `ready` deltaP `4.0396` edge `0.216` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.2097` n `103` status `ready` deltaP `18.9017` edge `2.099` maxDD `-152.2601`
- `risk_on_high->metal_1h` score `0.3056` n `32` status `ready` deltaP `6.25` edge `0.066` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.3056` n `32` status `ready` deltaP `6.25` edge `0.066` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2836` n `32` status `ready` deltaP `1.0479` edge `0.1731` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2836` n `32` status `ready` deltaP `1.0479` edge `0.1731` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
