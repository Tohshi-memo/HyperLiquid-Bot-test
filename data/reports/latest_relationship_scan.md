# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T18:07:42.262096+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9882`

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

- `market_context_high->unknown_1h` score `82.5091` n `47` status `ready` deltaP `9.8166` edge `6.8174` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `32.2142` n `46` status `ready` deltaP `18.048` edge `2.5798` maxDD `-0.5817`
- `market_context_high->equity_24h` score `18.2148` n `46` status `ready` deltaP `15.4439` edge `1.425` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.8297` n `46` status `ready` deltaP `13.0208` edge `1.149` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `7.5206` n `96` status `ready` deltaP `-4.6875` edge `1.3438` maxDD `-46.1999`
- `market_context_high->index_24h` score `6.1696` n `46` status `ready` deltaP `24.4716` edge `0.3597` maxDD `-0.03`
- `news_risk_high->crypto_major_4h` score `4.3066` n `103` status `ready` deltaP `16.5182` edge `0.3065` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `3.8421` n `103` status `ready` deltaP `11.3353` edge `0.3444` maxDD `-5.9838`
- `news_risk_high->commodity_24h` score `3.0379` n `96` status `ready` deltaP `27.9514` edge `0.1847` maxDD `-2.431`
- `news_risk_high->crypto_alt_1h` score `2.2848` n `103` status `ready` deltaP `12.1098` edge `0.1587` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.2561` n `47` status `ready` deltaP `27.1666` edge `0.0223` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `1.9773` n `103` status `ready` deltaP `15.5529` edge `0.1046` maxDD `-1.8141`
- `news_risk_high->crypto_alt_24h` score `1.9387` n `96` status `ready` deltaP `-6.7709` edge `0.6948` maxDD `-32.7147`
- `news_risk_high->fx_4h` score `1.3371` n `103` status `ready` deltaP `20.3277` edge `0.0395` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.181` n `96` status `ready` deltaP `28.2986` edge `0.1217` maxDD `-1.7159`
- `market_context_high->equity_4h` score `0.7886` n `47` status `ready` deltaP `7.9981` edge `0.0542` maxDD `-1.3444`
- `market_context_high->metal_24h` score `0.732` n `46` status `ready` deltaP `18.4481` edge `-0.0386` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.6756` n `47` status `ready` deltaP `11.4664` edge `0.0077` maxDD `-0.2275`
- `news_risk_high->metal_1h` score `0.605` n `103` status `ready` deltaP `14.9032` edge `0.0104` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.3745` n `47` status `ready` deltaP `7.1251` edge `0.024` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
