# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T14:52:26.281590+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11348`

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

- `news_risk_high->unknown_24h` score `46.97` n `59` status `ready` deltaP `12.1764` edge `3.9133` maxDD `-3.4247`
- `news_risk_high->crypto_alt_24h` score `21.8806` n `59` status `ready` deltaP `33.6128` edge `1.8847` maxDD `-19.1657`
- `market_context_high->unknown_24h` score `8.4067` n `104` status `ready` deltaP `19.7383` edge `0.6422` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3799` n `80` status `ready` deltaP `11.5854` edge `0.5134` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.4547` n `104` status `ready` deltaP `32.3317` edge `0.2576` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.6104` n `80` status `ready` deltaP `5.2246` edge `0.2184` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.4802` n `80` status `ready` deltaP `35.8841` edge `0.0224` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.3842` n `116` status `ready` deltaP `17.6199` edge `0.1244` maxDD `-0.788`
- `news_risk_high->equity_24h` score `1.8828` n `59` status `ready` deltaP `21.8808` edge `0.3349` maxDD `-16.1513`
- `news_risk_high->metal_24h` score `1.1843` n `59` status `ready` deltaP `34.6133` edge `0.029` maxDD `-5.6339`
- `news_risk_high->crypto_major_24h` score `1.1267` n `59` status `ready` deltaP `18.235` edge `0.3398` maxDD `-21.6871`
- `market_context_high->unknown_1h` score `1.1207` n `128` status `ready` deltaP `9.5996` edge `0.0775` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7483` n `80` status `ready` deltaP `14.3413` edge `0.0056` maxDD `-0.108`
- `news_risk_high->index_24h` score `0.5905` n `59` status `ready` deltaP `17.9791` edge `0.018` maxDD `-1.6386`
- `news_risk_high->commodity_1h` score `0.3995` n `80` status `ready` deltaP `11.7515` edge `0.0049` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.1087` n `116` status `ready` deltaP `18.3032` edge `0.214` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.3008` n `116` status `ready` deltaP `6.7284` edge `0.0083` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->crypto_alt_4h` score `-0.4722` n `116` status `ready` deltaP `20.5898` edge `0.308` maxDD `-31.4361`
- `market_context_high->commodity_1h` score `-0.5154` n `128` status `ready` deltaP `-0.7485` edge `0.0083` maxDD `-1.5507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
