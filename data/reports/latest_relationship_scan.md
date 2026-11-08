# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T10:37:32.467889+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4713`

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

- `market_context_high->unknown_4h` score `108.097` n `37` status `ready` deltaP `-3.9387` edge `9.0791` maxDD `-0.9139`
- `market_context_high->equity_24h` score `4.8487` n `34` status `ready` deltaP `11.1213` edge `0.7594` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.2688` n `37` status `ready` deltaP `10.5074` edge `0.2483` maxDD `-2.3425`
- `market_context_high->fx_4h` score `3.1327` n `37` status `ready` deltaP `33.7714` edge `0.0449` maxDD `-0.0521`
- `news_risk_high->fx_4h` score `2.2505` n `41` status `ready` deltaP `26.9817` edge `0.0162` maxDD `-0.016`
- `market_context_high->index_4h` score `2.0548` n `37` status `ready` deltaP `26.8128` edge `0.0395` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `0.94` n `38` status `ready` deltaP `3.5453` edge `0.0768` maxDD `-0.1014`
- `market_context_high->crypto_major_1h` score `0.8466` n `37` status `ready` deltaP `10.1999` edge `0.0611` maxDD `-3.0172`
- `market_context_high->index_24h` score `0.6317` n `34` status `ready` deltaP `7.598` edge `0.0934` maxDD `-2.7123`
- `market_context_high->crypto_alt_1h` score `0.5628` n `37` status `ready` deltaP `12.2957` edge `0.0717` maxDD `-3.1881`
- `news_risk_high->fx_1h` score `0.5357` n `41` status `ready` deltaP `12.6041` edge `0.0062` maxDD `-0.0567`
- `market_context_high->commodity_24h` score `0.5108` n `34` status `ready` deltaP `4.0032` edge `0.1583` maxDD `-6.5601`
- `market_context_high->fx_24h` score `0.5015` n `34` status `ready` deltaP `9.2729` edge `-0.0112` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.3727` n `37` status `ready` deltaP `6.4736` edge `0.015` maxDD `-0.1681`
- `market_context_high->index_1h` score `0.3225` n `37` status `ready` deltaP `2.2496` edge `0.0389` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.1109` n `37` status `ready` deltaP `8.8688` edge `0.0097` maxDD `-1.7019`
- `news_risk_high->equity_4h` score `0.0579` n `41` status `ready` deltaP `-3.5061` edge `0.1021` maxDD `-4.2454`
- `news_risk_high->index_1h` score `0.0281` n `41` status `ready` deltaP `6.9958` edge `0.0023` maxDD `-0.2931`
- `news_risk_high->index_4h` score `0.0068` n `41` status `ready` deltaP `4.2683` edge `0.0203` maxDD `-0.4975`
- `market_context_high->commodity_4h` score `-0.0607` n `37` status `ready` deltaP `2.2248` edge `0.0228` maxDD `-1.633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
