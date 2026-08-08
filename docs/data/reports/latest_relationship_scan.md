# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T01:22:25.674228+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `7.3667` n `81` status `ready` deltaP `5.2469` edge `0.8849` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7926` n `81` status `ready` deltaP `12.4421` edge `0.2907` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7225` n `81` status `ready` deltaP `33.6034` edge `0.0668` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.7105` n `103` status `ready` deltaP `17.0302` edge `0.0963` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.4606` n `81` status `ready` deltaP `9.7993` edge `0.2077` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.1135` n `103` status `ready` deltaP `13.3335` edge `0.0382` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.2315` n `103` status `ready` deltaP `5.6945` edge `0.0256` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4695` n `103` status `ready` deltaP `-2.885` edge `-0.0062` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4818` n `103` status `ready` deltaP `2.2048` edge `-0.0053` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5954` n `103` status `ready` deltaP `-0.814` edge `-0.0104` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6078` n `103` status `ready` deltaP `-3.4111` edge `-0.0056` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8847` n `103` status `ready` deltaP `0.8702` edge `-0.0042` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-0.9782` n `103` status `ready` deltaP `-1.8485` edge `-0.0122` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.6738` n `103` status `ready` deltaP `-8.1841` edge `-0.022` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-1.7031` n `103` status `ready` deltaP `3.9605` edge `-0.0346` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-1.9196` n `81` status `ready` deltaP `11.2076` edge `-0.0714` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1797` n `103` status `ready` deltaP `-5.4895` edge `-0.0454` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.566` n `81` status `ready` deltaP `-21.4313` edge `-0.17` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.7165` n `103` status `ready` deltaP `-7.6827` edge `-0.0933` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.1281` n `103` status `ready` deltaP `-9.0709` edge `-0.1944` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
