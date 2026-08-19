# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T05:22:25.362290+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11618`

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

- `market_context_high->crypto_major_24h` score `2.0946` n `96` status `ready` deltaP `6.7708` edge `0.2502` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.6199` n `96` status `ready` deltaP `13.3546` edge `0.0761` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.5902` n `96` status `ready` deltaP `9.3242` edge `0.1592` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.2624` n `96` status `ready` deltaP `15.625` edge `0.241` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.2024` n `96` status `ready` deltaP `17.937` edge `0.0382` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9935` n `96` status `ready` deltaP `11.4583` edge `0.1085` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.8731` n `96` status `ready` deltaP `15.1634` edge `0.0104` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.2899` n `96` status `ready` deltaP `9.0569` edge `-0.0135` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.2738` n `96` status `ready` deltaP `10.3659` edge `0.0807` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1512` n `96` status `ready` deltaP `5.9693` edge `0.0115` maxDD `-0.4291`
- `market_context_high->fx_4h` score `0.0471` n `96` status `ready` deltaP `7.7998` edge `0.0043` maxDD `-0.3539`
- `market_context_high->index_4h` score `0.0253` n `96` status `ready` deltaP `6.8851` edge `0.0217` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.337` n `96` status `ready` deltaP `-1.4721` edge `0.0025` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.3465` n `96` status `ready` deltaP `3.125` edge `0.0149` maxDD `-2.413`
- `market_context_high->unknown_24h` score `-0.3968` n `96` status `ready` deltaP `13.1944` edge `-0.0704` maxDD `-1.0505`
- `market_context_high->crypto_major_1h` score `-0.4001` n `96` status `ready` deltaP `2.5324` edge `0.0163` maxDD `-2.7581`
- `market_context_high->commodity_4h` score `-0.5213` n `96` status `ready` deltaP `1.499` edge `0.0082` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8721` n `96` status `ready` deltaP `-7.4414` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2464` n `96` status `ready` deltaP `-3.6458` edge `0.0671` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.2942` n `96` status `ready` deltaP `-25.5208` edge `-0.0294` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
