# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T19:51:20.953032+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8636`

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

- `market_context_high->unknown_24h` score `1225.9539` n `148` status `ready` deltaP `-2.135` edge `102.2698` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `21.6144` n `149` status `ready` deltaP `4.385` edge `1.7872` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.3379` n `148` status `ready` deltaP `23.3671` edge `0.0245` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.147` n `149` status `ready` deltaP `6.9696` edge `0.0016` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.1112` n `149` status `ready` deltaP `8.0276` edge `0.0069` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.2222` n `149` status `ready` deltaP `5.7047` edge `0.0033` maxDD `-0.4545`
- `market_context_high->crypto_major_1h` score `-0.3983` n `149` status `ready` deltaP `6.2312` edge `0.0357` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4428` n `149` status `ready` deltaP `6.8966` edge `0.039` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5269` n `148` status `ready` deltaP `12.7534` edge `0.0283` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6321` n `149` status `ready` deltaP `-0.1909` edge `0.007` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7702` n `149` status `ready` deltaP `-4.0731` edge `-0.0033` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7932` n `149` status `ready` deltaP `8.2941` edge `-0.0029` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.4576` n `149` status `ready` deltaP `0.64` edge `0.0001` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.611` n `149` status `ready` deltaP `2.4464` edge `0.0135` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.1368` n `149` status `ready` deltaP `-10.2462` edge `-0.0309` maxDD `-5.6417`
- `market_context_high->equity_24h` score `-3.2602` n `148` status `ready` deltaP `5.9168` edge `-0.0147` maxDD `-15.7143`
- `market_context_high->crypto_major_24h` score `-3.3442` n `148` status `ready` deltaP `-0.0187` edge `0.0571` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4464` n `149` status `ready` deltaP `3.5092` edge `-0.0333` maxDD `-27.2215`
- `market_context_high->metal_24h` score `-3.4503` n `148` status `ready` deltaP `-0.0657` edge `0.0149` maxDD `-10.1587`
- `market_context_high->equity_4h` score `-5.4854` n `149` status `ready` deltaP `-4.3921` edge `-0.1506` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
