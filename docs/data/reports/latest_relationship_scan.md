# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T15:22:30.876029+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11696`

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

- `market_context_high->commodity_4h` score `0.8288` n `169` status `ready` deltaP `11.6891` edge `0.0626` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7263` n `136` status `ready` deltaP `18.7634` edge `0.0162` maxDD `-1.4613`
- `market_context_high->commodity_1h` score `0.7017` n `173` status `ready` deltaP `9.5211` edge `0.0293` maxDD `-0.7439`
- `market_context_high->equity_24h` score `0.6707` n `136` status `ready` deltaP `3.5962` edge `0.3453` maxDD `-21.0709`
- `market_context_high->fx_4h` score `-0.0265` n `169` status `ready` deltaP `7.4046` edge `0.0084` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.0793` n `173` status `ready` deltaP `5.1296` edge `0.0008` maxDD `-0.613`
- `market_context_high->index_24h` score `-0.3795` n `136` status `ready` deltaP `3.2126` edge `0.1001` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.7482` n `173` status `ready` deltaP `-1.9106` edge `-0.0019` maxDD `-0.8168`
- `market_context_high->metal_1h` score `-0.7772` n `173` status `ready` deltaP `-4.1146` edge `-0.0086` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8017` n `173` status `ready` deltaP `-1.5402` edge `-0.006` maxDD `-4.5876`
- `market_context_high->metal_24h` score `-0.8363` n `136` status `ready` deltaP `0.8653` edge `0.0527` maxDD `-2.9193`
- `market_context_high->index_4h` score `-1.2253` n `169` status `ready` deltaP `-1.8843` edge `-0.0113` maxDD `-1.26`
- `market_context_high->crypto_alt_1h` score `-1.6212` n `173` status `ready` deltaP `-9.5289` edge `-0.0422` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.9894` n `169` status `ready` deltaP `-6.6099` edge `-0.0346` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.2791` n `169` status `ready` deltaP `-11.4059` edge `-0.1327` maxDD `-7.9331`
- `market_context_high->crypto_major_1h` score `-3.6308` n `173` status `ready` deltaP `-10.4981` edge `-0.0592` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-3.7657` n `136` status `ready` deltaP `-0.1172` edge `-0.0636` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.9558` n `169` status `ready` deltaP `-12.15` edge `-0.1504` maxDD `-15.3937`
- `market_context_high->crypto_alt_24h` score `-4.1481` n `136` status `ready` deltaP `-11.5608` edge `-0.1243` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-8.7047` n `136` status `ready` deltaP `-5.3752` edge `-0.2086` maxDD `-52.3908`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
