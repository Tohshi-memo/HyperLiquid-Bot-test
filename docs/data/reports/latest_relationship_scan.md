# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T20:22:36.036349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `5.4266` n `89` status `ready` deltaP `1.2609` edge `0.7498` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5718` n `89` status `ready` deltaP `14.9162` edge `0.2558` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.8066` n `89` status `ready` deltaP `27.3936` edge `0.0602` maxDD `-2.3818`
- `market_context_high->commodity_4h` score `1.4051` n `109` status `ready` deltaP `14.8327` edge `0.0855` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.2922` n `89` status `ready` deltaP `11.234` edge `0.1841` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.8214` n `111` status `ready` deltaP `11.2586` edge `0.0303` maxDD `-0.9524`
- `market_context_high->fx_1h` score `-0.1827` n `111` status `ready` deltaP `5.5538` edge `-0.0027` maxDD `-0.9639`
- `market_context_high->equity_1h` score `-0.2505` n `111` status `ready` deltaP `5.7278` edge `0.0238` maxDD `-4.6286`
- `market_context_high->fx_4h` score `-0.423` n `109` status `ready` deltaP `5.4864` edge `0.0035` maxDD `-1.6928`
- `market_context_high->index_1h` score `-0.5829` n `111` status `ready` deltaP `-1.4875` edge `-0.0039` maxDD `-0.7809`
- `market_context_high->index_4h` score `-0.5849` n `109` status `ready` deltaP `2.1551` edge `-0.0026` maxDD `-1.1743`
- `market_context_high->crypto_alt_1h` score `-0.9008` n `111` status `ready` deltaP `-5.5457` edge `-0.0156` maxDD `-2.3669`
- `market_context_high->metal_1h` score `-0.9648` n `111` status `ready` deltaP `-3.7384` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.0223` n `109` status `ready` deltaP `7.8205` edge `-0.0036` maxDD `-7.6983`
- `market_context_high->metal_4h` score `-1.0966` n `109` status `ready` deltaP `2.1748` edge `-0.005` maxDD `-2.7373`
- `market_context_high->crypto_major_1h` score `-2.3062` n `111` status `ready` deltaP `-7.0562` edge `-0.0455` maxDD `-4.6382`
- `market_context_high->crypto_alt_4h` score `-3.1272` n `109` status `ready` deltaP `-3.9676` edge `-0.0747` maxDD `-6.0893`
- `market_context_high->crypto_major_24h` score `-3.6387` n `89` status `ready` deltaP `5.5348` edge `-0.0907` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.9557` n `89` status `ready` deltaP `-18.2657` edge `-0.1469` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.135` n `109` status `ready` deltaP `-9.1785` edge `-0.1882` maxDD `-18.9491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
