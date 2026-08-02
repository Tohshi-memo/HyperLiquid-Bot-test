# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-02T08:37:23.813446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5900`

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

- `news_risk_high->unknown_24h` score `5188.5018` n `60` status `ready` deltaP `31.1149` edge `432.2098` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.9375` n `46` status `ready` deltaP `60.1085` edge `1.1338` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `6.4537` n `46` status `ready` deltaP `38.6821` edge `0.379` maxDD `-5.5926`
- `news_risk_high->equity_4h` score `4.5349` n `68` status `ready` deltaP `16.5261` edge `0.3441` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.589` n `68` status `ready` deltaP `15.6115` edge `0.0664` maxDD `-0.3783`
- `market_context_high->fx_4h` score `1.0839` n `46` status `ready` deltaP `21.8452` edge `0.0243` maxDD `-1.3685`
- `market_context_high->commodity_4h` score `0.609` n `46` status `ready` deltaP `10.1405` edge `0.0951` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.6` n `68` status `ready` deltaP `9.4928` edge `0.069` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `0.152` n `46` status `ready` deltaP `2.7439` edge `0.0969` maxDD `-5.323`
- `news_risk_high->fx_4h` score `0.1406` n `68` status `ready` deltaP `12.4462` edge `0.0245` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1134` n `68` status `ready` deltaP `5.3174` edge `0.0267` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.0839` n `46` status `ready` deltaP `4.2697` edge `0.0239` maxDD `-1.3282`
- `news_risk_high->crypto_alt_1h` score `0.0757` n `68` status `ready` deltaP `6.1818` edge `0.0367` maxDD `-3.1233`
- `market_context_high->fx_1h` score `0.0585` n `46` status `ready` deltaP `8.3181` edge `0.0023` maxDD `-0.6874`
- `news_risk_high->fx_1h` score `-0.0435` n `68` status `ready` deltaP `3.267` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.1026` n `68` status `ready` deltaP `1.8669` edge `0.0067` maxDD `-0.5845`
- `news_risk_high->metal_1h` score `-0.1427` n `68` status `ready` deltaP `2.4657` edge `0.0056` maxDD `-0.5599`
- `market_context_high->fx_24h` score `-0.1716` n `46` status `ready` deltaP `5.384` edge `0.0401` maxDD `-2.506`
- `news_risk_high->crypto_major_1h` score `-0.2483` n `68` status `ready` deltaP `1.9197` edge `0.0274` maxDD `-3.762`
- `market_context_high->crypto_alt_1h` score `-0.5867` n `46` status `ready` deltaP `-1.8745` edge `0.0` maxDD `-3.0178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
