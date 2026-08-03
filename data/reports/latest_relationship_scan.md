# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T00:37:22.885815+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `5094.9074` n `60` status `ready` deltaP `23.7152` edge `424.4596` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.8775` n `40` status `ready` deltaP `51.9792` edge `0.933` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.2134` n `40` status `ready` deltaP `51.3194` edge `0.6051` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `4.3396` n `60` status `ready` deltaP `13.7704` edge `0.3462` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5028` n `60` status `ready` deltaP `14.3699` edge `0.0675` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.9564` n `41` status `ready` deltaP `12.6525` edge `0.1229` maxDD `-2.7703`
- `market_context_high->crypto_alt_4h` score `0.6859` n `41` status `ready` deltaP `7.4695` edge `0.1287` maxDD `-4.9116`
- `market_context_high->fx_4h` score `0.5988` n `41` status `ready` deltaP `19.5122` edge `0.0263` maxDD `-1.3685`
- `news_risk_high->equity_1h` score `0.3331` n `60` status `ready` deltaP `7.1757` edge `0.0622` maxDD `-2.916`
- `market_context_high->commodity_1h` score `0.3005` n `46` status `ready` deltaP `6.4436` edge `0.033` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0819` n `46` status `ready` deltaP `7.869` edge `-0.0042` maxDD `-0.6874`
- `news_risk_high->fx_4h` score `-0.0534` n `60` status `ready` deltaP `10.0813` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->fx_1h` score `-0.0598` n `60` status `ready` deltaP `3.014` edge `0.0045` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0768` n `60` status `ready` deltaP `2.6048` edge `0.0051` maxDD `-0.5845`
- `news_risk_high->metal_4h` score `-0.0905` n `60` status `ready` deltaP `3.1707` edge `0.0107` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.1402` n `60` status `ready` deltaP `5.4491` edge `0.0139` maxDD `-3.1233`
- `news_risk_high->metal_1h` score `-0.2824` n `60` status `ready` deltaP `0.4691` edge `0.001` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-0.3548` n `60` status `ready` deltaP `5.4291` edge `-0.0139` maxDD `-2.0891`
- `news_risk_high->crypto_major_1h` score `-0.4753` n `60` status `ready` deltaP `1.0479` edge `0.0041` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.7511` n `40` status `ready` deltaP `0.6597` edge `0.031` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
