# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T22:49:25.698035+00:00`
- Price records: `672`
- Market context records: `2083`
- Flow alert records: `7891`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_major_4h` score `10.2274` n `196` status `ready` deltaP `36.1312` edge `0.6644` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `9.9582` n `196` status `ready` deltaP `30.0024` edge `0.7443` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `7.4374` n `196` status `ready` deltaP `24.9595` edge `0.5283` maxDD `-2.6599`
- `market_context_high->unknown_24h` score `5.0955` n `195` status `ready` deltaP `21.4604` edge `0.8136` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.9557` n `196` status `ready` deltaP `21.4784` edge `0.2959` maxDD `-5.0894`
- `market_context_high->index_4h` score `2.3094` n `196` status `ready` deltaP `17.2971` edge `0.1455` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.1578` n `196` status `ready` deltaP `15.6941` edge `0.1738` maxDD `-3.2225`
- `market_context_high->index_24h` score `1.8341` n `195` status `ready` deltaP `10.6166` edge `0.2049` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.8267` n `195` status `ready` deltaP `21.6707` edge `0.4976` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `1.8179` n `196` status `ready` deltaP `12.3396` edge `0.1806` maxDD `-4.9097`
- `market_context_high->equity_1h` score `0.6327` n `196` status `ready` deltaP `9.6236` edge `0.0674` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.5209` n `196` status `ready` deltaP `5.3801` edge `0.0795` maxDD `-3.0902`
- `market_context_high->crypto_major_24h` score `0.2757` n `195` status `ready` deltaP `21.1587` edge `0.7405` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0424` n `196` status `ready` deltaP `4.5155` edge `0.0254` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.1398` n `195` status `ready` deltaP `14.7077` edge `0.0296` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.2207` n `196` status `ready` deltaP `12.8422` edge `0.1505` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.4881` n `196` status `ready` deltaP `4.6804` edge `0.0302` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8479` n `196` status `ready` deltaP `-1.4084` edge `0.0015` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.3082` n `196` status `ready` deltaP `-3.3412` edge `0.0014` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.4649` n `195` status `ready` deltaP `11.0318` edge `0.1945` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
