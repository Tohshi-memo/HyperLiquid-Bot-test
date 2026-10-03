# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T16:52:29.109048+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4220`

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

- `market_context_high->unknown_1h` score `368.6984` n `50` status `ready` deltaP `11.9222` edge `30.6503` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `297.4958` n `50` status `ready` deltaP `12.3476` edge `24.709` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2647` n `50` status `ready` deltaP `29.9792` edge `1.1592` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8291` n `50` status `ready` deltaP `37.6326` edge `0.8765` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6672` n `62` status `ready` deltaP `29.9575` edge `0.7377` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.6193` n `67` status `ready` deltaP `38.4851` edge `0.6487` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6963` n `67` status `ready` deltaP `27.7007` edge `0.5911` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.1981` n `50` status `ready` deltaP `16.9329` edge `0.5573` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.0553` n `50` status `ready` deltaP `17.1037` edge `0.5195` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6167` n `62` status `ready` deltaP `33.8095` edge `0.1752` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.936` n `67` status `ready` deltaP `27.7894` edge `0.204` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2758` n `50` status `ready` deltaP `14.503` edge `0.2426` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `3.1103` n `67` status `ready` deltaP `34.0644` edge `0.0583` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9918` n `68` status `ready` deltaP `13.658` edge `0.1938` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.927` n `50` status `ready` deltaP `12.9521` edge `0.2026` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4181` n `67` status `ready` deltaP `20.5179` edge `0.1063` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0581` n `68` status `ready` deltaP `25.3963` edge `0.0172` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.6205` n `68` status `ready` deltaP `5.8559` edge `0.1479` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5705` n `50` status `ready` deltaP `21.8383` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
