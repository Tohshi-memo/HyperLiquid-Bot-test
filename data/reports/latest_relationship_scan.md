# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T13:52:28.327714+00:00`
- Price records: `672`
- Market context records: `5357`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11494`

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

- `market_context_high->unknown_24h` score `12.9735` n `166` status `ready` deltaP `18.0869` edge `0.9737` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.2419` n `166` status `ready` deltaP `21.9231` edge `0.7447` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.1139` n `166` status `ready` deltaP `17.0264` edge `0.7922` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.4017` n `194` status `ready` deltaP `13.1836` edge `0.3415` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.021` n `194` status `ready` deltaP `9.7498` edge `0.2675` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.6138` n `194` status `ready` deltaP `9.7875` edge `0.2331` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7386` n `166` status `ready` deltaP `23.4124` edge `0.1021` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.1634` n `166` status `ready` deltaP `9.8478` edge `0.0375` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0175` n `202` status `ready` deltaP `5.8472` edge `0.059` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.0037` n `202` status `ready` deltaP `4.1916` edge `0.0963` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0429` n `202` status `ready` deltaP `1.7964` edge `0.0806` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.1433` n `202` status `ready` deltaP `4.3398` edge `0.0095` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.418` n `194` status `ready` deltaP `5.6119` edge `0.0249` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4464` n `202` status `ready` deltaP `0.7485` edge `0.0053` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.4604` n `202` status `ready` deltaP `-1.3014` edge `-0.0014` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.6755` n `194` status `ready` deltaP `1.9832` edge `0.0031` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2087` n `194` status `ready` deltaP `7.908` edge `-0.0352` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.53` n `202` status `ready` deltaP `-3.9722` edge `-0.0077` maxDD `-3.4655`
- `market_context_high->metal_4h` score `-2.7483` n `194` status `ready` deltaP `-8.4439` edge `-0.0436` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.768` n `166` status `ready` deltaP `11.7951` edge `0.308` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
