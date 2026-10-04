# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T07:52:34.711066+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5004`

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

- `market_context_high->unknown_4h` score `228.8646` n `61` status `ready` deltaP `7.7719` edge `19.0346` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `180.2149` n `73` status `ready` deltaP `2.1697` edge `15.0449` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.9345` n `46` status `ready` deltaP `31.5613` edge `1.0781` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.8307` n `46` status `ready` deltaP `38.0039` edge `0.8811` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.1276` n `65` status `ready` deltaP `40.1736` edge `0.6798` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `11.0199` n `59` status `ready` deltaP `28.4023` edge `0.739` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.5434` n `65` status `ready` deltaP `24.6646` edge `0.5986` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.234` n `61` status `ready` deltaP `21.6364` edge `0.4456` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4074` n `61` status `ready` deltaP `20.0744` edge `0.4457` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.7394` n `59` status `ready` deltaP `32.0624` edge `0.1812` maxDD `0.0`
- `market_context_high->equity_24h` score `4.0458` n `46` status `ready` deltaP `9.095` edge `0.3762` maxDD `-6.3081`
- `news_risk_high->equity_4h` score `3.9567` n `65` status `ready` deltaP `27.2842` edge `0.2091` maxDD `-2.9013`
- `news_risk_high->index_4h` score `3.2074` n `65` status `ready` deltaP `34.9625` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0383` n `65` status `ready` deltaP `13.3095` edge `0.2` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6355` n `73` status `ready` deltaP `17.0187` edge `0.1512` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5768` n `65` status `ready` deltaP `22.1271` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.2376` n `73` status `ready` deltaP `13.5305` edge `0.1709` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.1824` n `65` status `ready` deltaP `26.8148` edge `0.0181` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5763` n `65` status `ready` deltaP `4.8687` edge `0.1508` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.3226` n `61` status `ready` deltaP `19.3823` edge `0.0304` maxDD `-0.285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
