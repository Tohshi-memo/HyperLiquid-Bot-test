# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T01:52:25.855641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6237`

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

- `market_context_high->unknown_24h` score `4570.7169` n `75` status `ready` deltaP `-7.8959` edge `380.9748` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `187.4519` n `75` status `ready` deltaP `1.1077` edge `15.6269` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `81.3496` n `108` status `ready` deltaP `-5.1951` edge `6.8424` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `14.7589` n `92` status `ready` deltaP `35.0921` edge `1.1133` maxDD `-6.3871`
- `market_context_high->equity_24h` score `12.3116` n `75` status `ready` deltaP `23.9097` edge `1.1008` maxDD `-12.0716`
- `news_risk_high->crypto_alt_4h` score `5.498` n `108` status `ready` deltaP `20.7317` edge `0.4586` maxDD `-7.4246`
- `market_context_high->index_24h` score `5.3303` n `75` status `ready` deltaP `46.2153` edge `0.1544` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `2.6927` n `75` status `ready` deltaP `26.9533` edge `0.0781` maxDD `-0.3387`
- `market_context_high->fx_1h` score `1.0297` n `75` status `ready` deltaP `15.6048` edge `0.0002` maxDD `-0.1407`
- `news_risk_high->crypto_alt_1h` score `0.8337` n `108` status `ready` deltaP `8.727` edge `0.1067` maxDD `-3.9659`
- `market_context_high->metal_4h` score `0.6719` n `75` status `ready` deltaP `12.935` edge `0.0424` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.5671` n `75` status `ready` deltaP `8.3952` edge `0.0203` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.5533` n `75` status `ready` deltaP `12.437` edge `0.0023` maxDD `-0.1285`
- `market_context_high->equity_1h` score `0.2518` n `75` status `ready` deltaP `0.9661` edge `0.1134` maxDD `-2.3383`
- `market_context_high->commodity_24h` score `0.1662` n `75` status `ready` deltaP `24.7014` edge `0.0908` maxDD `-12.0667`
- `market_context_high->equity_4h` score `0.0956` n `75` status `ready` deltaP `-6.5711` edge `0.1954` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `-0.2311` n `75` status `ready` deltaP `1.4152` edge `0.0637` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3288` n `75` status `ready` deltaP `0.8443` edge `0.0184` maxDD `-0.4475`
- `market_context_high->crypto_alt_1h` score `-0.6772` n `75` status `ready` deltaP `-1.0878` edge `0.0787` maxDD `-5.9953`
- `news_risk_high->index_1h` score `-0.6779` n `108` status `ready` deltaP `4.0031` edge `-0.0032` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
