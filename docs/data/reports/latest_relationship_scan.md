# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T06:07:25.331268+00:00`
- Price records: `672`
- Market context records: `2942`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `16.4574` n `139` status `ready` deltaP `15.6637` edge `1.6587` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.899` n `139` status `ready` deltaP `18.3479` edge `0.7363` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.032` n `139` status `ready` deltaP `16.3907` edge `0.5232` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.8333` n `139` status `ready` deltaP `13.8576` edge `0.2418` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `2.4078` n `139` status `ready` deltaP `16.8827` edge `0.3737` maxDD `-11.5146`
- `market_context_high->equity_4h` score `0.9569` n `140` status `ready` deltaP `8.6542` edge `0.154` maxDD `-5.5563`
- `market_context_high->index_4h` score `0.7484` n `140` status `ready` deltaP `15.1045` edge `0.0794` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.2196` n `140` status `ready` deltaP `4.1899` edge `0.0957` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.1063` n `140` status `ready` deltaP `16.0888` edge `0.3619` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.017` n `140` status `ready` deltaP `4.9316` edge `0.0187` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.452` n `140` status `ready` deltaP `0.3935` edge `0.043` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4813` n `140` status `ready` deltaP `5.4149` edge `0.0782` maxDD `-10.747`
- `market_context_high->unknown_1h` score `-0.5351` n `140` status `ready` deltaP `2.4893` edge `0.0119` maxDD `-3.1801`
- `market_context_high->fx_1h` score `-0.5747` n `140` status `ready` deltaP `-0.9324` edge `0.0027` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.6219` n `140` status `ready` deltaP `5.5517` edge `0.0702` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6274` n `140` status `ready` deltaP `-0.7357` edge `-0.0002` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6824` n `140` status `ready` deltaP `-0.278` edge `0.0031` maxDD `-3.4325`
- `market_context_high->fx_4h` score `-0.9492` n `140` status `ready` deltaP `-1.2195` edge `0.0069` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2307` n `140` status `ready` deltaP `2.2256` edge `0.0194` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3697` n `139` status `ready` deltaP `-2.2132` edge `-0.0122` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
