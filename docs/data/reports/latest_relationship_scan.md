# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T12:22:23.362548+00:00`
- Price records: `672`
- Market context records: `2968`
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

- `market_context_high->crypto_alt_24h` score `16.8231` n `114` status `ready` deltaP `10.3801` edge `1.7244` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `9.3138` n `114` status `ready` deltaP `16.3377` edge `0.7137` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `8.6882` n `114` status `ready` deltaP `32.3282` edge `0.5726` maxDD `-2.1282`
- `market_context_high->equity_24h` score `7.4115` n `114` status `ready` deltaP `16.7398` edge `0.7064` maxDD `-12.6963`
- `market_context_high->index_24h` score `3.6193` n `114` status `ready` deltaP `15.1773` edge `0.2985` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1976` n `115` status `ready` deltaP `16.246` edge `0.1971` maxDD `-0.7819`
- `market_context_high->crypto_alt_4h` score `2.5165` n `115` status `ready` deltaP `23.6015` edge `0.5085` maxDD `-30.8239`
- `market_context_high->index_4h` score `1.5817` n `115` status `ready` deltaP `16.9115` edge `0.0979` maxDD `-1.9733`
- `market_context_high->equity_1h` score `0.8766` n `115` status `ready` deltaP `6.4996` edge `0.0632` maxDD `-1.012`
- `market_context_high->crypto_alt_1h` score `0.3632` n `115` status `ready` deltaP `9.5509` edge `0.1301` maxDD `-10.747`
- `market_context_high->unknown_4h` score `0.1296` n `115` status `ready` deltaP `3.4106` edge `0.0934` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.0921` n `115` status `ready` deltaP `5.8943` edge `0.0206` maxDD `-1.1802`
- `market_context_high->crypto_major_1h` score `0.0135` n `115` status `ready` deltaP `9.0666` edge `0.0949` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-0.1546` n `115` status `ready` deltaP `8.3576` edge `0.0552` maxDD `-7.1252`
- `market_context_high->fx_1h` score `-0.3323` n `115` status `ready` deltaP `-0.1002` edge `0.0037` maxDD `-0.1244`
- `market_context_high->commodity_1h` score `-0.6061` n `115` status `ready` deltaP `-1.8107` edge `-0.0031` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.7851` n `115` status `ready` deltaP `-1.5178` edge `-0.0018` maxDD `-3.4325`
- `market_context_high->unknown_1h` score `-0.8456` n `115` status `ready` deltaP `2.3874` edge `-0.0133` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.9111` n `115` status `ready` deltaP `11.0604` edge `0.322` maxDD `-33.6701`
- `market_context_high->fx_4h` score `-1.2153` n `115` status `ready` deltaP `-4.1556` edge `0.0043` maxDD `-0.5631`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
