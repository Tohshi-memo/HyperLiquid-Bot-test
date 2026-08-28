# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T12:37:31.109391+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.5417` n `50` status `ready` deltaP `11.6118` edge `4.3844` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.031` n `50` status `ready` deltaP `41.0607` edge `2.3563` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.2118` n `52` status `ready` deltaP `24.6248` edge `0.8677` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4511` n `50` status `ready` deltaP `30.1005` edge `0.3464` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.7367` n `50` status `ready` deltaP `45.8336` edge `0.0934` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9077` n `52` status `ready` deltaP `45.3565` edge `0.0323` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.1256` n `50` status `ready` deltaP `19.5286` edge `0.1796` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5487` n `50` status `ready` deltaP `28.9012` edge `0.0348` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4146` n `134` status `ready` deltaP `18.138` edge `0.121` maxDD `-0.5894`
- `market_context_high->metal_24h` score `2.4114` n `133` status `ready` deltaP `22.2697` edge `0.1544` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.0921` n `56` status `ready` deltaP `12.2754` edge `0.1282` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `1.8802` n `133` status `ready` deltaP `5.5968` edge `0.1926` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4803` n `56` status `ready` deltaP `19.9423` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1135` n `56` status `ready` deltaP `15.601` edge `0.0193` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `1.0054` n `134` status `ready` deltaP `7.4247` edge `0.0793` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.9442` n `52` status `ready` deltaP `21.4001` edge `0.0547` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.51` n `56` status `ready` deltaP `13.997` edge `0.0041` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3638` n `56` status `ready` deltaP `7.1429` edge `0.0053` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.2543` n `52` status `ready` deltaP `10.9053` edge `0.0016` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.0509` n `56` status `ready` deltaP `5.9346` edge `0.0009` maxDD `-0.0486`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
