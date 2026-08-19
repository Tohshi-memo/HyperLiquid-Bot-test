# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-19T04:37:23.415958+00:00`
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

- `market_context_high->crypto_major_24h` score `2.1356` n `96` status `ready` deltaP `7.118` edge `0.2513` maxDD `-4.9964`
- `market_context_high->equity_1h` score `1.6127` n `96` status `ready` deltaP `13.3546` edge `0.0755` maxDD `-0.4112`
- `market_context_high->equity_4h` score `1.5092` n `96` status `ready` deltaP `8.8668` edge `0.1555` maxDD `-2.4411`
- `market_context_high->commodity_24h` score `1.3066` n `96` status `ready` deltaP `16.1458` edge `0.2432` maxDD `-4.666`
- `market_context_high->metal_4h` score `1.1708` n `96` status `ready` deltaP `17.6321` edge `0.0376` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.9887` n `96` status `ready` deltaP `11.4583` edge `0.1081` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.86` n `96` status `ready` deltaP `15.0137` edge `0.0103` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.3175` n `96` status `ready` deltaP `9.2066` edge `-0.0122` maxDD `-0.4843`
- `market_context_high->crypto_alt_4h` score `0.3038` n `96` status `ready` deltaP `10.3659` edge `0.0832` maxDD `-5.4926`
- `market_context_high->metal_1h` score `0.1488` n `96` status `ready` deltaP `5.9693` edge `0.0113` maxDD `-0.4291`
- `market_context_high->fx_4h` score `0.0194` n `96` status `ready` deltaP `7.3424` edge `0.0038` maxDD `-0.3539`
- `market_context_high->index_4h` score `-0.0221` n `96` status `ready` deltaP `6.4278` edge `0.0208` maxDD `-0.5728`
- `market_context_high->fx_1h` score `-0.3455` n `96` status `ready` deltaP `-1.6218` edge `0.0024` maxDD `-0.2043`
- `market_context_high->crypto_alt_1h` score `-0.3567` n `96` status `ready` deltaP `2.9753` edge `0.0146` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-0.4188` n `96` status `ready` deltaP `2.233` edge `0.0159` maxDD `-2.7581`
- `market_context_high->unknown_24h` score `-0.4438` n `96` status `ready` deltaP `12.8472` edge `-0.072` maxDD `-1.0505`
- `market_context_high->commodity_4h` score `-0.5213` n `96` status `ready` deltaP `1.499` edge `0.0082` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8643` n `96` status `ready` deltaP `-7.2917` edge `-0.0056` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-2.2659` n `96` status `ready` deltaP `-3.6458` edge `0.0646` maxDD `-11.4635`
- `market_context_high->fx_24h` score `-4.3026` n `96` status `ready` deltaP `-25.5208` edge `-0.0301` maxDD `-1.9981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
