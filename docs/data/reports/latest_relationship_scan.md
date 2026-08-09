# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T12:52:26.685806+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.8508` n `103` status `ready` deltaP `4.5729` edge `0.5964` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4991` n `103` status `ready` deltaP `10.8229` edge `0.1937` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1146` n `143` status `ready` deltaP `14.4423` edge `0.0639` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7785` n `143` status `ready` deltaP `10.6916` edge `0.0279` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7255` n `103` status `ready` deltaP `21.4013` edge `0.037` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4924` n `103` status `ready` deltaP `7.8849` edge `0.1637` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.3505` n `143` status `ready` deltaP `-0.1957` edge `-0.0047` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.3588` n `143` status `ready` deltaP `3.5468` edge `-0.004` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.5443` n `143` status `ready` deltaP `5.0657` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6402` n `143` status `ready` deltaP `-3.9895` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7467` n `143` status `ready` deltaP `0.9136` edge `-0.0078` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8833` n `143` status `ready` deltaP `0.1121` edge `0.0085` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9575` n `143` status `ready` deltaP `-0.7462` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8293` n `143` status `ready` deltaP `-9.5348` edge `-0.0247` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3363` n `143` status `ready` deltaP `0.4105` edge `-0.0637` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0872` n `143` status `ready` deltaP `-10.2383` edge `-0.0568` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5597` n `143` status `ready` deltaP `-6.5997` edge `-0.087` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.8094` n `103` status `ready` deltaP `2.9211` edge `-0.0875` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.9124` n `103` status `ready` deltaP `-16.4392` edge `-0.2388` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7502` n `143` status `ready` deltaP `-5.3453` edge `-0.5655` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
