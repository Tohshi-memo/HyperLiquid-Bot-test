# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T07:22:21.238891+00:00`
- Price records: `625`
- Market context records: `731`
- Flow alert records: `2065`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1009`

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

- `market_context_high->crypto_major_24h` score `12.1481` n `146` status `ready` deltaP `29.2099` edge `0.851` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4469` n `146` status `ready` deltaP `7.8217` edge `0.4899` maxDD `-0.0508`
- `market_context_high->index_24h` score `-0.1778` n `146` status `ready` deltaP `0.2988` edge `0.1827` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.3523` n `149` status `ready` deltaP `5.1561` edge `0.0076` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.4325` n `156` status `ready` deltaP `2.9038` edge `0.0024` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5232` n `156` status `ready` deltaP `2.0477` edge `0.0402` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.9096` n `156` status `ready` deltaP `0.9226` edge `0.0034` maxDD `-2.8282`
- `market_context_high->equity_24h` score `-0.9389` n `146` status `ready` deltaP `-1.4194` edge `0.1917` maxDD `-10.5047`
- `market_context_high->crypto_major_4h` score `-0.9618` n `149` status `ready` deltaP `17.9246` edge `0.1278` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.045` n `156` status `ready` deltaP `-0.6981` edge `-0.0014` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.0818` n `156` status `ready` deltaP `5.5215` edge `-0.0032` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.4674` n `156` status `ready` deltaP `4.0475` edge `-0.0178` maxDD `-8.1842`
- `market_context_high->unknown_1h` score `-1.6081` n `156` status `ready` deltaP `-4.8959` edge `-0.0242` maxDD `-3.5069`
- `market_context_high->index_4h` score `-1.8834` n `149` status `ready` deltaP `0.7832` edge `-0.0099` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.0053` n `149` status `ready` deltaP `3.1606` edge `0.0688` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.8646` n `149` status `ready` deltaP `-2.192` edge `-0.0089` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.2179` n `156` status `ready` deltaP `-4.2797` edge `-0.0437` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.5476` n `149` status `ready` deltaP `-4.9254` edge `0.0873` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.9365` n `149` status `ready` deltaP `4.6164` edge `-0.171` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.2732` n `146` status `ready` deltaP `-14.471` edge `-0.0624` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
