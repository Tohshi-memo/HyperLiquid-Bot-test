# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T10:37:28.768562+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8030`

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

- `market_context_high->crypto_major_24h` score `22.4689` n `44` status `ready` deltaP `32.2759` edge `1.7853` maxDD `-6.245`
- `market_context_high->crypto_alt_24h` score `21.7356` n `44` status `ready` deltaP `20.644` edge `1.8413` maxDD `-9.4102`
- `market_context_high->unknown_4h` score `19.7206` n `111` status `ready` deltaP `-3.5226` edge `1.7315` maxDD `-1.8373`
- `risk_on_high->crypto_alt_4h` score `3.786` n `48` status `ready` deltaP `18.1911` edge `0.239` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.786` n `48` status `ready` deltaP `18.1911` edge `0.239` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.441` n `48` status `ready` deltaP `32.6728` edge `0.3086` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.441` n `48` status `ready` deltaP `32.6728` edge `0.3086` maxDD `-4.1548`
- `market_context_high->unknown_1h` score `2.9297` n `111` status `ready` deltaP `-3.5132` edge `0.3012` maxDD `-1.024`
- `market_context_high->equity_24h` score `2.5528` n `44` status `ready` deltaP `2.0676` edge `0.4538` maxDD `-7.5571`
- `market_context_high->index_24h` score `1.7242` n `44` status `ready` deltaP `24.779` edge `0.1119` maxDD `-0.4833`
- `market_context_high->crypto_major_4h` score `1.6492` n `111` status `ready` deltaP `12.9656` edge `0.2485` maxDD `-10.1339`
- `market_context_high->metal_24h` score `1.2414` n `44` status `ready` deltaP `15.9565` edge `0.0637` maxDD `-1.6634`
- `market_context_high->crypto_alt_1h` score `0.9903` n `111` status `ready` deltaP `8.5667` edge `0.1205` maxDD `-4.9401`
- `market_context_high->crypto_alt_4h` score `0.9854` n `111` status `ready` deltaP `6.5357` edge `0.2573` maxDD `-12.5004`
- `risk_on_high->crypto_alt_1h` score `0.8112` n `48` status `ready` deltaP `5.6387` edge `0.0897` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.8112` n `48` status `ready` deltaP `5.6387` edge `0.0897` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `0.3352` n `48` status `ready` deltaP `4.6158` edge `0.0775` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.3352` n `48` status `ready` deltaP `4.6158` edge `0.0775` maxDD `-3.2233`
- `market_context_high->crypto_major_1h` score `0.1747` n `111` status `ready` deltaP `2.7014` edge `0.0807` maxDD `-3.4384`
- `market_context_high->metal_1h` score `-0.2312` n `111` status `ready` deltaP `3.7574` edge `0.0014` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
