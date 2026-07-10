# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T22:22:23.585839+00:00`
- Price records: `672`
- Market context records: `6328`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.4782` n `32` status `ready` deltaP `43.2292` edge `1.0164` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0644` n `32` status `ready` deltaP `50.6944` edge `0.1674` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4324` n `32` status `ready` deltaP `16.6667` edge `0.5351` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2033` n `32` status `ready` deltaP `43.8262` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.3863` n `32` status `ready` deltaP `30.0347` edge `0.1025` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5138` n `32` status `ready` deltaP `14.8765` edge `0.1416` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9369` n `32` status `ready` deltaP `11.7702` edge `0.0878` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.1493` n `196` status `ready` deltaP `10.4343` edge `0.0392` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `-0.0037` n `208` status `ready` deltaP `-7.9197` edge `0.1533` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.268` n `196` status `ready` deltaP `5.3385` edge `0.0205` maxDD `-0.9023`
- `market_context_high->metal_24h` score `-0.3244` n `148` status `ready` deltaP `18.5482` edge `0.0916` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.3324` n `208` status `ready` deltaP `4.9113` edge `0.0024` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.5519` n `208` status `ready` deltaP `-3.1207` edge `0.0023` maxDD `-0.8466`
- `news_risk_high->index_24h` score `-0.5968` n `32` status `ready` deltaP `2.2569` edge `-0.0044` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.6085` n `208` status `ready` deltaP `-1.4106` edge `-0.0003` maxDD `-2.1314`
- `market_context_high->equity_4h` score `-0.7386` n `196` status `ready` deltaP `4.6043` edge `0.0445` maxDD `-8.2573`
- `news_risk_high->unknown_1h` score `-0.7575` n `32` status `ready` deltaP `5.7822` edge `-0.0672` maxDD `-0.7581`
- `news_risk_high->metal_1h` score `-0.7792` n `32` status `ready` deltaP `-3.7425` edge `-0.0252` maxDD `-1.6464`
- `market_context_high->fx_1h` score `-0.8109` n `208` status `ready` deltaP `-1.9087` edge `-0.0021` maxDD `-0.8865`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
