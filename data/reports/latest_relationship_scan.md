# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T02:52:25.567090+00:00`
- Price records: `672`
- Market context records: `5729`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8882`

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

- `market_context_high->equity_24h` score `0.9047` n `218` status `ready` deltaP `15.703` edge `0.5192` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.1215` n `279` status `ready` deltaP `7.1083` edge `0.1266` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2381` n `285` status `ready` deltaP `2.4866` edge `0.001` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.43` n `285` status `ready` deltaP `1.9346` edge `-0.0005` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6118` n `285` status `ready` deltaP `3.3617` edge `0.0273` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.625` n `285` status `ready` deltaP `0.4376` edge `0.0038` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7909` n `285` status `ready` deltaP `-2.1872` edge `-0.0061` maxDD `-3.7906`
- `market_context_high->crypto_major_1h` score `-0.8165` n `285` status `ready` deltaP `3.0807` edge `0.0349` maxDD `-5.5448`
- `market_context_high->crypto_alt_1h` score `-0.9587` n `285` status `ready` deltaP `1.3358` edge `0.0316` maxDD `-5.6318`
- `market_context_high->fx_24h` score `-1.1204` n `218` status `ready` deltaP `10.8611` edge `0.0423` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1415` n `279` status `ready` deltaP `1.7528` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2542` n `279` status `ready` deltaP `2.7046` edge `0.0057` maxDD `-1.4288`
- `market_context_high->crypto_major_4h` score `-1.3341` n `279` status `ready` deltaP `7.8377` edge `0.1598` maxDD `-18.525`
- `market_context_high->metal_4h` score `-2.6013` n `279` status `ready` deltaP `-7.01` edge `-0.0492` maxDD `-11.6719`
- `market_context_high->crypto_alt_4h` score `-2.6651` n `279` status `ready` deltaP `5.6955` edge `0.1112` maxDD `-20.3676`
- `market_context_high->index_24h` score `-2.9467` n `218` status `ready` deltaP `1.2265` edge `0.0285` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8162` n `279` status `ready` deltaP `-3.2193` edge `-0.029` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3478` n `218` status `ready` deltaP `7.1961` edge `0.0354` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.6366` n `218` status `ready` deltaP `-7.255` edge `-0.2422` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.503` n `218` status `ready` deltaP `-10.5744` edge `-0.0741` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
