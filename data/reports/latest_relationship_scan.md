# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T20:51:06.707542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4196`

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

- `news_risk_high->equity_4h` score `1.6189` n `87` status `ready` deltaP `14.133` edge `0.2039` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7733` n `87` status `ready` deltaP `13.758` edge `0.0205` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.283` n `87` status `ready` deltaP `11.5665` edge `0.0045` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.2351` n `87` status `ready` deltaP `4.1245` edge `0.0576` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.1174` n `87` status `ready` deltaP `4.2946` edge `0.0009` maxDD `-0.2336`
- `news_risk_high->fx_1h` score `-0.31` n `87` status `ready` deltaP `-0.0189` edge `0.0002` maxDD `-0.1858`
- `news_risk_high->metal_1h` score `-0.333` n `87` status `ready` deltaP `-0.3235` edge `-0.0048` maxDD `-0.5256`
- `news_risk_high->index_24h` score `-0.5714` n `87` status `ready` deltaP `-1.2451` edge `0.14` maxDD `-6.6786`
- `news_risk_high->crypto_major_4h` score `-0.6313` n `87` status `ready` deltaP `0.7149` edge `0.0829` maxDD `-9.1553`
- `news_risk_high->crypto_alt_1h` score `-0.6371` n `87` status `ready` deltaP `2.6705` edge `0.0233` maxDD `-5.8225`
- `news_risk_high->fx_24h` score `-0.6984` n `87` status `ready` deltaP `-5.8407` edge `0.025` maxDD `-0.2073`
- `news_risk_high->crypto_major_1h` score `-0.8182` n `87` status `ready` deltaP `-2.4778` edge `0.0055` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-1.0548` n `87` status `ready` deltaP `-1.6172` edge `-0.0339` maxDD `-1.5773`
- `news_risk_high->equity_24h` score `-1.307` n `87` status `ready` deltaP `26.4866` edge `0.8145` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-1.7121` n `87` status `ready` deltaP `-2.8736` edge `0.0633` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.9036` n `87` status `ready` deltaP `-17.4152` edge `-0.0069` maxDD `-1.8506`
- `news_risk_high->metal_24h` score `-2.9784` n `87` status `ready` deltaP `3.5638` edge `-0.216` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.125` n `87` status `ready` deltaP `-26.3316` edge `-0.0024` maxDD `-4.5976`
- `news_risk_high->crypto_major_24h` score `-7.0988` n `87` status `ready` deltaP `-19.9466` edge `0.0732` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.2526` n `87` status `ready` deltaP `-25.7495` edge `-0.0179` maxDD `-29.1857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
