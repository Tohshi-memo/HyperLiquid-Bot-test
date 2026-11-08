# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T17:07:26.071191+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4865`

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

- `market_context_high->unknown_4h` score `36.0414` n `39` status `ready` deltaP `-4.964` edge `3.0813` maxDD `-0.9139`
- `market_context_high->equity_24h` score `5.9956` n `37` status `ready` deltaP `14.3722` edge `0.8333` maxDD `-31.3588`
- `market_context_high->equity_1h` score `3.4099` n `39` status `ready` deltaP `13.0355` edge `0.2432` maxDD `-2.3425`
- `market_context_high->fx_4h` score `2.8086` n `39` status `ready` deltaP `30.1399` edge `0.0421` maxDD `-0.0521`
- `market_context_high->index_4h` score `1.8869` n `39` status `ready` deltaP `24.789` edge `0.039` maxDD `-2.4279`
- `market_context_high->crypto_alt_1h` score `1.1777` n `39` status `ready` deltaP `14.2139` edge `0.0849` maxDD `-3.1881`
- `market_context_high->crypto_major_1h` score `1.1345` n `39` status `ready` deltaP `11.9684` edge `0.0733` maxDD `-3.0172`
- `market_context_high->index_24h` score `1.0111` n `37` status `ready` deltaP `12.4343` edge `0.1098` maxDD `-2.7123`
- `market_context_high->fx_24h` score `0.7766` n `37` status `ready` deltaP `10.9422` edge `0.0006` maxDD `-0.0397`
- `market_context_high->fx_1h` score `0.5075` n `39` status `ready` deltaP `8.2643` edge `0.0143` maxDD `-0.1681`
- `market_context_high->commodity_24h` score `0.3503` n `37` status `ready` deltaP `3.782` edge `0.1392` maxDD `-6.5601`
- `market_context_high->index_1h` score `0.2667` n `39` status `ready` deltaP `3.5276` edge `0.0377` maxDD `-0.1621`
- `market_context_high->commodity_1h` score `0.0536` n `39` status `ready` deltaP `7.796` edge `0.0095` maxDD `-1.7019`
- `market_context_high->metal_1h` score `-0.0269` n `39` status `ready` deltaP `2.0306` edge `0.0158` maxDD `-0.6226`
- `market_context_high->commodity_4h` score `-0.1579` n `39` status `ready` deltaP `0.3401` edge `0.0229` maxDD `-1.633`
- `market_context_high->equity_4h` score `-0.5907` n `39` status `ready` deltaP `23.1669` edge `0.0978` maxDD `-24.9053`
- `market_context_high->metal_4h` score `-0.7817` n `39` status `ready` deltaP `-3.0566` edge `-0.0348` maxDD `-0.9363`
- `market_context_high->crypto_alt_4h` score `-0.9517` n `39` status `ready` deltaP `16.1664` edge `0.0145` maxDD `-17.5435`
- `market_context_high->metal_24h` score `-2.0181` n `37` status `ready` deltaP `4.0541` edge `-0.1399` maxDD `-1.4245`
- `market_context_high->crypto_major_4h` score `-3.8666` n `39` status `ready` deltaP `1.794` edge `-0.1092` maxDD `-15.9983`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
