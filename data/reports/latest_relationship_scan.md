# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T11:22:29.075227+00:00`
- Price records: `672`
- Market context records: `5449`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->crypto_major_24h` score `3.2328` n `187` status `ready` deltaP `17.3592` edge `0.6077` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.9963` n `196` status `ready` deltaP `15.5457` edge `0.3753` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.8956` n `187` status `ready` deltaP `10.9849` edge `0.5788` maxDD `-25.5256`
- `market_context_high->equity_4h` score `2.5542` n `196` status `ready` deltaP `12.6618` edge `0.2923` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.2913` n `196` status `ready` deltaP `10.6085` edge `0.2843` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5087` n `199` status `ready` deltaP `8.1628` edge `0.0845` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2608` n `187` status `ready` deltaP `11.3803` edge `0.0354` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1439` n `199` status `ready` deltaP `6.6342` edge `0.0171` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.2869` n `199` status `ready` deltaP `3.8117` edge `0.0182` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3261` n `199` status `ready` deltaP `0.9569` edge `0.0626` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4351` n `199` status `ready` deltaP `2.1439` edge `0.074` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.6039` n `199` status `ready` deltaP `-0.1873` edge `-0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8159` n `196` status `ready` deltaP `7.5348` edge `0.0427` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.0174` n `187` status `ready` deltaP `15.3938` edge `0.0883` maxDD `-13.7088`
- `market_context_high->fx_4h` score `-1.1017` n `196` status `ready` deltaP `1.0515` edge `0.0037` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.402` n `199` status `ready` deltaP `-2.4215` edge `-0.0059` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6413` n `196` status `ready` deltaP `-8.2753` edge `-0.031` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2455` n `196` status `ready` deltaP `-6.67` edge `-0.0455` maxDD `-14.1062`
- `market_context_high->metal_24h` score `-7.3959` n `187` status `ready` deltaP `-5.1498` edge `-0.1761` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.4587` n `187` status `ready` deltaP `8.1987` edge `0.1935` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
