# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T22:54:53.729977+00:00`
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

- `market_context_high->unknown_24h` score `117.4769` n `82` status `ready` deltaP `-29.0566` edge `15.5232` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `5.8561` n `82` status `ready` deltaP `38.1732` edge `0.2476` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.0187` n `112` status `ready` deltaP `11.9555` edge `0.0523` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.2323` n `116` status `ready` deltaP `1.466` edge `0.012` maxDD `-0.624`
- `market_context_high->metal_4h` score `-0.3136` n `112` status `ready` deltaP `13.9373` edge `0.0076` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.4108` n `116` status `ready` deltaP `0.1136` edge `0.0015` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.4471` n `112` status `ready` deltaP `3.1359` edge `0.0023` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.4825` n `116` status `ready` deltaP `1.9513` edge `-0.0033` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.6258` n `116` status `ready` deltaP `-4.0006` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->crypto_major_4h` score `-0.7264` n `112` status `ready` deltaP `2.5262` edge `-0.0063` maxDD `-3.9599`
- `market_context_high->index_24h` score `-0.9434` n `82` status `ready` deltaP `6.0129` edge `-0.0484` maxDD `-0.9578`
- `market_context_high->index_4h` score `-1.1192` n `112` status `ready` deltaP `-8.6237` edge `-0.0051` maxDD `-0.8045`
- `market_context_high->crypto_major_24h` score `-1.6606` n `82` status `ready` deltaP `-4.1836` edge `0.1124` maxDD `-17.4589`
- `market_context_high->fx_24h` score `-2.1998` n `82` status `ready` deltaP `-17.3823` edge `-0.0054` maxDD `-1.8596`
- `market_context_high->crypto_alt_1h` score `-2.2087` n `116` status `ready` deltaP `-5.1724` edge `-0.0298` maxDD `-5.9152`
- `market_context_high->crypto_major_1h` score `-2.2311` n `116` status `ready` deltaP `-6.0345` edge `-0.0346` maxDD `-4.8879`
- `market_context_high->metal_24h` score `-2.2955` n `82` status `ready` deltaP `-13.5459` edge `0.0472` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-2.4572` n `116` status `ready` deltaP `-9.9576` edge `-0.0431` maxDD `-4.289`
- `market_context_high->crypto_alt_4h` score `-5.5326` n `112` status `ready` deltaP `-7.2735` edge `-0.0444` maxDD `-16.786`
- `market_context_high->equity_24h` score `-5.9739` n `82` status `ready` deltaP `0.4234` edge `-0.3512` maxDD `-26.7341`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
