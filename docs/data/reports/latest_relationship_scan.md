# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T15:22:24.848280+00:00`
- Price records: `657`
- Market context records: `768`
- Flow alert records: `2165`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1170`

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

- `market_context_high->crypto_major_24h` score `13.423` n `147` status `ready` deltaP `31.9765` edge `0.9388` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.6905` n `147` status `ready` deltaP `7.3411` edge `0.5134` maxDD `-0.0508`
- `risk_on_high->metal_1h` score `1.3334` n `32` status `ready` deltaP `15.2134` edge `0.0327` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.3334` n `32` status `ready` deltaP `15.2134` edge `0.0327` maxDD `-0.5074`
- `market_context_high->index_24h` score `0.5689` n `147` status `ready` deltaP `3.168` edge `0.2258` maxDD `-5.9609`
- `risk_on_high->fx_1h` score `0.4285` n `32` status `ready` deltaP `10.6173` edge `0.0031` maxDD `-0.1827`
- `risk_on_and_context->fx_1h` score `0.4285` n `32` status `ready` deltaP `10.6173` edge `0.0031` maxDD `-0.1827`
- `risk_on_high->commodity_1h` score `0.1781` n `32` status `ready` deltaP `6.4378` edge `0.0175` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.1781` n `32` status `ready` deltaP `6.4378` edge `0.0175` maxDD `-0.6739`
- `risk_on_high->crypto_major_1h` score `0.1111` n `32` status `ready` deltaP `6.8482` edge `-0.0029` maxDD `-0.948`
- `risk_on_and_context->crypto_major_1h` score `0.1111` n `32` status `ready` deltaP `6.8482` edge `-0.0029` maxDD `-0.948`
- `market_context_high->equity_24h` score `-0.0011` n `147` status `ready` deltaP `1.722` edge `0.2489` maxDD `-10.5047`
- `risk_on_high->index_1h` score `-0.3402` n `32` status `ready` deltaP `-1.3338` edge `0.0089` maxDD `-0.2687`
- `risk_on_and_context->index_1h` score `-0.3402` n `32` status `ready` deltaP `-1.3338` edge `0.0089` maxDD `-0.2687`
- `risk_on_high->crypto_alt_1h` score `-0.3873` n `32` status `ready` deltaP `3.6945` edge `-0.0245` maxDD `-0.9258`
- `risk_on_and_context->crypto_alt_1h` score `-0.3873` n `32` status `ready` deltaP `3.6945` edge `-0.0245` maxDD `-0.9258`
- `market_context_high->fx_4h` score `-0.4404` n `171` status `ready` deltaP `3.5069` edge `0.0073` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.4611` n `183` status `ready` deltaP `2.4931` edge `0.0424` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.5193` n `183` status `ready` deltaP `0.368` edge `0.012` maxDD `-4.4826`
- `market_context_high->fx_1h` score `-0.525` n `183` status `ready` deltaP `1.8229` edge `0.0019` maxDD `-0.291`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
