# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T11:37:27.310873+00:00`
- Price records: `672`
- Market context records: `5450`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->crypto_major_24h` score `3.3071` n `188` status `ready` deltaP `17.3279` edge `0.6141` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.0248` n `197` status `ready` deltaP `15.5874` edge `0.3774` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.5299` n `197` status `ready` deltaP `12.688` edge `0.2901` maxDD `-7.4425`
- `market_context_high->equity_24h` score `2.3167` n `188` status `ready` deltaP `10.5497` edge `0.5605` maxDD `-27.3552`
- `market_context_high->crypto_alt_4h` score `2.2967` n `197` status `ready` deltaP `10.6607` edge `0.2844` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5111` n `199` status `ready` deltaP `8.1628` edge `0.0847` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2323` n `188` status `ready` deltaP `11.1443` edge `0.0346` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.157` n `199` status `ready` deltaP `6.7839` edge `0.0172` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.2689` n `199` status `ready` deltaP `3.9614` edge `0.0187` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.3285` n `199` status `ready` deltaP `0.9569` edge `0.0624` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.4411` n `199` status `ready` deltaP `2.1439` edge `0.0735` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5908` n `199` status `ready` deltaP `-0.0376` edge `-0.0001` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.8105` n `197` status `ready` deltaP `7.6181` edge `0.0426` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1157` n `197` status `ready` deltaP `0.9061` edge `0.0035` maxDD `-1.5345`
- `market_context_high->index_24h` score `-1.1548` n `188` status `ready` deltaP `15.0155` edge `0.0844` maxDD `-14.2714`
- `market_context_high->commodity_1h` score `-1.3984` n `199` status `ready` deltaP `-2.4215` edge `-0.0056` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6159` n `197` status `ready` deltaP `-7.9671` edge `-0.0298` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.3398` n `197` status `ready` deltaP `-6.691` edge `-0.0456` maxDD `-14.3822`
- `market_context_high->metal_24h` score `-7.3487` n `188` status `ready` deltaP `-4.8426` edge `-0.1721` maxDD `-33.021`
- `market_context_high->crypto_alt_24h` score `-7.401` n `188` status `ready` deltaP `8.2299` edge `0.1981` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
