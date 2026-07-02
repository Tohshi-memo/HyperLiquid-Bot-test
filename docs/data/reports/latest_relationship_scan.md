# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T05:07:32.640170+00:00`
- Price records: `672`
- Market context records: `5422`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_24h` score `4.2266` n `189` status `ready` deltaP `19.8661` edge `0.6738` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.8134` n `200` status `ready` deltaP `16.4451` edge `0.4374` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.6162` n `189` status `ready` deltaP `10.1191` edge `0.5875` maxDD `-21.6219`
- `market_context_high->crypto_alt_4h` score `2.9609` n `200` status `ready` deltaP `11.8537` edge `0.3318` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.4999` n `200` status `ready` deltaP `12.1037` edge `0.2915` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4242` n `200` status `ready` deltaP `7.8563` edge `0.0795` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1015` n `200` status `ready` deltaP `6.2994` edge `0.0158` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0584` n `189` status `ready` deltaP `9.2097` edge `0.033` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.1908` n `200` status `ready` deltaP `3.7425` edge `0.0837` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2905` n `200` status `ready` deltaP `0.997` edge `0.0653` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4971` n `200` status `ready` deltaP `1.9491` edge `0.0131` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.5887` n `200` status `ready` deltaP `0.003` edge `-0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-1.0312` n `200` status `ready` deltaP `5.5488` edge `0.038` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1557` n `200` status `ready` deltaP `0.6159` edge `0.0021` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.3392` n `189` status `ready` deltaP `14.6412` edge `0.0894` maxDD `-12.5551`
- `market_context_high->commodity_1h` score `-1.455` n `200` status `ready` deltaP `-3.0` edge `-0.0068` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.6703` n `200` status `ready` deltaP `-8.128` edge `-0.0357` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.29` n `200` status `ready` deltaP `-7.0305` edge `-0.0468` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.2017` n `189` status `ready` deltaP `10.8301` edge `0.2807` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2149` n `189` status `ready` deltaP `-4.8942` edge `-0.1546` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
