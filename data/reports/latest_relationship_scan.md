# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T22:52:24.031259+00:00`
- Price records: `672`
- Market context records: `7298`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13807`

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

- `market_context_high->fx_1h` score `-0.0976` n `126` status `ready` deltaP `5.148` edge `0.0021` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.5177` n `126` status `ready` deltaP `0.1716` edge `-0.0103` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.5373` n `126` status `ready` deltaP `0.1497` edge `0.034` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6325` n `126` status `ready` deltaP `4.0586` edge `0.0329` maxDD `-7.6171`
- `market_context_high->commodity_4h` score `-0.6672` n `123` status `ready` deltaP `3.2259` edge `-0.0102` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.9039` n `119` status `ready` deltaP `0.7965` edge `0.0016` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-0.9141` n `123` status `ready` deltaP `4.438` edge `0.0132` maxDD `-1.4649`
- `market_context_high->unknown_1h` score `-1.2469` n `126` status `ready` deltaP `0.1639` edge `-0.0986` maxDD `-1.3217`
- `market_context_high->index_1h` score `-1.2941` n `126` status `ready` deltaP `-5.2124` edge `-0.0089` maxDD `-2.1355`
- `market_context_high->unknown_4h` score `-1.3054` n `123` status `ready` deltaP `6.1483` edge `0.0861` maxDD `-6.2031`
- `market_context_high->metal_1h` score `-1.3719` n `126` status `ready` deltaP `-9.4502` edge `-0.0025` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.4265` n `123` status `ready` deltaP `-9.0956` edge `-0.0049` maxDD `-4.6441`
- `market_context_high->crypto_major_4h` score `-3.0857` n `123` status `ready` deltaP `1.4736` edge `-0.016` maxDD `-23.4879`
- `market_context_high->commodity_24h` score `-3.2015` n `119` status `ready` deltaP `-6.4538` edge `-0.144` maxDD `-2.3815`
- `market_context_high->crypto_alt_4h` score `-3.314` n `123` status `ready` deltaP `0.9654` edge `-0.0083` maxDD `-15.2776`
- `market_context_high->unknown_24h` score `-3.3634` n `120` status `ready` deltaP `-8.8889` edge `-0.044` maxDD `-14.2357`
- `market_context_high->equity_1h` score `-4.4057` n `126` status `ready` deltaP `-9.1806` edge `-0.0683` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.948` n `123` status `ready` deltaP `-14.7124` edge `-0.0573` maxDD `-10.2226`
- `market_context_high->metal_24h` score `-11.0308` n `120` status `ready` deltaP `-28.7848` edge `-0.1272` maxDD `-21.3444`
- `market_context_high->index_24h` score `-13.066` n `119` status `ready` deltaP `-30.1747` edge `-0.1656` maxDD `-33.7654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
