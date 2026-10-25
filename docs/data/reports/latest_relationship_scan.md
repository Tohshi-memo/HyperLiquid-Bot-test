# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T00:52:34.431223+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7190`

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

- `market_context_high->unknown_4h` score `22.4493` n `95` status `ready` deltaP `1.741` edge `1.8927` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.6871` n `55` status `ready` deltaP `22.2886` edge `0.0829` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9204` n `95` status `ready` deltaP `11.9897` edge `0.053` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.2918` n `107` status `ready` deltaP `2.3323` edge `0.0102` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3314` n `107` status `ready` deltaP `-1.3977` edge `0.0023` maxDD `-0.1712`
- `market_context_high->metal_1h` score `-0.922` n `107` status `ready` deltaP `1.1836` edge `-0.0053` maxDD `-1.6873`
- `market_context_high->fx_4h` score `-0.9661` n `95` status `ready` deltaP `-3.5976` edge `0.0041` maxDD `-0.5168`
- `market_context_high->index_1h` score `-1.09` n `107` status `ready` deltaP `-2.7814` edge `-0.0071` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.6506` n `55` status `ready` deltaP `-4.7538` edge `-0.0026` maxDD `-1.5942`
- `market_context_high->crypto_major_24h` score `-2.169` n `55` status `ready` deltaP `-0.3977` edge `-0.0376` maxDD `-14.3593`
- `market_context_high->crypto_major_1h` score `-2.414` n `107` status `ready` deltaP `0.6897` edge `-0.0337` maxDD `-10.432`
- `market_context_high->crypto_alt_1h` score `-3.2746` n `107` status `ready` deltaP `0.5079` edge `-0.0546` maxDD `-14.4004`
- `market_context_high->metal_4h` score `-3.3325` n `95` status `ready` deltaP `-10.1027` edge `-0.0323` maxDD `-5.9114`
- `market_context_high->metal_24h` score `-3.3396` n `55` status `ready` deltaP `-10.9753` edge `0.0084` maxDD `-7.0827`
- `market_context_high->equity_1h` score `-4.0111` n `107` status `ready` deltaP `-1.1347` edge `-0.0938` maxDD `-12.6316`
- `market_context_high->index_4h` score `-4.8961` n `95` status `ready` deltaP `-23.474` edge `-0.053` maxDD `-5.2144`
- `market_context_high->crypto_alt_24h` score `-7.3908` n `55` status `ready` deltaP `2.6452` edge `-0.2587` maxDD `-49.1843`
- `market_context_high->index_24h` score `-7.6687` n `55` status `ready` deltaP `-37.4463` edge `-0.1766` maxDD `-6.6921`
- `market_context_high->unknown_1h` score `-8.1781` n `107` status `ready` deltaP `-0.1973` edge `-0.6313` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-13.3952` n `95` status `ready` deltaP `-23.6264` edge `-0.3407` maxDD `-42.4446`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
