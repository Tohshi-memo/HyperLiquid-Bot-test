# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T05:52:28.225264+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9326`

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

- `market_context_high->unknown_4h` score `34.6309` n `58` status `ready` deltaP `1.23` edge `2.8927` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.1626` n `98` status `ready` deltaP `11.9225` edge `2.6199` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `18.8431` n `98` status `ready` deltaP `12.4894` edge `1.9751` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.589` n `101` status `ready` deltaP `20.1385` edge `0.3691` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0275` n `101` status `ready` deltaP `21.5105` edge `0.318` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.8001` n `101` status `ready` deltaP `16.6805` edge `0.1687` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.148` n `101` status `ready` deltaP `18.3272` edge `0.1091` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.2049` n `98` status `ready` deltaP `23.4694` edge `0.1286` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0788` n `58` status `ready` deltaP `8.1045` edge `0.0612` maxDD `-0.36`
- `market_context_high->index_1h` score `0.855` n `58` status `ready` deltaP `12.2238` edge `0.0153` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6353` n `101` status `ready` deltaP `14.7477` edge `0.0148` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.4197` n `58` status `ready` deltaP `16.1533` edge `0.0098` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.4044` n `101` status `ready` deltaP `15.422` edge `0.0363` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3573` n `58` status `ready` deltaP `6.2978` edge `0.0186` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3067` n `58` status `ready` deltaP `8.3265` edge `0.0057` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1663` n `101` status `ready` deltaP `8.1834` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.0039` n `101` status `ready` deltaP `3.7173` edge `0.0161` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.137` n `58` status `ready` deltaP `-1.4918` edge `0.0704` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2424` n `101` status `ready` deltaP `2.6931` edge `0.0062` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3201` n `98` status `ready` deltaP `10.1226` edge `-0.0241` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
