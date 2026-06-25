# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T03:52:29.042171+00:00`
- Price records: `672`
- Market context records: `4687`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9744`

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

- `market_context_high->unknown_1h` score `78.7142` n `135` status `ready` deltaP `12.026` edge `6.5211` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1556` n `135` status `ready` deltaP `10.9169` edge `0.4779` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8667` n `135` status `ready` deltaP `10.7987` edge `0.1759` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.4967` n `135` status `ready` deltaP `1.9062` edge `0.0255` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7812` n `135` status `ready` deltaP `3.7692` edge `-0.013` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.8796` n `135` status `ready` deltaP `-3.0417` edge `0.0062` maxDD `-5.5624`
- `market_context_high->fx_4h` score `-0.9441` n `135` status `ready` deltaP `-1.6351` edge `-0.0019` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-1.0346` n `135` status `ready` deltaP `-3.8933` edge `-0.0048` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.2526` n `135` status `ready` deltaP `5.2462` edge `0.0152` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.2796` n `135` status `ready` deltaP `1.0897` edge `0.0056` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.8139` n `135` status `ready` deltaP `-5.5866` edge `-0.0135` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.8676` n `135` status `ready` deltaP `-4.4766` edge `-0.081` maxDD `-17.2107`
- `market_context_high->fx_24h` score `-4.6592` n `135` status `ready` deltaP `-11.8287` edge `-0.0134` maxDD `-5.3476`
- `market_context_high->commodity_24h` score `-4.9632` n `135` status `ready` deltaP `13.4606` edge `0.0471` maxDD `-30.7016`
- `market_context_high->crypto_alt_1h` score `-5.5556` n `135` status `ready` deltaP `-2.301` edge `-0.1189` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7155` n `135` status `ready` deltaP `-5.2562` edge `-0.1493` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3723` n `135` status `ready` deltaP `-10.6366` edge `-0.0893` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-8.6832` n `135` status `ready` deltaP `-3.6168` edge `-0.2234` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-9.2122` n `135` status `ready` deltaP `-1.0061` edge `-0.289` maxDD `-64.494`
- `market_context_high->crypto_major_4h` score `-11.6996` n `135` status `ready` deltaP `-4.0526` edge `-0.3829` maxDD `-81.8692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
