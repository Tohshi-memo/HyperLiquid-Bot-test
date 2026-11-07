# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T00:22:29.732490+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.921` n `73` status `ready` deltaP `7.5364` edge `0.1584` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.2735` n `73` status `ready` deltaP `9.6663` edge `0.0184` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.1303` n `73` status `ready` deltaP `6.1073` edge `0.1428` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0787` n `73` status `ready` deltaP `7.7885` edge `0.0035` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `0.0246` n `73` status `ready` deltaP `1.456` edge `0.0484` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.037` n `73` status `ready` deltaP `5.5421` edge `0.0029` maxDD `-0.2336`
- `news_risk_high->fx_24h` score `-0.2009` n `73` status `ready` deltaP `-2.5328` edge `0.0444` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2651` n `73` status `ready` deltaP `0.4532` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.418` n `73` status `ready` deltaP `-1.7328` edge `-0.0063` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.291` n `73` status `ready` deltaP `-5.2602` edge `-0.0399` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-1.9305` n `73` status `ready` deltaP `-6.2095` edge `-0.0256` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-2.3406` n `73` status `ready` deltaP `-4.2408` edge `-0.044` maxDD `-5.8225`
- `news_risk_high->commodity_1h` score `-2.698` n `73` status `ready` deltaP `-17.1007` edge `-0.0074` maxDD `-1.6076`
- `news_risk_high->crypto_major_4h` score `-2.8819` n `73` status `ready` deltaP `-8.1377` edge `-0.0173` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-3.2526` n `73` status `ready` deltaP `21.29` edge `0.5997` maxDD `-86.0244`
- `news_risk_high->metal_24h` score `-3.3296` n `73` status `ready` deltaP `-0.2188` edge `-0.2358` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-4.139` n `73` status `ready` deltaP `-27.1676` edge `-0.004` maxDD `-4.1171`
- `news_risk_high->crypto_alt_4h` score `-4.8279` n `73` status `ready` deltaP `-10.1194` edge `-0.072` maxDD `-14.0292`
- `news_risk_high->commodity_24h` score `-9.7623` n `73` status `ready` deltaP `-26.5221` edge `-0.0688` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.2472` n `73` status `ready` deltaP `-29.8968` edge `-0.0543` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
