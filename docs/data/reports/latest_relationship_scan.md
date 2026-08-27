# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T23:37:21.500999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.3986` n `50` status `ready` deltaP `11.6319` edge `4.289` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.6682` n `50` status `ready` deltaP `37.8403` edge `1.7642` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6712` n `50` status `ready` deltaP `24.6402` edge `0.9016` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.9408` n `50` status `ready` deltaP `46.0903` edge `0.1087` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.8561` n `50` status `ready` deltaP `27.4028` edge `0.3148` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7775` n `50` status `ready` deltaP `44.1341` edge `0.0296` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.9742` n `128` status `ready` deltaP `5.3819` edge `0.2852` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9576` n `50` status `ready` deltaP `16.3772` edge `0.1729` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7897` n `50` status `ready` deltaP `31.4028` edge `0.0382` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2282` n `148` status `ready` deltaP `17.8024` edge `0.1077` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5204` n `50` status `ready` deltaP `20.3533` edge `0.008` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.2517` n `50` status `ready` deltaP `17.5629` edge `0.0151` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.0548` n `50` status `ready` deltaP `20.2073` edge `0.0295` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8341` n `148` status `ready` deltaP `8.6745` edge `0.0567` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5004` n `50` status `ready` deltaP `14.0` edge `0.0021` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1366` n `50` status `ready` deltaP `7.6587` edge `0.0004` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0968` n `50` status `ready` deltaP `5.4012` edge `-0.001` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0359` n `50` status `ready` deltaP `8.0732` edge `-0.0037` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1099` n `50` status `ready` deltaP `4.7988` edge `-0.0015` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4046` n `148` status `ready` deltaP `6.9381` edge `-0.0064` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
