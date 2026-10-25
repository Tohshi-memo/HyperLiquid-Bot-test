# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T00:07:25.014786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7158`

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

- `market_context_high->unknown_4h` score `22.5296` n `96` status `ready` deltaP `1.9055` edge `1.8983` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.7303` n `58` status `ready` deltaP `23.0843` edge `0.0812` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.9304` n `96` status `ready` deltaP `12.1443` edge `0.0528` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.0986` n `107` status `ready` deltaP `4.6869` edge `0.0106` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3143` n `107` status `ready` deltaP `0.957` edge `0.0029` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.9211` n `96` status `ready` deltaP `-3.125` edge `0.0047` maxDD `-0.5168`
- `market_context_high->metal_1h` score `-0.9884` n `107` status `ready` deltaP `0.3987` edge `-0.0056` maxDD `-1.6873`
- `market_context_high->index_1h` score `-1.0888` n `107` status `ready` deltaP `-2.7814` edge `-0.007` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.9225` n `58` status `ready` deltaP `-6.0704` edge `-0.0028` maxDD `-1.6885`
- `market_context_high->crypto_major_1h` score `-2.6467` n `107` status `ready` deltaP `-0.88` edge `-0.0405` maxDD `-10.6022`
- `market_context_high->crypto_major_24h` score `-2.6961` n `58` status `ready` deltaP `-2.7778` edge `-0.0685` maxDD `-16.0245`
- `market_context_high->metal_4h` score `-3.4924` n `96` status `ready` deltaP `-11.9918` edge `-0.0324` maxDD `-5.9618`
- `market_context_high->crypto_alt_1h` score `-3.5014` n `107` status `ready` deltaP `-1.0619` edge `-0.0601` maxDD `-14.6347`
- `market_context_high->metal_24h` score `-3.5331` n `58` status `ready` deltaP `-11.7277` edge `0.012` maxDD `-7.259`
- `market_context_high->equity_1h` score `-4.0243` n `107` status `ready` deltaP `-1.1347` edge `-0.0949` maxDD `-12.6316`
- `market_context_high->index_4h` score `-5.0609` n `96` status `ready` deltaP `-25.3303` edge `-0.0534` maxDD `-5.2909`
- `market_context_high->index_24h` score `-7.8227` n `58` status `ready` deltaP `-37.5838` edge `-0.1735` maxDD `-6.8933`
- `market_context_high->unknown_1h` score `-8.2021` n `107` status `ready` deltaP `-0.1973` edge `-0.6333` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `-8.9832` n `58` status `ready` deltaP `0.012` edge `-0.3489` maxDD `-55.8969`
- `market_context_high->crypto_major_4h` score `-14.305` n `96` status `ready` deltaP `-25.4827` edge `-0.3661` maxDD `-44.4877`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
