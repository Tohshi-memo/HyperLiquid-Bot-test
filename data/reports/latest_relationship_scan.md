# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T02:37:24.882382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->commodity_24h` score `4.0261` n `71` status `ready` deltaP `34.1989` edge `0.1424` maxDD `-0.4576`
- `market_context_high->index_24h` score `1.2977` n `71` status `ready` deltaP `20.4665` edge `-0.0241` maxDD `-0.0026`
- `market_context_high->commodity_4h` score `1.2225` n `101` status `ready` deltaP `13.6682` edge `0.0579` maxDD `-0.7718`
- `market_context_high->crypto_major_24h` score `1.1448` n `71` status `ready` deltaP `1.5919` edge `0.2354` maxDD `-6.7154`
- `market_context_high->equity_24h` score `0.6338` n `71` status `ready` deltaP `14.6005` edge `0.0125` maxDD `-2.8946`
- `market_context_high->commodity_1h` score `-0.2397` n `108` status `ready` deltaP `0.3826` edge `0.0113` maxDD `-0.8998`
- `market_context_high->metal_4h` score `-0.335` n `101` status `ready` deltaP `15.4205` edge `0.01` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.4614` n `108` status `ready` deltaP `-2.9275` edge `-0.0026` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.5449` n `108` status `ready` deltaP `3.6095` edge `0.0021` maxDD `-1.7257`
- `market_context_high->fx_4h` score `-0.6338` n `101` status `ready` deltaP `-2.1734` edge `-0.0063` maxDD `-0.504`
- `market_context_high->index_1h` score `-1.0669` n `108` status `ready` deltaP `-5.2118` edge `-0.002` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.2687` n `108` status `ready` deltaP `-6.9804` edge `-0.033` maxDD `-3.3165`
- `market_context_high->crypto_major_4h` score `-1.4878` n `101` status `ready` deltaP `1.6375` edge `-0.0141` maxDD `-4.6638`
- `market_context_high->crypto_alt_1h` score `-1.9463` n `108` status `ready` deltaP `-6.0047` edge `-0.0212` maxDD `-4.4101`
- `market_context_high->index_4h` score `-1.9825` n `101` status `ready` deltaP `-11.8526` edge `-0.0053` maxDD `-0.8045`
- `market_context_high->crypto_major_1h` score `-2.0283` n `108` status `ready` deltaP `-6.0047` edge `-0.0286` maxDD `-4.0312`
- `market_context_high->fx_24h` score `-3.0745` n `71` status `ready` deltaP `-29.1031` edge `-0.0394` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-5.166` n `71` status `ready` deltaP `-21.4813` edge `-0.0361` maxDD `-7.0954`
- `market_context_high->equity_4h` score `-5.5467` n `101` status `ready` deltaP `-19.7748` edge `-0.1497` maxDD `-8.1221`
- `market_context_high->crypto_alt_4h` score `-5.919` n `101` status `ready` deltaP `-9.3289` edge `-0.0629` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
