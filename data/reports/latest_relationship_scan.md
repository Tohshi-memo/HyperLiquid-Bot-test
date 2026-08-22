# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T11:52:39.670154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.0147` n `145` status `ready` deltaP `7.6472` edge `0.0563` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2707` n `134` status `ready` deltaP `18.6112` edge `-0.0576` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0638` n `134` status `ready` deltaP `7.3103` edge `0.0097` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0225` n `145` status `ready` deltaP `4.2154` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2901` n `134` status `ready` deltaP `6.3001` edge `-0.0176` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.2977` n `145` status `ready` deltaP `1.275` edge `-0.0048` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3437` n `145` status `ready` deltaP `4.4879` edge `0.033` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5652` n `134` status `ready` deltaP `2.9851` edge `0.0112` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6613` n `134` status `ready` deltaP `-0.7121` edge `0.005` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8982` n `145` status `ready` deltaP `-6.6694` edge `-0.0016` maxDD `-1.1941`
- `market_context_high->crypto_alt_4h` score `-1.5172` n `134` status `ready` deltaP `5.4992` edge `-0.0361` maxDD `-5.4926`
- `market_context_high->equity_4h` score `-1.6557` n `134` status `ready` deltaP `-0.248` edge `0.0699` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-1.9141` n `120` status `ready` deltaP `-5.382` edge `0.0597` maxDD `-4.666`
- `market_context_high->fx_24h` score `-1.9204` n `120` status `ready` deltaP `-1.0417` edge `0.0079` maxDD `-2.2121`
- `market_context_high->crypto_alt_1h` score `-2.3396` n `145` status `ready` deltaP `-2.0989` edge `-0.0315` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.3898` n `145` status `ready` deltaP `-4.7718` edge `-0.1048` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.4348` n `120` status `ready` deltaP `-7.8472` edge `-0.0463` maxDD `-20.2626`
- `market_context_high->crypto_major_4h` score `-5.075` n `134` status `ready` deltaP `-0.7599` edge `-0.3084` maxDD `-3.7558`
- `market_context_high->metal_24h` score `-5.3993` n `120` status `ready` deltaP `-23.8542` edge `-0.2024` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
