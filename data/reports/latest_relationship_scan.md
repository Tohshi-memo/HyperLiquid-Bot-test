# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T04:22:32.658062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.7799` n `70` status `ready` deltaP `33.8046` edge `0.1309` maxDD `-0.6348`
- `market_context_high->equity_24h` score `1.5876` n `70` status `ready` deltaP `16.0814` edge `0.046` maxDD `-0.6726`
- `market_context_high->crypto_major_24h` score `1.5389` n `70` status `ready` deltaP `2.5496` edge `0.2489` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4721` n `70` status `ready` deltaP `21.7014` edge `-0.022` maxDD `0.0`
- `market_context_high->commodity_4h` score `0.7285` n `104` status `ready` deltaP `12.8401` edge `0.0565` maxDD `-0.8962`
- `market_context_high->metal_4h` score `-0.1947` n `104` status `ready` deltaP `16.3345` edge `0.0156` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3236` n `113` status `ready` deltaP `-0.4557` edge `-0.0014` maxDD `-0.2968`
- `market_context_high->commodity_1h` score `-0.3245` n `113` status `ready` deltaP `-0.6187` edge `0.0087` maxDD `-1.0276`
- `market_context_high->crypto_major_4h` score `-0.5823` n `104` status `ready` deltaP `3.037` edge `0.0259` maxDD `-4.6638`
- `market_context_high->metal_1h` score `-0.6193` n `113` status `ready` deltaP `2.635` edge `0.0024` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.7765` n `104` status `ready` deltaP `-4.667` edge `-0.0069` maxDD `-0.59`
- `market_context_high->index_1h` score `-0.8559` n `113` status `ready` deltaP `-2.7542` edge `-0.0008` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.0308` n `113` status `ready` deltaP `-4.4141` edge `-0.0196` maxDD `-3.3165`
- `market_context_high->crypto_alt_1h` score `-1.0623` n `113` status `ready` deltaP `-3.9955` edge `-0.0086` maxDD `-4.4101`
- `market_context_high->crypto_major_1h` score `-1.6731` n `113` status `ready` deltaP `-3.41` edge `-0.0163` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.7915` n `104` status `ready` deltaP `-9.6154` edge `-0.0043` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1551` n `70` status `ready` deltaP `-30.3224` edge `-0.0416` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.3031` n `104` status `ready` deltaP `-17.3663` edge `-0.127` maxDD `-8.1221`
- `market_context_high->crypto_alt_4h` score `-3.5212` n `104` status `ready` deltaP `-7.5867` edge `-0.0327` maxDD `-16.786`
- `market_context_high->metal_24h` score `-5.3728` n `70` status `ready` deltaP `-22.3264` edge `-0.0477` maxDD `-7.0954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
