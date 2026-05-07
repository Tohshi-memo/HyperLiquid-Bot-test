# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T01:37:13.327638+00:00`
- Price records: `506`
- Market context records: `600`
- Flow alert records: `1697`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.5977` n `146` status `ready` deltaP `6.8761` edge `0.3421` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.7076` n `146` status `ready` deltaP `11.0491` edge `0.2687` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0342` n `146` status `ready` deltaP `10.8941` edge `0.0189` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3269` n `146` status `ready` deltaP `1.8292` edge `0.0037` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6359` n `146` status `ready` deltaP `0.9187` edge `-0.0023` maxDD `-2.8282`
- `market_context_high->commodity_1h` score `-0.6483` n `146` status `ready` deltaP `1.1581` edge `0.0357` maxDD `-3.7959`
- `market_context_high->crypto_alt_1h` score `-1.1173` n `146` status `ready` deltaP `5.6187` edge `0.0009` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.1262` n `146` status `ready` deltaP `-3.8722` edge `-0.0077` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.1817` n `146` status `ready` deltaP `-1.4909` edge `-0.0075` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7411` n `146` status `ready` deltaP `5.2065` edge `-0.0075` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-1.9446` n `146` status `ready` deltaP `3.7545` edge `0.0699` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.1973` n `146` status `ready` deltaP `0.4594` edge `-0.0339` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.4793` n `146` status `ready` deltaP `-6.8999` edge `0.0389` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-2.6482` n `146` status `ready` deltaP `13.1423` edge `0.0623` maxDD `-22.648`
- `market_context_high->equity_4h` score `-3.1775` n `146` status `ready` deltaP `-2.8327` edge `-0.0307` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3267` n `146` status `ready` deltaP `-4.83` edge `-0.0491` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.8298` n `146` status `ready` deltaP `-7.5229` edge `0.0811` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.3256` n `146` status `ready` deltaP `-3.2526` edge `-0.0157` maxDD `-21.0414`
- `market_context_high->equity_24h` score `-4.5164` n `146` status `ready` deltaP `-10.6181` edge `-0.0451` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.9998` n `146` status `ready` deltaP `1.0455` edge `-0.2358` maxDD `-8.3588`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
