# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T16:07:26.529791+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10826`

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

- `market_context_high->equity_24h` score `3.5073` n `104` status `ready` deltaP `3.6992` edge `0.5736` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.2372` n `104` status `ready` deltaP `8.734` edge `0.1858` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.321` n `143` status `ready` deltaP `16.2716` edge `0.0689` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8384` n `143` status `ready` deltaP `11.2904` edge `0.0289` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6456` n `104` status `ready` deltaP `20.4193` edge `0.0333` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.3488` n `104` status `ready` deltaP `5.8894` edge `0.1586` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.396` n `143` status `ready` deltaP `3.0977` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4073` n `143` status `ready` deltaP `-1.2436` edge `-0.005` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5577` n `143` status `ready` deltaP `4.9133` edge `-0.0039` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.69` n `143` status `ready` deltaP `-4.8877` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9098` n `143` status `ready` deltaP `-0.9157` edge `-0.0092` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9229` n `143` status `ready` deltaP `-0.3371` edge `0.0082` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0177` n `143` status `ready` deltaP `-1.8132` edge `-0.0175` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0067` n `143` status `ready` deltaP `-10.8821` edge `-0.0305` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5558` n `143` status `ready` deltaP `-1.4188` edge `-0.0698` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2957` n `143` status `ready` deltaP `-11.885` edge `-0.0632` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.9091` n `143` status `ready` deltaP `-8.5814` edge `-0.1029` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1937` n `104` status `ready` deltaP `1.2821` edge `-0.1086` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.5731` n `104` status `ready` deltaP `-18.3226` edge `-0.2813` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8185` n `143` status `ready` deltaP `-6.0938` edge `-0.5662` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
