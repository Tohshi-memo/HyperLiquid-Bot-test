# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T05:37:14.251795+00:00`
- Price records: `618`
- Market context records: `723`
- Flow alert records: `2043`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.6921` n `146` status `ready` deltaP `28.3708` edge `0.8186` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.3372` n `146` status `ready` deltaP `7.9358` edge `0.48` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.3133` n `149` status `ready` deltaP `5.7114` edge `0.0089` maxDD `-1.6381`
- `market_context_high->index_24h` score `-0.4473` n `146` status `ready` deltaP `-0.6691` edge `0.1667` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.4517` n `153` status `ready` deltaP `2.6262` edge `0.0423` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.4701` n `153` status `ready` deltaP `2.4343` edge `0.0024` maxDD `-0.291`
- `market_context_high->index_1h` score `-0.6194` n `153` status `ready` deltaP `0.4564` edge `0.0029` maxDD `-2.8282`
- `market_context_high->crypto_major_4h` score `-0.9997` n `149` status `ready` deltaP `17.4798` edge `0.1259` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.0839` n `153` status `ready` deltaP `-1.019` edge `-0.0025` maxDD `-4.4826`
- `market_context_high->equity_24h` score `-1.3242` n `146` status `ready` deltaP `-2.4567` edge `0.1665` maxDD `-10.5047`
- `market_context_high->unknown_1h` score `-1.3972` n `153` status `ready` deltaP `-4.5699` edge `-0.0188` maxDD `-2.7068`
- `market_context_high->crypto_alt_1h` score `-1.4406` n `153` status `ready` deltaP `4.1132` edge `-0.016` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.6611` n `153` status `ready` deltaP `5.5619` edge `-0.0032` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.8391` n `149` status `ready` deltaP `1.2166` edge `-0.0091` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9888` n `149` status `ready` deltaP `3.3668` edge `0.0688` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7907` n `149` status `ready` deltaP `-1.7934` edge `-0.0054` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3582` n `153` status `ready` deltaP `-5.0435` edge `-0.0503` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.6215` n `149` status `ready` deltaP `-5.3994` edge `0.0843` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.0141` n `149` status `ready` deltaP `4.2766` edge `-0.1752` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.1975` n `146` status `ready` deltaP `-13.7039` edge `-0.0578` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
