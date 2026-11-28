# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T05:52:28.325916+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3716`

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

- `news_risk_high->unknown_1h` score `3346.4617` n `31` status `ready` deltaP `1.4825` edge `278.8795` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3207.0945` n `31` status `ready` deltaP `3.634` edge `267.2393` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.6201` n `31` status `ready` deltaP `30.6759` edge `1.4305` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.6601` n `31` status `ready` deltaP `28.5962` edge `0.9477` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.5573` n `31` status `ready` deltaP `24.4367` edge `0.8002` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.5703` n `31` status `ready` deltaP `20.0531` edge `0.5842` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.086` n `31` status `ready` deltaP `28.0783` edge `0.2847` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7474` n `31` status `ready` deltaP `38.6762` edge `0.1506` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.6787` n `31` status `ready` deltaP `14.0342` edge `0.648` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.4132` n `31` status `ready` deltaP `12.7076` edge `0.2272` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.2576` n `31` status `ready` deltaP `27.8009` edge `0.0113` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.2221` n `31` status `ready` deltaP `24.9567` edge `0.0188` maxDD `0.0`
- `news_risk_high->index_4h` score `2.2141` n `31` status `ready` deltaP `27.4686` edge `0.0274` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.074` n `31` status `ready` deltaP `14.1491` edge `0.0972` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6784` n `31` status `ready` deltaP `5.2202` edge `0.2265` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5854` n `31` status `ready` deltaP `8.5136` edge `0.1822` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0943` n `31` status `ready` deltaP `24.0438` edge `0.0079` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3009` n `31` status `ready` deltaP `7.9121` edge `0.0256` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2458` n `31` status `ready` deltaP `10.0708` edge `0.0201` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3376` n `31` status `ready` deltaP `-2.062` edge `0.0118` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
