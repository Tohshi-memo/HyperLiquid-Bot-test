# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T23:22:31.879292+00:00`
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

- `news_risk_high->equity_4h` score `1.0875` n `77` status `ready` deltaP `9.5087` edge `0.1666` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.2901` n `77` status `ready` deltaP `10.0452` edge `0.018` maxDD `-0.4888`
- `news_risk_high->index_1h` score `0.1822` n `77` status `ready` deltaP `9.6878` edge `0.0041` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.1815` n `77` status `ready` deltaP `3.6473` edge `0.0539` maxDD `-1.396`
- `news_risk_high->fx_4h` score `0.0577` n `77` status `ready` deltaP `7.3923` edge `0.0027` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.0066` n `77` status `ready` deltaP `3.6707` edge `0.1415` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.1972` n `77` status `ready` deltaP `-1.6617` edge `0.0389` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.3347` n `77` status `ready` deltaP `1.3532` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4837` n `77` status `ready` deltaP `-2.996` edge `-0.0063` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.9311` n `77` status `ready` deltaP `-3.2993` edge `-0.0035` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-1.2006` n `77` status `ready` deltaP `-1.5515` edge `-0.0208` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-1.332` n `77` status `ready` deltaP `-6.1372` edge `-0.0393` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.5259` n `77` status `ready` deltaP `-5.0879` edge `0.0069` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-2.6412` n `77` status `ready` deltaP `22.9979` edge `0.6667` maxDD `-86.0244`
- `news_risk_high->commodity_1h` score `-2.8945` n `77` status `ready` deltaP `-17.5811` edge `-0.0071` maxDD `-1.6855`
- `news_risk_high->metal_24h` score `-3.2106` n `77` status `ready` deltaP `1.2131` edge `-0.2301` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.0095` n `77` status `ready` deltaP `-26.0136` edge `-0.0009` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.6208` n `77` status `ready` deltaP `-8.6732` edge `-0.0636` maxDD `-14.0916`
- `news_risk_high->commodity_24h` score `-9.5287` n `77` status `ready` deltaP `-26.3258` edge `-0.05` maxDD `-28.1509`
- `news_risk_high->crypto_major_24h` score `-12.7623` n `77` status `ready` deltaP `-28.86` edge `-0.0208` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
