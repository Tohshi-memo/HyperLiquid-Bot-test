# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T23:52:15.698013+00:00`
- Price records: `672`
- Market context records: `1680`
- Flow alert records: `6745`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8854`

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

- `market_context_high->metal_24h` score `8.5312` n `154` status `ready` deltaP `27.3199` edge `0.7714` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.2114` n `195` status `ready` deltaP `22.8901` edge `0.5481` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.8858` n `154` status `ready` deltaP `18.7974` edge `0.3363` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `3.4014` n `195` status `ready` deltaP `19.3559` edge `0.4253` maxDD `-13.3376`
- `market_context_high->equity_4h` score `2.7466` n `195` status `ready` deltaP `15.0047` edge `0.2383` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.8971` n `154` status `ready` deltaP `17.9301` edge `0.5284` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.6144` n `154` status `ready` deltaP `14.0363` edge `0.573` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5864` n `204` status `ready` deltaP `6.0203` edge `0.1111` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.4561` n `154` status `ready` deltaP `25.2483` edge `1.0506` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.099` n `195` status `ready` deltaP `5.677` edge `0.0793` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.0212` n `154` status `ready` deltaP `24.0754` edge `0.7008` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1294` n `204` status `ready` deltaP `3.3404` edge `0.0478` maxDD `-2.8014`
- `market_context_high->crypto_major_1h` score `-0.3874` n `204` status `ready` deltaP `3.2553` edge `0.0734` maxDD `-5.5244`
- `market_context_high->metal_1h` score `-0.5543` n `204` status `ready` deltaP `7.0682` edge `0.0154` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.5799` n `154` status `ready` deltaP `6.0419` edge `0.0163` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6216` n `204` status `ready` deltaP `-0.3493` edge `0.0137` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6321` n `195` status `ready` deltaP `12.6469` edge `0.1322` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.857` n `204` status `ready` deltaP `-0.8835` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.2439` n `195` status `ready` deltaP `-8.3224` edge `-0.0111` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.1361` n `204` status `ready` deltaP `0.4638` edge `-0.0315` maxDD `-14.9691`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
