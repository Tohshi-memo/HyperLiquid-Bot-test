# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T03:07:30.452269+00:00`
- Price records: `672`
- Market context records: `5414`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11492`

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

- `market_context_high->crypto_major_4h` score `4.0137` n `205` status `ready` deltaP `17.0732` edge `0.4499` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.8724` n `194` status `ready` deltaP `19.414` edge `0.6473` maxDD `-29.6555`
- `market_context_high->crypto_alt_4h` score `3.2034` n `205` status `ready` deltaP `12.5305` edge `0.3475` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.5028` n `205` status `ready` deltaP `12.5` edge `0.2891` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.3985` n `205` status `ready` deltaP `7.6099` edge `0.079` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0999` n `205` status `ready` deltaP `6.3247` edge `0.0155` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `0.0598` n `205` status `ready` deltaP `4.4742` edge `0.0997` maxDD `-6.9639`
- `market_context_high->fx_24h` score `-0.0102` n `194` status `ready` deltaP `8.7271` edge `0.0305` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `-0.0143` n `205` status `ready` deltaP `2.079` edge `0.0811` maxDD `-5.0257`
- `market_context_high->equity_24h` score `-0.3908` n `194` status `ready` deltaP `8.0327` edge `0.4976` maxDD `-40.0306`
- `market_context_high->fx_1h` score `-0.4477` n `205` status `ready` deltaP `-1.1034` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5718` n `205` status `ready` deltaP `1.3305` edge `0.011` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9325` n `205` status `ready` deltaP `6.7073` edge `0.0385` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.2645` n `205` status `ready` deltaP `-0.5183` edge `0.001` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4699` n `205` status `ready` deltaP `-3.1707` edge `-0.0069` maxDD `-3.5563`
- `market_context_high->index_24h` score `-1.6487` n `194` status `ready` deltaP `12.8275` edge `0.0757` maxDD `-12.5551`
- `market_context_high->metal_4h` score `-2.5401` n `205` status `ready` deltaP `-6.5244` edge `-0.0297` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2341` n `205` status `ready` deltaP `-6.6768` edge `-0.0445` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.3399` n `194` status `ready` deltaP `10.678` edge `0.2702` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.0997` n `194` status `ready` deltaP `-4.9435` edge `-0.1395` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
