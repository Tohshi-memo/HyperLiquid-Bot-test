# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T15:37:25.968977+00:00`
- Price records: `672`
- Market context records: `6100`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11111`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.5895` n `30` status `ready` deltaP `34.3055` edge `0.4185` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.1921` n `32` status `ready` deltaP `43.5213` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3296` n `32` status `ready` deltaP `27.994` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3846` n `195` status `ready` deltaP `8.4756` edge `0.1506` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.3415` n `32` status `ready` deltaP `14.4274` edge `0.1225` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7546` n `32` status `ready` deltaP `9.8241` edge `0.0774` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1` n `30` status `ready` deltaP `9.2361` edge `0.0384` maxDD `-2.3058`
- `news_risk_high->commodity_24h` score `-0.0585` n `30` status `ready` deltaP `16.1806` edge `-0.0922` maxDD `-0.3101`
- `market_context_high->fx_1h` score `-0.3159` n `195` status `ready` deltaP `0.6863` edge `-0.0005` maxDD `-0.5659`
- `market_context_high->equity_1h` score `-0.5609` n `195` status `ready` deltaP `1.8363` edge `0.0274` maxDD `-4.2573`
- `market_context_high->metal_4h` score `-0.5951` n `195` status `ready` deltaP `3.847` edge `0.0168` maxDD `-3.4996`
- `market_context_high->metal_1h` score `-0.6475` n `195` status `ready` deltaP `4.0373` edge `-0.001` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.6585` n `32` status `ready` deltaP `-1.3473` edge `-0.0257` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.7536` n `195` status `ready` deltaP `-1.8394` edge `-0.0059` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.7638` n `195` status `ready` deltaP `3.3755` edge `0.026` maxDD `-1.381`
- `market_context_high->crypto_alt_1h` score `-0.8213` n `195` status `ready` deltaP `4.8081` edge `0.0379` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8565` n `195` status `ready` deltaP `5.2127` edge `0.0322` maxDD `-9.807`
- `news_risk_high->index_1h` score `-1.0478` n `32` status `ready` deltaP `-8.9259` edge `-0.0185` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1389` n `195` status `ready` deltaP `-1.8586` edge `0.0044` maxDD `-0.9531`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
