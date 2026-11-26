# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T20:37:34.842254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3132`

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

- `news_risk_high->unknown_1h` score `3218.3615` n `31` status `ready` deltaP `2.3807` edge `268.1985` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3196.419` n `31` status `ready` deltaP `4.3962` edge `266.3446` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `29.1646` n `31` status `ready` deltaP `38.3681` edge `2.1746` maxDD `0.0`
- `news_risk_high->equity_24h` score `26.4564` n `31` status `ready` deltaP `37.5` edge `1.9547` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `23.0275` n `31` status `ready` deltaP `37.6736` edge `1.6678` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.0385` n `31` status `ready` deltaP `24.6262` edge `0.7594` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.8493` n `31` status `ready` deltaP `36.6149` edge `0.5414` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.6845` n `31` status `ready` deltaP `24.048` edge `0.4242` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.4773` n `31` status `ready` deltaP `17.6927` edge `0.8542` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9199` n `31` status `ready` deltaP `41.5379` edge `0.1459` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.6687` n `31` status `ready` deltaP `38.8889` edge `0.1298` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2756` n `31` status `ready` deltaP `19.0892` edge `0.1644` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.1225` n `31` status `ready` deltaP `34.9381` edge `0.0533` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5883` n `31` status `ready` deltaP `30.9446` edge `0.0179` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2545` n `31` status `ready` deltaP `7.9148` edge `0.2824` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0445` n `31` status `ready` deltaP `11.0585` edge `0.2241` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3872` n `31` status `ready` deltaP `27.7863` edge `0.0205` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8234` n `31` status `ready` deltaP `14.3391` edge `0.0657` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3182` n `31` status `ready` deltaP `10.9608` edge `0.0075` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4419` n `31` status `ready` deltaP `-2.6608` edge `0.0071` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
