# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T13:52:29.641322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7286`

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

- `market_context_high->unknown_24h` score `837.7565` n `46` status `ready` deltaP `-16.1835` edge `69.9573` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `49.0537` n `78` status `ready` deltaP `-8.8102` edge `4.2046` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9357` n `46` status `ready` deltaP `31.1292` edge `0.58` maxDD `-1.0977`
- `market_context_high->index_24h` score `4.8038` n `46` status `ready` deltaP `40.4287` edge `0.1593` maxDD `-0.2807`
- `market_context_high->crypto_major_24h` score `2.8705` n `46` status `ready` deltaP `-10.7186` edge `0.7543` maxDD `-17.8526`
- `market_context_high->fx_24h` score `2.269` n `46` status `ready` deltaP `28.0042` edge `0.0309` maxDD `-0.2809`
- `market_context_high->fx_4h` score `1.0758` n `78` status `ready` deltaP `16.3071` edge `0.0093` maxDD `-0.2692`
- `market_context_high->unknown_1h` score `0.277` n `83` status `ready` deltaP `-4.9347` edge `0.0896` maxDD `-1.0231`
- `market_context_high->commodity_4h` score `0.2681` n `78` status `ready` deltaP `9.717` edge `0.0109` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2219` n `83` status `ready` deltaP `5.1439` edge `0.0093` maxDD `-0.3417`
- `market_context_high->fx_1h` score `-0.3245` n `83` status `ready` deltaP `-0.5735` edge `0.001` maxDD `-0.271`
- `market_context_high->crypto_alt_1h` score `-0.4511` n `83` status `ready` deltaP `2.884` edge `0.0466` maxDD `-4.9401`
- `market_context_high->metal_4h` score `-0.559` n `78` status `ready` deltaP `-2.5641` edge `0.0177` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.5735` n `83` status `ready` deltaP `1.3653` edge `0.0022` maxDD `-0.7275`
- `market_context_high->crypto_major_1h` score `-1.0588` n `83` status `ready` deltaP `-2.406` edge `0.0167` maxDD `-3.7778`
- `market_context_high->index_4h` score `-1.1865` n `78` status `ready` deltaP `-11.9958` edge `-0.0004` maxDD `-1.0724`
- `market_context_high->index_1h` score `-1.2028` n `83` status `ready` deltaP `-9.6349` edge `-0.0038` maxDD `-0.5603`
- `market_context_high->equity_1h` score `-1.2445` n `83` status `ready` deltaP `-9.5988` edge `-0.0086` maxDD `-2.2898`
- `market_context_high->crypto_major_4h` score `-1.2862` n `78` status `ready` deltaP `-5.3159` edge `0.0811` maxDD `-11.1784`
- `market_context_high->crypto_alt_4h` score `-2.0199` n `78` status `ready` deltaP `-8.2669` edge `0.052` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
