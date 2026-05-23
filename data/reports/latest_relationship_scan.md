# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T16:07:19.626967+00:00`
- Price records: `672`
- Market context records: `1644`
- Flow alert records: `6646`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `9.4552` n `172` status `ready` deltaP `27.3195` edge `0.8484` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `3.6789` n `186` status `ready` deltaP `20.9089` edge `0.4336` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.5337` n `172` status `ready` deltaP `19.3469` edge `0.3033` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.0529` n `186` status `ready` deltaP `16.6895` edge `0.3307` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.6435` n `186` status `ready` deltaP `11.6858` edge `0.1685` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.3123` n `172` status `ready` deltaP `18.4055` edge `0.4765` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.1232` n `172` status `ready` deltaP `24.143` edge `0.7079` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.1184` n `195` status `ready` deltaP `4.3716` edge `0.0884` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `-0.2714` n `172` status `ready` deltaP `24.7043` edge `0.9936` maxDD `-88.8062`
- `market_context_high->equity_1h` score `-0.3071` n `195` status `ready` deltaP `1.0624` edge `0.0344` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.4588` n `186` status `ready` deltaP `0.1618` edge `0.049` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.4779` n `172` status `ready` deltaP `6.4617` edge `0.022` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.4803` n `195` status `ready` deltaP `-0.7957` edge `0.0069` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.4852` n `195` status `ready` deltaP `0.6324` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_major_1h` score `-0.5809` n `195` status `ready` deltaP `0.8877` edge `0.047` maxDD `-5.5244`
- `market_context_high->commodity_1h` score `-0.8116` n `195` status `ready` deltaP `2.0627` edge `-0.0055` maxDD `-6.6507`
- `market_context_high->metal_1h` score `-0.8429` n `195` status `ready` deltaP `3.1528` edge `0.0045` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-1.3945` n `186` status `ready` deltaP `-10.8589` edge `-0.0135` maxDD `-1.4313`
- `market_context_high->metal_4h` score `-1.4608` n `186` status `ready` deltaP `7.4926` edge `0.0975` maxDD `-12.5349`
- `market_context_high->unknown_4h` score `-3.3358` n `186` status `ready` deltaP `9.7705` edge `-0.116` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
