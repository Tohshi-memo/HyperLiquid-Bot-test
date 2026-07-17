# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T11:52:32.642753+00:00`
- Price records: `672`
- Market context records: `7025`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2983` n `219` status `ready` deltaP `1.4033` edge `0.0009` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6315` n `219` status `ready` deltaP `1.0219` edge `0.027` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.6801` n `219` status `ready` deltaP `-1.711` edge `0.001` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7304` n `219` status `ready` deltaP `-0.3186` edge `-0.0004` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7402` n `219` status `ready` deltaP `10.7418` edge `0.0068` maxDD `-1.8643`
- `market_context_high->crypto_major_1h` score `-0.7449` n `219` status `ready` deltaP `2.5265` edge `0.0229` maxDD `-7.1523`
- `market_context_high->unknown_24h` score `-0.8237` n `206` status `ready` deltaP `-6.8247` edge `0.3949` maxDD `-18.7342`
- `market_context_high->unknown_1h` score `-1.25` n `219` status `ready` deltaP `-2.886` edge `-0.0001` maxDD `-3.1196`
- `market_context_high->commodity_1h` score `-1.4127` n `219` status `ready` deltaP `-4.0159` edge `-0.0188` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.5301` n `219` status `ready` deltaP `-4.3469` edge `-0.0385` maxDD `-3.9617`
- `market_context_high->index_4h` score `-1.8485` n `219` status `ready` deltaP `6.9336` edge `-0.0133` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9547` n `219` status `ready` deltaP `5.7328` edge `0.0095` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.2381` n `219` status `ready` deltaP `-5.9918` edge `0.0778` maxDD `-9.2824`
- `market_context_high->commodity_24h` score `-2.7323` n `206` status `ready` deltaP `-3.4217` edge `-0.074` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.7497` n `219` status `ready` deltaP `0.8415` edge `0.0204` maxDD `-22.2831`
- `market_context_high->equity_1h` score `-3.1124` n `219` status `ready` deltaP `2.2715` edge `-0.0191` maxDD `-15.7664`
- `market_context_high->crypto_major_4h` score `-3.1235` n `219` status `ready` deltaP `1.9051` edge `0.0153` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.9281` n `206` status `ready` deltaP `-3.9509` edge `-0.014` maxDD `-4.2932`
- `market_context_high->equity_4h` score `-11.291` n `219` status `ready` deltaP `4.0455` edge `-0.0763` maxDD `-64.3269`
- `market_context_high->metal_24h` score `-13.5254` n `206` status `ready` deltaP `-11.2476` edge `-0.0552` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
