# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T05:22:31.357732+00:00`
- Price records: `672`
- Market context records: `5423`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11474`

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

- `market_context_high->crypto_major_24h` score `4.3955` n `188` status `ready` deltaP `20.0724` edge `0.6865` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.9147` n `188` status `ready` deltaP `10.5497` edge `0.6095` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.834` n `199` status `ready` deltaP `16.5967` edge `0.4381` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9962` n `199` status `ready` deltaP `11.9952` edge `0.3338` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.55` n `199` status `ready` deltaP `12.4303` edge `0.2935` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.4085` n `199` status `ready` deltaP `7.6603` edge `0.0795` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0826` n `199` status `ready` deltaP `6.0783` edge `0.0157` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.0527` n `188` status `ready` deltaP `9.0943` edge `0.0333` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `-0.2193` n `199` status `ready` deltaP `3.4912` edge `0.083` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.2802` n `199` status `ready` deltaP `1.096` edge `0.0655` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.4656` n `199` status `ready` deltaP `2.2079` edge `0.014` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.58` n `199` status `ready` deltaP `0.1121` edge `-0.0002` maxDD `-0.577`
- `market_context_high->index_4h` score `-1.0065` n `199` status `ready` deltaP `5.8126` edge `0.0383` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1308` n `199` status `ready` deltaP `0.9124` edge `0.0022` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.2732` n `188` status `ready` deltaP `15.0155` edge `0.0924` maxDD `-12.5551`
- `market_context_high->commodity_1h` score `-1.4787` n `199` status `ready` deltaP `-3.2663` edge `-0.007` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.6905` n `199` status `ready` deltaP `-8.427` edge `-0.0363` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3267` n `199` status `ready` deltaP `-7.3546` edge `-0.0477` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-6.0666` n `188` status `ready` deltaP `10.9745` edge `0.291` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2278` n `188` status `ready` deltaP `-4.8426` edge `-0.1566` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
