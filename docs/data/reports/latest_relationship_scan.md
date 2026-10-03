# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T16:07:26.647508+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4210`

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

- `market_context_high->unknown_1h` score `368.1393` n `50` status `ready` deltaP `11.6228` edge `30.6057` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `296.8416` n `50` status `ready` deltaP `12.1951` edge `24.6555` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `14.2803` n `50` status `ready` deltaP `29.9792` edge `1.1605` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.8171` n `50` status `ready` deltaP `37.6326` edge `0.8755` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `10.8531` n `64` status `ready` deltaP `38.4527` edge `0.6684` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6438` n `62` status `ready` deltaP `29.7842` edge `0.7369` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.6038` n `64` status `ready` deltaP `27.2485` edge `0.5864` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2899` n `50` status `ready` deltaP `17.3902` edge `0.5619` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.2251` n `50` status `ready` deltaP `17.561` edge `0.5306` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6179` n `62` status `ready` deltaP `33.8095` edge `0.1753` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9938` n `64` status `ready` deltaP `27.4771` edge `0.2109` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3453` n `50` status `ready` deltaP `14.9521` edge `0.2454` maxDD `-3.6376`
- `news_risk_high->index_4h` score `3.1341` n `64` status `ready` deltaP `34.032` edge `0.0605` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0992` n `50` status `ready` deltaP `34.8232` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `3.029` n `68` status `ready` deltaP `13.9574` edge `0.1949` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.9641` n `50` status `ready` deltaP `13.2515` edge `0.2037` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3321` n `64` status `ready` deltaP `18.9787` edge `0.1094` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.0593` n `68` status `ready` deltaP `25.3963` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.69` n `68` status `ready` deltaP `6.305` edge `0.1507` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5945` n `50` status `ready` deltaP `22.1377` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
