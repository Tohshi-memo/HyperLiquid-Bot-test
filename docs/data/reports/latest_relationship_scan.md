# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T11:22:27.888330+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_24h` score `189.6952` n `56` status `ready` deltaP `-15.5258` edge `15.9478` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.3378` n `85` status `ready` deltaP `-6.8041` edge `3.7149` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.0844` n `56` status `ready` deltaP `34.623` edge `0.5691` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `5.128` n `56` status `ready` deltaP `1.9593` edge `0.9592` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.7174` n `56` status `ready` deltaP `25.9425` edge `0.1269` maxDD `-1.04`
- `market_context_high->fx_4h` score `1.2664` n `85` status `ready` deltaP `18.6298` edge `0.0097` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.3583` n `56` status `ready` deltaP `15.377` edge `0.0193` maxDD `-0.7369`
- `market_context_high->commodity_4h` score `0.282` n `85` status `ready` deltaP `10.2655` edge `0.0084` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1867` n `88` status `ready` deltaP `4.7496` edge `0.009` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0307` n `88` status `ready` deltaP `3.7017` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.5544` n `88` status `ready` deltaP `-0.5988` edge `0.0218` maxDD `-3.7778`
- `market_context_high->metal_1h` score `-0.5559` n `88` status `ready` deltaP `-2.0346` edge `0.0016` maxDD `-0.7443`
- `market_context_high->metal_4h` score `-0.5704` n `85` status `ready` deltaP `-2.4839` edge `0.0157` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `-1.1995` n `88` status `ready` deltaP `-3.5316` edge `0.027` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.3313` n `85` status `ready` deltaP `-5.7317` edge `0.0781` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.3718` n `85` status `ready` deltaP `-12.3529` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.6124` n `88` status `ready` deltaP `-6.7297` edge `-0.0033` maxDD `-0.5627`
- `market_context_high->metal_24h` score `-1.6772` n `56` status `ready` deltaP `-12.5744` edge `0.0173` maxDD `-3.5466`
- `market_context_high->equity_1h` score `-1.682` n `88` status `ready` deltaP `-6.7365` edge `-0.0083` maxDD `-2.2898`
- `market_context_high->unknown_1h` score `-1.7158` n `88` status `ready` deltaP `-8.4989` edge `-0.0527` maxDD `-1.0231`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
