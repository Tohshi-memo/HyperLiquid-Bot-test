# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T16:07:32.439707+00:00`
- Price records: `672`
- Market context records: `5367`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `9.857` n `175` status `ready` deltaP `17.1806` edge `0.7199` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.1852` n `175` status `ready` deltaP `22.1885` edge `0.7382` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.2037` n `175` status `ready` deltaP `14.8592` edge `0.7308` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.3666` n `199` status `ready` deltaP `13.0002` edge `0.3398` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.8341` n `199` status `ready` deltaP `9.6182` edge `0.2528` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.2082` n `199` status `ready` deltaP `8.4668` edge `0.2081` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.3744` n `175` status `ready` deltaP `17.3194` edge `0.0961` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.0784` n `205` status `ready` deltaP `5.8135` edge `0.0643` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.017` n `175` status `ready` deltaP `8.6022` edge `0.0336` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1229` n `205` status `ready` deltaP `4.0792` edge `0.0119` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.1237` n `205` status `ready` deltaP `3.7257` edge `0.0894` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.169` n `205` status `ready` deltaP `1.3305` edge `0.0732` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4252` n `205` status `ready` deltaP `-0.6543` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5586` n `205` status `ready` deltaP `1.1808` edge `0.0131` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.9563` n `199` status `ready` deltaP `4.6666` edge `0.023` maxDD `-2.704`
- `market_context_high->fx_4h` score `-1.0625` n `199` status `ready` deltaP `1.827` edge `0.0022` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4891` n `205` status `ready` deltaP `-3.4701` edge `-0.0065` maxDD `-3.5563`
- `market_context_high->unknown_4h` score `-1.5065` n `199` status `ready` deltaP `7.4397` edge `-0.0567` maxDD `-6.1421`
- `market_context_high->metal_4h` score `-2.7637` n `199` status `ready` deltaP `-8.2746` edge `-0.0467` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.5292` n `175` status `ready` deltaP `12.7421` edge `0.3323` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
