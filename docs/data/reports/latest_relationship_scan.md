# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T09:52:25.624213+00:00`
- Price records: `672`
- Market context records: `7016`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2808` n `227` status `ready` deltaP `1.7258` edge `0.001` maxDD `-0.5468`
- `market_context_high->unknown_24h` score `-0.444` n `214` status `ready` deltaP `-5.9271` edge `0.4376` maxDD `-18.7342`
- `market_context_high->crypto_alt_1h` score `-0.5681` n `227` status `ready` deltaP `1.499` edge `0.0291` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.66` n `227` status `ready` deltaP `-1.2807` edge `0.0007` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.6694` n `227` status `ready` deltaP `0.6139` edge `0.0012` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-1.0413` n `227` status `ready` deltaP `10.0617` edge `0.0058` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.0767` n `227` status `ready` deltaP `3.1371` edge `0.0246` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.2429` n `227` status `ready` deltaP `-2.2989` edge `-0.0161` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.2625` n `227` status `ready` deltaP `-1.7555` edge `-0.0034` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.7089` n `227` status `ready` deltaP `-4.6577` edge `-0.0393` maxDD `-5.5657`
- `market_context_high->index_4h` score `-1.7836` n `227` status `ready` deltaP `7.7751` edge `-0.0106` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8417` n `227` status `ready` deltaP `3.6891` edge `-0.0053` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8871` n `227` status `ready` deltaP `6.8229` edge `0.0109` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.4444` n `227` status `ready` deltaP `-6.0029` edge `0.0708` maxDD `-10.0921`
- `market_context_high->crypto_alt_4h` score `-2.7189` n `227` status `ready` deltaP `1.5237` edge `0.0198` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.9778` n `214` status `ready` deltaP `-4.41` edge `-0.0837` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.1763` n `214` status `ready` deltaP `-5.6204` edge `-0.0154` maxDD `-4.9456`
- `market_context_high->crypto_major_4h` score `-4.8732` n `227` status `ready` deltaP `1.6426` edge `0.0114` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-11.4296` n `227` status `ready` deltaP `4.7921` edge `-0.0627` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.3999` n `214` status `ready` deltaP `-9.7693` edge `-0.0546` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
