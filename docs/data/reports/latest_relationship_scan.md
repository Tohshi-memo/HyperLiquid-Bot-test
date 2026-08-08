# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T18:52:28.660646+00:00`
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

- `market_context_high->equity_24h` score `2.9544` n `103` status `ready` deltaP `4.5729` edge `0.5217` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.3743` n `103` status `ready` deltaP `12.0382` edge `0.1752` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.508` n `103` status `ready` deltaP `14.4387` edge `0.0967` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9923` n `110` status `ready` deltaP `11.6685` edge `0.0392` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.9884` n `103` status `ready` deltaP `23.8319` edge `0.0545` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4019` n `103` status `ready` deltaP `9.1002` edge `0.144` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5292` n `110` status `ready` deltaP `1.6576` edge `-0.0056` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5416` n `110` status `ready` deltaP `-3.571` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.6024` n `110` status `ready` deltaP `2.2592` edge `0.0176` maxDD `-4.6286`
- `market_context_high->metal_1h` score `-0.6041` n `110` status `ready` deltaP `-3.2498` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.715` n `103` status `ready` deltaP `-2.9482` edge `-0.0115` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.8039` n `103` status `ready` deltaP `2.0897` edge `-0.0056` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0304` n `103` status `ready` deltaP `-2.7631` edge `-0.0128` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0328` n `110` status `ready` deltaP `-11.7419` edge `-0.0282` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.1962` n `103` status `ready` deltaP `0.3019` edge `-0.0513` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.5482` n `110` status `ready` deltaP `-8.1491` edge `-0.0555` maxDD `-4.8686`
- `market_context_high->crypto_major_24h` score `-3.3893` n `103` status `ready` deltaP `6.5669` edge `-0.0768` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.8506` n `103` status `ready` deltaP `-12.4461` edge `-0.0936` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.4966` n `103` status `ready` deltaP `-12.4083` edge `-0.1268` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-8.0447` n `103` status `ready` deltaP `-14.5587` edge `-0.2342` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
