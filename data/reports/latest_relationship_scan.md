# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T11:17:50.199477+00:00`
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

- `news_risk_high->unknown_24h` score `53.4409` n `50` status `ready` deltaP `11.6118` edge `4.376` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `30.7625` n `50` status `ready` deltaP `40.1941` edge `2.3397` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.9634` n `50` status `ready` deltaP `26.0122` edge `0.9168` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4655` n `50` status `ready` deltaP `30.1005` edge `0.3476` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.8996` n `50` status `ready` deltaP `46.7002` edge `0.1012` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9333` n `50` status `ready` deltaP `45.811` edge `0.0314` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `2.8122` n `50` status `ready` deltaP `19.182` edge `0.1558` maxDD `-2.6128`
- `news_risk_high->index_24h` score `2.5595` n `50` status `ready` deltaP `28.9012` edge `0.0357` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2498` n `139` status `ready` deltaP `18.3431` edge `0.1059` maxDD `-0.5894`
- `market_context_high->unknown_24h` score `2.2162` n `133` status `ready` deltaP `5.5968` edge `0.2206` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.0921` n `56` status `ready` deltaP `12.2754` edge `0.1282` maxDD `-0.8558`
- `news_risk_high->equity_4h` score `1.8427` n `50` status `ready` deltaP `24.4756` edge `0.0667` maxDD `-2.105`
- `market_context_high->metal_24h` score `1.6655` n `133` status `ready` deltaP `19.3769` edge `0.1282` maxDD `-3.1535`
- `news_risk_high->fx_1h` score `1.4564` n `56` status `ready` deltaP `19.6429` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.0992` n `56` status `ready` deltaP `15.4513` edge `0.0191` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9401` n `139` status `ready` deltaP `7.779` edge `0.0715` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.4867` n `56` status `ready` deltaP `13.6976` edge `0.0031` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3914` n `56` status `ready` deltaP `7.4423` edge `0.0056` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.1782` n `50` status `ready` deltaP `10.3598` edge `-0.0011` maxDD `-0.249`
- `news_risk_high->index_4h` score `0.1298` n `50` status `ready` deltaP `7.3902` edge `0.0012` maxDD `-0.1719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
