# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T17:22:29.957590+00:00`
- Price records: `672`
- Market context records: `5476`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11466`

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

- `market_context_high->crypto_major_24h` score `3.5883` n `193` status `ready` deltaP `16.628` edge `0.6422` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.5246` n `196` status `ready` deltaP `13.0724` edge `0.2871` maxDD `-7.4425`
- `market_context_high->crypto_major_4h` score `2.3763` n `196` status `ready` deltaP `14.0213` edge `0.3338` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.0296` n `196` status `ready` deltaP `10.5619` edge `0.2628` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.9452` n `193` status `ready` deltaP `9.4748` edge `0.5235` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.5741` n `196` status `ready` deltaP `8.8904` edge `0.0851` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.2373` n `196` status `ready` deltaP `7.592` edge `0.0185` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1078` n `193` status `ready` deltaP `10.3807` edge `0.0325` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3087` n `196` status `ready` deltaP `1.3198` edge `0.0005` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3676` n `196` status `ready` deltaP `3.3881` edge `0.0143` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4721` n `196` status `ready` deltaP `0.6324` edge `0.0526` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6309` n `196` status `ready` deltaP `1.9461` edge `0.059` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.7651` n `196` status `ready` deltaP `7.9455` edge `0.0442` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9391` n `196` status `ready` deltaP `2.8279` edge `0.0054` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4667` n `196` status `ready` deltaP `-2.9451` edge `-0.0078` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8876` n `193` status `ready` deltaP `13.1827` edge `0.0688` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-4.2171` n `196` status `ready` deltaP `-9.1899` edge `-0.0377` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2658` n `196` status `ready` deltaP `-5.9606` edge `-0.0443` maxDD `-14.3822`
- `market_context_high->crypto_alt_24h` score `-6.9791` n `193` status `ready` deltaP `7.8332` edge `0.2359` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0779` n `193` status `ready` deltaP `-3.3543` edge `-0.1473` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
