# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T02:37:30.514977+00:00`
- Price records: `672`
- Market context records: `5938`
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

- `news_risk_high->fx_24h` score `6.7287` n `30` status `ready` deltaP `61.4583` edge `0.151` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.5052` n `30` status `ready` deltaP `39.2709` edge `0.2175` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.6265` n `30` status `ready` deltaP `37.561` edge `0.0564` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1016` n `30` status `ready` deltaP `25.4291` edge `0.0195` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3735` n `221` status `ready` deltaP `9.9755` edge `0.1574` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8816` n `30` status `ready` deltaP `10.9381` edge `0.0868` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2138` n `30` status `ready` deltaP `5.4691` edge `0.0371` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0777` n `221` status `ready` deltaP `6.2922` edge `0.0401` maxDD `-4.3608`
- `news_risk_high->index_24h` score `-0.2879` n `30` status `ready` deltaP `6.1111` edge `0.0095` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3062` n `221` status `ready` deltaP `3.8597` edge `0.0021` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4422` n `30` status `ready` deltaP `1.5369` edge `-0.0303` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5592` n `221` status `ready` deltaP `-2.6452` edge `-0.0025` maxDD `-1.4578`
- `market_context_high->crypto_major_1h` score `-0.5776` n `221` status `ready` deltaP `3.7134` edge `0.0333` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-0.655` n `221` status `ready` deltaP `3.101` edge `0.0288` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.6985` n `221` status `ready` deltaP `-1.2979` edge `-0.0007` maxDD `-0.5751`
- `market_context_high->index_1h` score `-0.8243` n `221` status `ready` deltaP `1.5871` edge `0.0055` maxDD `-0.7819`
- `news_risk_high->index_1h` score `-1.1139` n `30` status `ready` deltaP `-10.4491` edge `-0.0217` maxDD `-1.1161`
- `market_context_high->equity_24h` score `-1.142` n `213` status `ready` deltaP `17.4907` edge `0.2446` maxDD `-31.2762`
- `market_context_high->metal_4h` score `-1.7594` n `221` status `ready` deltaP `-3.4709` edge `-0.0392` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.7697` n `221` status `ready` deltaP `0.7877` edge `0.016` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
