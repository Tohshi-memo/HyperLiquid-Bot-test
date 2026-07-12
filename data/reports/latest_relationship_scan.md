# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T04:04:08.504703+00:00`
- Price records: `672`
- Market context records: `6460`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5875`

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

- `news_risk_high->crypto_alt_24h` score `11.9079` n `32` status `ready` deltaP `31.0764` edge `0.7999` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.4411` n `147` status `ready` deltaP `17.1025` edge `0.8361` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3106` n `32` status `ready` deltaP `52.2569` edge `0.1775` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1084` n `32` status `ready` deltaP `42.7591` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.5894` n `32` status `ready` deltaP `31.9444` edge `0.1067` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.5815` n `32` status `ready` deltaP `13.3681` edge `0.448` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4697` n `32` status `ready` deltaP `29.7904` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5974` n `172` status `ready` deltaP `-5.4867` edge `0.2598` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `1.3947` n `32` status `ready` deltaP `12.631` edge `0.1413` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7391` n `32` status `ready` deltaP `8.3271` edge `0.0854` maxDD `-1.6923`
- `market_context_high->commodity_24h` score `0.3264` n `147` status `ready` deltaP `6.7531` edge `0.169` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3138` n `172` status `ready` deltaP `9.9724` edge `0.0273` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.2848` n `172` status `ready` deltaP `8.5508` edge `0.1221` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2717` n `172` status `ready` deltaP `-15.0879` edge `0.3638` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.0713` n `172` status `ready` deltaP `10.6743` edge `0.0436` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.2547` n `32` status `ready` deltaP `5.6325` edge `-0.0243` maxDD `-0.7581`
- `news_risk_high->index_24h` score `-0.4861` n `32` status `ready` deltaP `4.3403` edge `-0.0041` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.5301` n `32` status `ready` deltaP `0.8982` edge `-0.0242` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.5505` n `172` status `ready` deltaP `0.8982` edge `0.0012` maxDD `-1.8877`
- `market_context_high->commodity_1h` score `-0.5837` n `172` status `ready` deltaP `-0.3342` edge `-0.0043` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
