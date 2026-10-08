# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T02:07:25.921355+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.604` n `90` status `ready` deltaP `-4.3224` edge `3.2997` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7831` n `62` status `ready` deltaP `37.6672` edge `0.6678` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.8965` n `62` status `ready` deltaP `22.1725` edge `0.5613` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.9844` n `62` status `ready` deltaP `14.8287` edge `0.4098` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.7349` n `62` status `ready` deltaP `34.2561` edge `0.1662` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.233` n `90` status `ready` deltaP `10.0461` edge `0.7731` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.913` n `62` status `ready` deltaP `32.0024` edge `0.0556` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4228` n `62` status `ready` deltaP `9.8754` edge `0.1716` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2783` n `90` status `ready` deltaP `15.7317` edge `0.1814` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.079` n `62` status `ready` deltaP `17.1666` edge `0.1186` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9277` n `62` status `ready` deltaP `24.2757` edge `0.0138` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.4799` n `90` status `ready` deltaP `12.3914` edge `0.0836` maxDD `-1.0977`
- `news_risk_high->metal_4h` score `1.4676` n `62` status `ready` deltaP `21.0956` edge `0.0891` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.3836` n `62` status `ready` deltaP `-7.2974` edge `0.2885` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.1878` n `90` status `ready` deltaP `20.7727` edge `0.1623` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0633` n `90` status `ready` deltaP `21.6734` edge `0.0188` maxDD `-0.3077`
- `news_risk_high->crypto_alt_1h` score `1.028` n `62` status `ready` deltaP `2.4097` edge `0.1215` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.725` n `90` status `ready` deltaP `12.0958` edge `0.004` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1097` n `90` status `ready` deltaP `9.8037` edge `0.0376` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.0976` n `90` status `ready` deltaP `7.1127` edge `0.5589` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
