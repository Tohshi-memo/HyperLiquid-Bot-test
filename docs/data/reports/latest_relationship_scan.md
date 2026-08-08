# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T17:37:25.862210+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11590`

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

- `market_context_high->equity_24h` score `2.9856` n `103` status `ready` deltaP `4.5729` edge `0.5243` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3599` n `103` status `ready` deltaP `12.0382` edge `0.174` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4946` n `103` status `ready` deltaP `14.2863` edge `0.0966` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0719` n `105` status `ready` deltaP `12.408` edge `0.0409` maxDD `-0.7439`
- `market_context_high->fx_24h` score `1.0398` n `103` status `ready` deltaP `24.7` edge `0.0553` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3941` n `103` status `ready` deltaP `9.1002` edge `0.143` maxDD `-5.9181`
- `market_context_high->equity_1h` score `-0.5202` n `105` status `ready` deltaP `2.8814` edge `0.0203` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.5548` n `105` status `ready` deltaP `-3.8109` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5938` n `105` status `ready` deltaP `0.9253` edge `-0.0061` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6159` n `105` status `ready` deltaP `-3.5529` edge `-0.0057` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6897` n `103` status `ready` deltaP `-2.4909` edge `-0.0113` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8417` n `103` status `ready` deltaP `1.6324` edge `-0.0057` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9201` n `105` status `ready` deltaP `-10.5731` edge `-0.0266` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.1052` n `103` status `ready` deltaP `1.0641` edge `-0.0488` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.4165` n `105` status `ready` deltaP `-7.4294` edge `-0.0522` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-3.19` n `103` status `ready` deltaP `6.9141` edge `-0.0625` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.6946` n `103` status `ready` deltaP `-12.4461` edge `-0.0806` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.3818` n `103` status `ready` deltaP `-11.7985` edge `-0.1213` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0401` n `103` status `ready` deltaP `-14.7111` edge `-0.2328` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
