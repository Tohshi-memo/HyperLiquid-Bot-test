# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T11:22:24.118359+00:00`
- Price records: `672`
- Market context records: `2964`
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

- `market_context_high->crypto_alt_24h` score `17.1479` n `118` status `ready` deltaP `11.4995` edge `1.744` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.0818` n `118` status `ready` deltaP `16.8432` edge `0.691` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `7.7513` n `118` status `ready` deltaP `29.558` edge `0.541` maxDD `-3.0356`
- `market_context_high->equity_24h` score `7.686` n `118` status `ready` deltaP `17.111` edge `0.7268` maxDD `-12.6963`
- `market_context_high->equity_4h` score `3.4152` n `119` status `ready` deltaP `16.9413` edge `0.2106` maxDD `-0.7819`
- `market_context_high->index_24h` score `3.3993` n `118` status `ready` deltaP `14.0478` edge `0.2877` maxDD `-2.5127`
- `market_context_high->crypto_alt_4h` score `2.9573` n `119` status `ready` deltaP `24.161` edge `0.5415` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.8748` n `119` status `ready` deltaP `15.0889` edge `0.0904` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.7133` n `119` status `ready` deltaP `5.115` edge `0.059` maxDD `-1.026`
- `market_context_high->unknown_4h` score `0.3962` n `119` status `ready` deltaP `4.7781` edge `0.1065` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0543` n `119` status `ready` deltaP `5.3465` edge `0.0194` maxDD `-1.1802`
- `market_context_high->crypto_alt_1h` score `-0.0405` n `119` status `ready` deltaP `7.5341` edge `0.1099` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.1687` n `119` status `ready` deltaP `7.1667` edge `0.0842` maxDD `-9.622`
- `market_context_high->fx_1h` score `-0.1988` n `119` status `ready` deltaP `1.4781` edge `0.0043` maxDD `-0.1244`
- `market_context_high->commodity_4h` score `-0.5561` n `119` status `ready` deltaP `6.4703` edge `0.0457` maxDD `-8.1442`
- `market_context_high->crypto_major_4h` score `-0.5597` n `119` status `ready` deltaP `12.0875` edge `0.3602` maxDD `-33.6701`
- `market_context_high->commodity_1h` score `-0.5671` n `119` status `ready` deltaP `-1.2844` edge `-0.0016` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.7409` n `119` status `ready` deltaP `-1.0869` edge `0.001` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8046` n `119` status `ready` deltaP `1.6857` edge `-0.0052` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.0354` n `119` status `ready` deltaP `-2.4019` edge `0.0076` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
