# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T23:07:32.395570+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `1.1363` n `78` status `ready` deltaP `10.0415` edge `0.1693` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.3098` n `78` status `ready` deltaP `10.4088` edge `0.0181` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.2149` n `78` status `ready` deltaP `4.0803` edge `0.0553` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.203` n `78` status `ready` deltaP `10.0875` edge `0.0041` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.081` n `78` status `ready` deltaP `7.8252` edge `0.0028` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.0492` n `78` status `ready` deltaP `3.0308` edge `0.1403` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.1849` n `78` status `ready` deltaP `-1.342` edge `0.0378` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.38` n `78` status `ready` deltaP `0.7869` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.5157` n `78` status `ready` deltaP `-3.612` edge `-0.0063` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.8783` n `78` status `ready` deltaP `-2.733` edge `-0.0005` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-1.133` n `78` status `ready` deltaP `-1.0019` edge `-0.0158` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-1.2959` n `78` status `ready` deltaP `-5.4878` edge `-0.039` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.4254` n `78` status `ready` deltaP `-4.4911` edge `0.0158` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-2.5544` n `78` status `ready` deltaP `23.3036` edge `0.6758` maxDD `-86.0244`
- `news_risk_high->commodity_1h` score `-2.9136` n `78` status `ready` deltaP `-17.8643` edge `-0.0068` maxDD `-1.6855`
- `news_risk_high->metal_24h` score `-3.1795` n `78` status `ready` deltaP `1.5709` edge `-0.2285` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9275` n `78` status `ready` deltaP `-25.1837` edge `0.0004` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.4949` n `78` status `ready` deltaP `-8.0598` edge `-0.0572` maxDD `-14.0916`
- `news_risk_high->commodity_24h` score `-9.4917` n `78` status `ready` deltaP `-26.3809` edge `-0.0462` maxDD `-28.1786`
- `news_risk_high->crypto_major_24h` score `-12.5478` n `78` status `ready` deltaP `-27.874` edge `-0.0095` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
