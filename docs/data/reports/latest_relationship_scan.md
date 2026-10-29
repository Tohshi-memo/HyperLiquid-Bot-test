# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T12:22:31.429542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1297.8271` n `147` status `ready` deltaP `-2.2499` edge `108.26` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `36.5147` n `147` status `ready` deltaP `5.3219` edge `3.0207` maxDD `-0.3966`
- `market_context_high->index_24h` score `0.8071` n `147` status `ready` deltaP `19.0618` edge `-0.0044` maxDD `-1.7672`
- `market_context_high->fx_1h` score `0.0782` n `147` status `ready` deltaP `6.2447` edge `0.0007` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `-0.0066` n `147` status `ready` deltaP `11.2245` edge `0.0465` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1547` n `147` status `ready` deltaP `7.4158` edge `0.0054` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.1958` n `147` status `ready` deltaP `6.1691` edge `0.0024` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.5141` n `147` status `ready` deltaP `0.9389` edge `0.0093` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.677` n `147` status `ready` deltaP `8.549` edge `-0.0007` maxDD `-4.4472`
- `market_context_high->index_1h` score `-0.7897` n `147` status `ready` deltaP `-4.3138` edge `-0.0042` maxDD `-1.4631`
- `market_context_high->crypto_major_1h` score `-0.8398` n `147` status `ready` deltaP `4.6529` edge `0.0273` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-1.3221` n `147` status `ready` deltaP `4.2482` edge `0.0091` maxDD `-1.141`
- `market_context_high->equity_1h` score `-1.4419` n `147` status `ready` deltaP `-0.0407` edge `0.0003` maxDD `-8.7915`
- `market_context_high->crypto_alt_1h` score `-1.6638` n `147` status `ready` deltaP `1.5795` edge `0.0091` maxDD `-11.9687`
- `market_context_high->index_4h` score `-3.0962` n `147` status `ready` deltaP `-10.5307` edge `-0.0327` maxDD `-5.4089`
- `market_context_high->crypto_major_4h` score `-3.5247` n `147` status `ready` deltaP `1.7483` edge `-0.0335` maxDD `-27.0697`
- `market_context_high->crypto_major_24h` score `-3.6814` n `147` status `ready` deltaP `-2.4234` edge `0.0299` maxDD `-29.1905`
- `market_context_high->metal_24h` score `-3.773` n `147` status `ready` deltaP `0.0319` edge `-0.0166` maxDD `-10.5088`
- `market_context_high->equity_4h` score `-5.0608` n `147` status `ready` deltaP `-4.82` edge `-0.1427` maxDD `-31.2527`
- `market_context_high->equity_24h` score `-5.3313` n `147` status `ready` deltaP `2.7353` edge `-0.1868` maxDD `-14.0571`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
