# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T08:37:27.680635+00:00`
- Price records: `672`
- Market context records: `7652`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0508` n `146` status `ready` deltaP `6.512` edge `0.011` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1596` n `146` status `ready` deltaP `8.1556` edge `0.0212` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2607` n `146` status `ready` deltaP `1.7554` edge `0.0181` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3967` n `146` status `ready` deltaP `1.5282` edge `-0.004` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.5228` n `146` status `ready` deltaP `5.2265` edge `0.0495` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6582` n `146` status `ready` deltaP `0.7895` edge `0.0149` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.7104` n `146` status `ready` deltaP `1.6066` edge `0.0046` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7119` n `146` status `ready` deltaP `7.84` edge `0.0266` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7675` n `146` status `ready` deltaP `-1.773` edge `-0.0022` maxDD `-0.6615`
- `market_context_high->commodity_24h` score `-0.8307` n `145` status `ready` deltaP `8.8838` edge `0.0299` maxDD `-7.0012`
- `market_context_high->crypto_alt_4h` score `-1.0898` n `146` status `ready` deltaP `2.2824` edge `0.044` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1735` n `146` status `ready` deltaP `9.4366` edge `0.0544` maxDD `-14.4206`
- `market_context_high->equity_24h` score `-1.3739` n `145` status `ready` deltaP `14.5381` edge `0.2175` maxDD `-34.5784`
- `market_context_high->unknown_1h` score `-1.4882` n `146` status `ready` deltaP `-0.8346` edge `-0.0561` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.6687` n `146` status `ready` deltaP `1.1436` edge `0.1928` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7162` n `146` status `ready` deltaP `-2.7376` edge `0.0439` maxDD `-4.6535`
- `market_context_high->unknown_24h` score `-2.2228` n `146` status `ready` deltaP `5.8029` edge `-0.1059` maxDD `-4.775`
- `market_context_high->metal_24h` score `-2.227` n `146` status `ready` deltaP `-3.2772` edge `0.062` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.74` n `146` status `ready` deltaP `-8.1878` edge `-0.0053` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
