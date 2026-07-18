# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T17:22:28.677358+00:00`
- Price records: `672`
- Market context records: `7162`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `market_context_high->fx_4h` score `0.053` n `159` status `ready` deltaP `11.2527` edge `0.0119` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3872` n `169` status `ready` deltaP `2.0781` edge `0.0013` maxDD `-0.4606`
- `market_context_high->crypto_alt_1h` score `-0.575` n `169` status `ready` deltaP `0.4597` edge `0.0271` maxDD `-5.9775`
- `market_context_high->unknown_1h` score `-0.5805` n `169` status `ready` deltaP `-1.2871` edge `0.0244` maxDD `-1.4688`
- `market_context_high->crypto_major_1h` score `-0.6221` n `169` status `ready` deltaP `3.7035` edge `0.0366` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.6434` n `169` status `ready` deltaP `-0.6448` edge `-0.0161` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7833` n `169` status `ready` deltaP `0.8087` edge `-0.0042` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-2.0209` n `169` status `ready` deltaP `-7.4682` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-2.0514` n `159` status `ready` deltaP `-5.9393` edge `0.0121` maxDD `-6.1736`
- `market_context_high->commodity_4h` score `-2.1079` n `159` status `ready` deltaP `-5.0582` edge `-0.0384` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9517` n `159` status `ready` deltaP `-10.7043` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.542` n `169` status `ready` deltaP `-0.6599` edge `-0.0381` maxDD `-15.5469`
- `market_context_high->index_4h` score `-3.9648` n `159` status `ready` deltaP `-2.7746` edge `-0.042` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4844` n `133` status `ready` deltaP `-13.4581` edge `-0.1531` maxDD `-4.4704`
- `market_context_high->crypto_major_4h` score `-4.7712` n `159` status `ready` deltaP `3.3057` edge `0.0157` maxDD `-25.1605`
- `market_context_high->fx_24h` score `-4.8294` n `133` status `ready` deltaP `-14.3157` edge `-0.0243` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.3824` n `159` status `ready` deltaP `-2.3364` edge `-0.0233` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.0534` n `133` status `ready` deltaP `-32.3556` edge `-0.1074` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7586` n `133` status `ready` deltaP `-32.1232` edge `-0.1976` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.8659` n `159` status `ready` deltaP `-4.4332` edge `-0.2091` maxDD `-66.6801`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
