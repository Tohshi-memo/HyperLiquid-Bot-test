# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T19:37:32.142553+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3744`

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

- `market_context_high->unknown_1h` score `32169.7226` n `45` status `ready` deltaP `1.8662` edge `2680.8072` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21838.5082` n `45` status `ready` deltaP `1.958` edge `1819.8765` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `934.7676` n `31` status `ready` deltaP `2.0813` edge `77.901` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `585.5607` n `31` status `ready` deltaP `3.1766` edge `48.7812` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `301.0271` n `31` status `ready` deltaP `5.7292` edge `25.0474` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.4151` n `31` status `ready` deltaP `52.0833` edge `3.5207` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.5463` n `31` status `ready` deltaP `54.5139` edge `3.1821` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `38.4063` n `31` status `ready` deltaP `54.5139` edge `2.8371` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.9931` n `31` status `ready` deltaP `41.2355` edge `0.752` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `11.2865` n `31` status `ready` deltaP `26.4555` edge `0.8512` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `11.0157` n `31` status `ready` deltaP `37.8344` edge `0.7138` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4811` n `31` status `ready` deltaP `53.2986` edge `0.2681` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `7.0007` n `31` status `ready` deltaP `17.6927` edge `0.9213` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.4561` n `31` status `ready` deltaP `46.9198` edge `0.1547` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6115` n `31` status `ready` deltaP `19.8377` edge `0.1874` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.387` n `31` status `ready` deltaP `36.31` edge `0.0662` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6159` n `31` status `ready` deltaP `31.0943` edge `0.0192` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4555` n `31` status `ready` deltaP `10.31` edge `0.2922` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.4044` n `45` status `ready` deltaP `29.6307` edge `0.0313` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2401` n `31` status `ready` deltaP `12.5555` edge `0.2392` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
