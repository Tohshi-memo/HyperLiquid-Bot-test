# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T09:37:26.542641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10695`

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

- `risk_on_high->crypto_major_24h` score `2.1797` n `101` status `ready` deltaP `14.9477` edge `0.9124` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.1797` n `101` status `ready` deltaP `14.9477` edge `0.9124` maxDD `-47.9416`
- `market_context_high->equity_24h` score `0.8358` n `187` status `ready` deltaP `12.3738` edge `0.341` maxDD `-16.9737`
- `risk_on_high->index_1h` score `-0.1006` n `145` status `ready` deltaP `5.2364` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1006` n `145` status `ready` deltaP `5.2364` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1286` n `145` status `ready` deltaP `8.1984` edge `0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1286` n `145` status `ready` deltaP `8.1984` edge `0.0001` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.4084` n `145` status `ready` deltaP `1.943` edge `0.0547` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4084` n `145` status `ready` deltaP `1.943` edge `0.0547` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4478` n `145` status `ready` deltaP `6.3535` edge `-0.0123` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4478` n `145` status `ready` deltaP `6.3535` edge `-0.0123` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5638` n `145` status `ready` deltaP `0.5049` edge `0.0` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5638` n `145` status `ready` deltaP `0.5049` edge `0.0` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7286` n `250` status `ready` deltaP `0.8635` edge `-0.0015` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.7983` n `145` status `ready` deltaP `0.9808` edge `0.0212` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.7983` n `145` status `ready` deltaP `0.9808` edge `0.0212` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9355` n `250` status `ready` deltaP `3.6467` edge `-0.0065` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.05` n `250` status `ready` deltaP `3.3054` edge `0.0009` maxDD `-3.1683`
- `market_context_high->index_4h` score `-1.1794` n `248` status `ready` deltaP `6.2304` edge `0.0009` maxDD `-5.825`
- `risk_on_high->metal_4h` score `-1.2948` n `145` status `ready` deltaP `2.4863` edge `-0.001` maxDD `-5.1925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
