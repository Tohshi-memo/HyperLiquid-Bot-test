# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T16:07:32.877847+00:00`
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

- `news_risk_high->unknown_24h` score `53.8443` n `50` status `ready` deltaP `11.9584` edge `4.4073` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.8886` n `50` status `ready` deltaP `43.1404` edge `2.4139` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.131` n `56` status `ready` deltaP `23.2796` edge `0.7866` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.5279` n `50` status `ready` deltaP `30.1005` edge `0.3528` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `4.5118` n `50` status `ready` deltaP `21.7816` edge `0.2801` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.317` n `50` status `ready` deltaP `43.4073` edge `0.0746` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0139` n `56` status `ready` deltaP `46.6681` edge `0.0324` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.1348` n `60` status `ready` deltaP `12.5749` edge `0.2131` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.0578` n `121` status `ready` deltaP `5.3468` edge `0.2924` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.0563` n `121` status `ready` deltaP `28.0519` edge `0.1696` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7569` n `121` status `ready` deltaP `18.2914` edge `0.1485` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3602` n `50` status `ready` deltaP `26.9948` edge `0.0318` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.5017` n `60` status `ready` deltaP `20.1497` edge `0.0078` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1382` n `121` status `ready` deltaP `9.4757` edge `0.0767` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8407` n `56` status `ready` deltaP `19.9042` edge `0.0514` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.6519` n `56` status `ready` deltaP `13.8502` edge `0.0151` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4659` n `60` status `ready` deltaP `13.1637` edge `0.004` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1148` n `56` status `ready` deltaP `7.4042` edge `0.0001` maxDD `-0.1919`
- `news_risk_high->equity_1h` score `0.0032` n `60` status `ready` deltaP `11.2575` edge `-0.0171` maxDD `-2.6031`
- `news_risk_high->metal_1h` score `-0.004` n `60` status `ready` deltaP `4.8503` edge `-0.0035` maxDD `-0.6807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
