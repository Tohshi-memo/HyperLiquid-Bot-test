# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T14:07:29.350707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11602`

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

- `news_risk_high->unknown_24h` score `53.6761` n `50` status `ready` deltaP `11.6118` edge `4.3956` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.4502` n `50` status `ready` deltaP `42.1005` edge `2.3843` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.9868` n `56` status `ready` deltaP `22.2125` edge `0.7817` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4415` n `50` status `ready` deltaP `30.1005` edge `0.3456` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.5299` n `50` status `ready` deltaP `44.7938` edge `0.0831` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9213` n `56` status `ready` deltaP `45.601` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.7325` n `50` status `ready` deltaP `20.3951` edge `0.2244` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.7229` n `128` status `ready` deltaP `24.9188` edge `0.1627` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4452` n `50` status `ready` deltaP `27.8614` edge `0.0331` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3646` n `128` status `ready` deltaP `18.083` edge `0.1172` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.2707` n `56` status `ready` deltaP `13.1737` edge `0.1371` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `2.1674` n `128` status `ready` deltaP `5.3618` edge `0.2181` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4815` n `56` status `ready` deltaP `19.9423` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1147` n `56` status `ready` deltaP `15.601` edge `0.0194` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.8117` n `128` status `ready` deltaP `6.9237` edge `0.0665` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7803` n `56` status `ready` deltaP `19.4469` edge `0.0467` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5705` n `56` status `ready` deltaP `13.088` edge `0.0134` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4999` n `56` status `ready` deltaP `13.8473` edge `0.0038` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3255` n `56` status `ready` deltaP `6.6938` edge `0.0051` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1074` n `56` status `ready` deltaP `7.2518` edge `0.0005` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
