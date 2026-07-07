# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T02:07:25.425089+00:00`
- Price records: `672`
- Market context records: `5936`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11219`

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

- `news_risk_high->fx_24h` score `6.7239` n `30` status `ready` deltaP `61.4583` edge `0.1506` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.5148` n `30` status `ready` deltaP `39.2709` edge `0.2183` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.5997` n `30` status `ready` deltaP `37.2561` edge `0.0562` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.2951` n `221` status `ready` deltaP `9.6706` edge `0.1529` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8605` n `30` status `ready` deltaP `10.7884` edge `0.0851` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1881` n `30` status `ready` deltaP `5.1697` edge `0.0358` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0808` n `221` status `ready` deltaP `6.2922` edge `0.0397` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.307` n `221` status `ready` deltaP `3.8597` edge `0.002` maxDD `-2.0339`
- `news_risk_high->index_24h` score `-0.3107` n `30` status `ready` deltaP `5.7639` edge `0.0089` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.443` n `30` status `ready` deltaP `1.5369` edge `-0.0304` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5576` n `221` status `ready` deltaP `-2.6452` edge `-0.0023` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5986` n `221` status `ready` deltaP `3.5637` edge `0.0316` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.6807` n `221` status `ready` deltaP `2.8016` edge `0.0275` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.8519` n `221` status `ready` deltaP `1.2877` edge `0.0052` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1318` n `30` status `ready` deltaP `-10.7485` edge `-0.022` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.1952` n `213` status `ready` deltaP `17.1435` edge `0.2401` maxDD `-31.2762`
- `market_context_high->commodity_4h` score `-1.7562` n `221` status `ready` deltaP `-4.9981` edge `-0.0205` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7948` n `221` status `ready` deltaP `-3.7758` edge `-0.0417` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
