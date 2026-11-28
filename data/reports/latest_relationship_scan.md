# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T21:07:26.752104+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7504`

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

- `market_context_high->fx_1h` score `0.7895` n `72` status `ready` deltaP `12.9491` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.662` n `65` status `ready` deltaP `12.7439` edge `0.0098` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2558` n `72` status `ready` deltaP `7.3935` edge `0.0043` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0109` n `72` status `ready` deltaP `3.676` edge `0.0087` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2072` n `72` status `ready` deltaP `6.2375` edge `-0.0079` maxDD `-2.1532`
- `market_context_high->index_1h` score `-0.455` n `72` status `ready` deltaP `-0.8982` edge `-0.003` maxDD `-0.2813`
- `market_context_high->metal_4h` score `-0.4751` n `65` status `ready` deltaP `0.4503` edge `0.0083` maxDD `-0.4441`
- `market_context_high->crypto_major_1h` score `-1.2111` n `72` status `ready` deltaP `-4.4661` edge `0.002` maxDD `-7.5329`
- `market_context_high->equity_4h` score `-3.9564` n `65` status `ready` deltaP `-20.7692` edge `-0.1651` maxDD `-6.9605`
- `market_context_high->commodity_4h` score `-4.2275` n `65` status `ready` deltaP `-26.189` edge `-0.0199` maxDD `-2.9572`
- `market_context_high->crypto_alt_1h` score `-4.3994` n `72` status `ready` deltaP `-9.506` edge `-0.1079` maxDD `-11.9607`
- `market_context_high->index_4h` score `-4.5652` n `65` status `ready` deltaP `-27.3804` edge `-0.0231` maxDD `-0.984`
- `market_context_high->crypto_major_4h` score `-9.5793` n `65` status `ready` deltaP `-11.4564` edge `-0.2714` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-20.1024` n `65` status `ready` deltaP `-34.8101` edge `-0.6967` maxDD `-49.048`
- `market_context_high->unknown_4h` score `-639.0513` n `65` status `ready` deltaP `4.4066` edge `-53.2787` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1324.7827` n `72` status `ready` deltaP `1.5885` edge `-110.3975` maxDD `-0.2652`
- `news_risk_high->unknown_4h` score `3471.4872` n `29` status `thin_sample` deltaP `5.9451` edge `299.2265` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2968.337` n `29` status `thin_sample` deltaP `5.0846` edge `255.8666` maxDD `-0.4169`
- `news_risk_high->crypto_major_24h` score `26.3326` n `29` status `thin_sample` deltaP `40.9722` edge `1.9969` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.6447` n `29` status `thin_sample` deltaP `39.0625` edge `1.5193` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
