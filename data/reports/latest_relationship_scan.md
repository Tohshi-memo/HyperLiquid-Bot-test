# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T09:07:18.808518+00:00`
- Price records: `672`
- Market context records: `1931`
- Flow alert records: `7458`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.2756` n `210` status `ready` deltaP `23.0647` edge `0.567` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7213` n `210` status `ready` deltaP `27.4071` edge `0.502` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.4302` n `210` status `ready` deltaP `16.8365` edge `0.376` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1009` n `210` status `ready` deltaP `13.5192` edge `0.1944` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.6635` n `196` status `ready` deltaP `14.1653` edge `0.4929` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.6079` n `222` status `ready` deltaP `7.6604` edge `0.0982` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.4757` n `222` status `ready` deltaP `7.2167` edge `0.1029` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3198` n `196` status `ready` deltaP `12.2626` edge `0.1875` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1718` n `196` status `ready` deltaP `4.2233` edge `0.109` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1165` n `210` status `ready` deltaP `7.7105` edge `0.0672` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1988` n `222` status `ready` deltaP `4.5315` edge `0.0326` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2465` n `196` status `ready` deltaP `10.1793` edge `0.0165` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6462` n `222` status `ready` deltaP `-3.0021` edge `0.0004` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6881` n `222` status `ready` deltaP `-0.1308` edge `0.0067` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7234` n `222` status `ready` deltaP `4.0554` edge `0.0138` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9431` n `210` status `ready` deltaP `-4.6487` edge `-0.0011` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-1.157` n `210` status `ready` deltaP `8.8008` edge `0.1141` maxDD `-12.5349`
- `market_context_high->equity_24h` score `-1.1823` n `196` status `ready` deltaP `7.4582` edge `0.3416` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.3526` n `222` status `ready` deltaP `1.2111` edge `-0.0256` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9349` n `222` status `ready` deltaP `1.8045` edge `-0.0043` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
