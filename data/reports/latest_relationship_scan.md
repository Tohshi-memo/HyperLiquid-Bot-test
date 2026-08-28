# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T14:52:27.546876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.7097` n `50` status `ready` deltaP `11.6118` edge `4.3984` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.6574` n `50` status `ready` deltaP `42.6205` edge `2.3981` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.0232` n `56` status `ready` deltaP `22.5174` edge `0.7827` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4499` n `50` status `ready` deltaP `30.1005` edge `0.3463` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.4427` n `50` status `ready` deltaP `44.2738` edge `0.0793` maxDD `-0.0053`
- `news_risk_high->crypto_major_24h` score `4.0405` n `50` status `ready` deltaP `20.9151` edge `0.2466` maxDD `-2.6128`
- `news_risk_high->fx_4h` score `3.9481` n `56` status `ready` deltaP `45.9059` edge `0.032` maxDD `-0.0559`
- `market_context_high->metal_24h` score `2.8685` n `125` status `ready` deltaP `26.2738` edge `0.1658` maxDD `-3.1535`
- `market_context_high->unknown_24h` score `2.5562` n `125` status `ready` deltaP `5.2118` edge `0.2515` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.4937` n `125` status `ready` deltaP `18.0317` edge `0.1283` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3952` n `50` status `ready` deltaP `27.3414` edge `0.0324` maxDD `-0.2064`
- `news_risk_high->unknown_1h` score `2.2432` n `56` status `ready` deltaP `12.8743` edge `0.1368` maxDD `-0.8558`
- `news_risk_high->fx_1h` score `1.4815` n `56` status `ready` deltaP `19.9423` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.074` n `56` status `ready` deltaP `15.4513` edge `0.017` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `1.0193` n `125` status `ready` deltaP `8.2743` edge `0.0748` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7669` n `56` status `ready` deltaP `19.2945` edge `0.046` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5985` n `56` status `ready` deltaP `13.3929` edge `0.0137` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4991` n `56` status `ready` deltaP `13.8473` edge `0.0037` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3459` n `56` status `ready` deltaP `6.8435` edge `0.0058` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0916` n `56` status `ready` deltaP `7.0993` edge `0.0002` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
