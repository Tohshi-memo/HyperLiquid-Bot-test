# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T10:37:27.967188+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.3773` n `50` status `ready` deltaP `11.6118` edge `4.3707` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.5973` n `50` status `ready` deltaP `39.6742` edge `2.3294` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.913` n `50` status `ready` deltaP `26.0122` edge `0.9126` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4679` n `50` status `ready` deltaP `30.1005` edge `0.3478` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.9904` n `50` status `ready` deltaP `47.2201` edge `0.1053` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9735` n `50` status `ready` deltaP `46.2683` edge `0.0317` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.685` n `50` status `ready` deltaP `19.182` edge `0.1452` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5643` n `50` status `ready` deltaP `28.9012` edge `0.0361` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.4298` n `133` status `ready` deltaP `5.5968` edge `0.2384` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.3341` n `142` status `ready` deltaP `18.6319` edge `0.111` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.0969` n `56` status `ready` deltaP `12.2754` edge `0.1286` maxDD `-0.8558`
- `news_risk_high->equity_4h` score `1.8667` n `50` status `ready` deltaP `24.4756` edge `0.0687` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.4708` n `56` status `ready` deltaP `19.7926` edge `0.0076` maxDD `-0.0257`
- `market_context_high->metal_24h` score `1.2147` n `133` status `ready` deltaP `17.6412` edge `0.1147` maxDD `-3.1535`
- `news_risk_high->equity_1h` score `1.1315` n `56` status `ready` deltaP `15.7507` edge `0.0198` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9324` n `142` status `ready` deltaP `8.4022` edge `0.0667` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4859` n `56` status `ready` deltaP `13.6976` edge `0.003` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3734` n `56` status `ready` deltaP `7.2926` edge `0.0051` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.183` n `50` status `ready` deltaP `10.3598` edge `-0.0007` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1334` n `50` status `ready` deltaP `7.3902` edge `0.0015` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
