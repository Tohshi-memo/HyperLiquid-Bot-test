# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T00:22:29.846364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `69.1385` n `80` status `ready` deltaP `-34.8958` edge `9.3649` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `4.6968` n `80` status `ready` deltaP `34.0625` edge `0.1992` maxDD `-0.4576`
- `market_context_high->commodity_4h` score `0.9694` n `108` status `ready` deltaP `11.3087` edge `0.0525` maxDD `-0.7687`
- `market_context_high->index_24h` score `0.0025` n `80` status `ready` deltaP `12.0139` edge `-0.0399` maxDD `-0.5323`
- `market_context_high->metal_4h` score `-0.1742` n `108` status `ready` deltaP `15.927` edge `0.0122` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.2857` n `112` status `ready` deltaP `1.1762` edge `0.0113` maxDD `-0.7695`
- `market_context_high->fx_1h` score `-0.4311` n `112` status `ready` deltaP `-0.0053` edge `0.0006` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4328` n `112` status `ready` deltaP `2.8176` edge `-0.0027` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.6359` n `108` status `ready` deltaP `1.451` edge `-0.0022` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.6604` n `112` status `ready` deltaP `-4.6514` edge `-0.0015` maxDD `-0.5064`
- `market_context_high->crypto_major_24h` score `-0.6858` n `80` status `ready` deltaP `-3.0556` edge `0.1538` maxDD `-12.3746`
- `market_context_high->crypto_major_4h` score `-0.8769` n `108` status `ready` deltaP `2.1568` edge `-0.006` maxDD `-4.6638`
- `market_context_high->index_4h` score `-1.2132` n `108` status `ready` deltaP `-10.3432` edge `-0.0057` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-1.2277` n `112` status `ready` deltaP `-5.5068` edge `-0.0213` maxDD `-3.9504`
- `market_context_high->crypto_alt_1h` score `-1.7809` n `112` status `ready` deltaP `-4.9134` edge `-0.0128` maxDD `-4.5615`
- `market_context_high->equity_1h` score `-2.4365` n `112` status `ready` deltaP `-9.8695` edge `-0.0432` maxDD `-4.1902`
- `market_context_high->metal_24h` score `-2.5236` n `80` status `ready` deltaP `-14.8264` edge `0.0265` maxDD `-7.0954`
- `market_context_high->fx_24h` score `-2.6104` n `80` status `ready` deltaP `-22.7431` edge `-0.0223` maxDD `-1.8596`
- `market_context_high->equity_24h` score `-3.4054` n `80` status `ready` deltaP `6.1806` edge `-0.2167` maxDD `-16.2208`
- `market_context_high->crypto_alt_4h` score `-5.5524` n `108` status `ready` deltaP `-7.2662` edge `-0.0461` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
