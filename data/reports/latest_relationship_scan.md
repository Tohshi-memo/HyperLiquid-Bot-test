# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T02:37:28.558687+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5368`

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

- `market_context_high->unknown_1h` score `122.7553` n `97` status `ready` deltaP `-1.4738` edge `10.2809` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.7832` n `95` status `ready` deltaP `2.4743` edge `5.9966` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.9623` n `54` status `ready` deltaP `30.3819` edge `0.7246` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.9353` n `54` status `ready` deltaP `25.2314` edge `0.7217` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.4104` n `65` status `ready` deltaP `32.704` edge `0.5865` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2878` n `65` status `ready` deltaP `20.5488` edge `0.5214` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.5481` n `65` status `ready` deltaP `16.0684` edge `0.2819` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.3032` n `95` status `ready` deltaP `18.291` edge `0.307` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.422` n `65` status `ready` deltaP `23.7847` edge `0.1266` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8901` n `65` status `ready` deltaP `31.7613` edge `0.0553` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.842` n `65` status `ready` deltaP `21.1867` edge `0.1566` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.542` n `65` status `ready` deltaP `10.3155` edge `0.1786` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.2181` n `97` status `ready` deltaP `15.2957` edge `0.1279` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.071` n `65` status `ready` deltaP `25.6172` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `2.0639` n `65` status `ready` deltaP `18.9259` edge `0.0874` maxDD `-0.993`
- `market_context_high->fx_24h` score `1.8219` n `54` status `ready` deltaP `22.2223` edge `0.0958` maxDD `-1.703`
- `market_context_high->equity_24h` score `1.6134` n `54` status `ready` deltaP `3.7037` edge `0.13` maxDD `-0.6196`
- `market_context_high->fx_4h` score `1.4563` n `95` status `ready` deltaP `25.3242` edge `0.0282` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.3208` n `65` status `ready` deltaP `4.1202` edge `0.1345` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.1676` n `95` status `ready` deltaP `3.7067` edge `0.2515` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
