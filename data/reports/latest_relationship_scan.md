# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T18:37:29.273879+00:00`
- Price records: `672`
- Market context records: `5067`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10324`

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

- `market_context_high->unknown_1h` score `12.4832` n `99` status `ready` deltaP `3.7592` edge `1.0653` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.1588` n `97` status `ready` deltaP `20.8731` edge `0.7263` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `6.1992` n `97` status `ready` deltaP `18.4546` edge `0.5155` maxDD `-6.4213`
- `market_context_high->crypto_major_4h` score `5.5514` n `97` status `ready` deltaP `17.0025` edge `0.5077` maxDD `-8.3416`
- `market_context_high->unknown_24h` score `4.1638` n `78` status `ready` deltaP `27.5908` edge `0.1973` maxDD `-1.4072`
- `market_context_high->crypto_major_1h` score `1.0996` n `99` status `ready` deltaP `7.9145` edge `0.1205` maxDD `-3.8637`
- `market_context_high->metal_4h` score `0.9788` n `97` status `ready` deltaP `10.5843` edge `0.1189` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8741` n `99` status `ready` deltaP `8.7734` edge `0.0717` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.7012` n `97` status `ready` deltaP `6.0112` edge `0.1713` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.5034` n `99` status `ready` deltaP `8.1761` edge `0.0371` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.4269` n `99` status `ready` deltaP `6.9407` edge `0.1008` maxDD `-4.7207`
- `market_context_high->index_4h` score `0.0198` n `97` status `ready` deltaP `5.8147` edge `0.039` maxDD `-1.0893`
- `market_context_high->index_1h` score `-0.2226` n `99` status `ready` deltaP `2.9744` edge `0.0127` maxDD `-0.552`
- `market_context_high->fx_24h` score `-0.2358` n `78` status `ready` deltaP `5.8895` edge `0.0067` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.6006` n `99` status `ready` deltaP `0.319` edge `0.0138` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.8431` n `97` status `ready` deltaP `7.2951` edge `0.006` maxDD `-4.9914`
- `market_context_high->fx_4h` score `-0.9432` n `97` status `ready` deltaP `-3.2232` edge `-0.0005` maxDD `-1.2484`
- `market_context_high->fx_1h` score `-1.4644` n `99` status `ready` deltaP `-8.5103` edge `-0.0043` maxDD `-0.5464`
- `market_context_high->metal_24h` score `-3.6949` n `78` status `ready` deltaP `3.0716` edge `0.0513` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-3.7267` n `78` status `ready` deltaP `4.0064` edge `-0.0504` maxDD `-24.3277`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
