# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T17:07:23.296831+00:00`
- Price records: `672`
- Market context records: `1758`
- Flow alert records: `6960`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8862`

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

- `market_context_high->metal_24h` score `7.1895` n `167` status `ready` deltaP `27.4087` edge `0.659` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.0808` n `195` status `ready` deltaP `21.3376` edge `0.5411` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5206` n `195` status `ready` deltaP `22.7518` edge `0.4656` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1826` n `167` status `ready` deltaP `19.093` edge `0.3441` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.7273` n `167` status `ready` deltaP `15.2029` edge `0.7413` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `3.1223` n `30` status `ready` deltaP `24.4212` edge `0.1291` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.1119` n `195` status `ready` deltaP `16.7511` edge `0.2571` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.9437` n `167` status `ready` deltaP `17.3923` edge `0.6192` maxDD `-33.1875`
- `market_context_high->unknown_4h` score `2.9348` n `195` status `ready` deltaP `12.7173` edge `0.3869` maxDD `-11.1695`
- `market_context_high->index_4h` score `0.9345` n `195` status `ready` deltaP `12.0106` edge `0.1067` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7942` n `195` status `ready` deltaP `7.4328` edge `0.119` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.7447` n `167` status `ready` deltaP `19.5962` edge `0.79` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2275` n `195` status `ready` deltaP `4.7413` edge `0.0947` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.1036` n `195` status `ready` deltaP `5.2925` edge `0.0542` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.174` n `195` status `ready` deltaP `4.0757` edge `0.0215` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.207` n `195` status `ready` deltaP `12.758` edge `0.1576` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.5091` n `30` status `ready` deltaP `-5.7285` edge `-0.0009` maxDD `-0.0948`
- `market_context_high->metal_1h` score `-0.518` n `195` status `ready` deltaP `5.7255` edge `0.029` maxDD `-6.3532`
- `news_risk_high->unknown_1h` score `-0.5829` n `30` status `ready` deltaP `15.6587` edge `-0.1319` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.5985` n `167` status `ready` deltaP `7.2344` edge `0.0068` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
