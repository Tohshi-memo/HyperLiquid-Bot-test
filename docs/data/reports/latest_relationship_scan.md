# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T06:07:20.142474+00:00`
- Price records: `524`
- Market context records: `620`
- Flow alert records: `1752`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `5.1978` n `146` status `ready` deltaP `7.4927` edge `0.388` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `5.0112` n `146` status `ready` deltaP `14.4444` edge `0.3547` maxDD `-1.3382`
- `market_context_high->fx_4h` score `-0.0862` n `146` status `ready` deltaP `9.0129` edge `0.016` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3201` n `146` status `ready` deltaP `2.0043` edge `0.0034` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.6107` n `146` status `ready` deltaP `1.4336` edge `0.037` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7046` n `146` status `ready` deltaP `-0.2814` edge `-0.0031` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.059` n `146` status `ready` deltaP `-3.3772` edge `-0.0054` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.178` n `146` status `ready` deltaP `5.7298` edge `-0.0049` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.3022` n `146` status `ready` deltaP `-2.4132` edge `-0.0114` maxDD `-4.4826`
- `market_context_high->crypto_alt_4h` score `-1.6166` n `146` status `ready` deltaP `4.9887` edge `0.089` maxDD `-15.2248`
- `market_context_high->crypto_major_1h` score `-1.7052` n `146` status `ready` deltaP `5.5505` edge `-0.0068` maxDD `-11.4508`
- `market_context_high->crypto_major_4h` score `-2.2398` n `146` status `ready` deltaP `14.4375` edge `0.0877` maxDD `-22.648`
- `market_context_high->index_4h` score `-2.3116` n `146` status `ready` deltaP `-0.8045` edge `-0.035` maxDD `-6.5149`
- `market_context_high->index_24h` score `-2.7901` n `146` status `ready` deltaP `-7.7992` edge `0.019` maxDD `-5.9609`
- `market_context_high->equity_4h` score `-3.2576` n `146` status `ready` deltaP `-3.3839` edge `-0.0337` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.301` n `146` status `ready` deltaP `-4.568` edge `-0.0487` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7002` n `146` status `ready` deltaP `-6.428` edge `0.0846` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.2608` n `146` status `ready` deltaP `-2.365` edge `-0.0133` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.6294` n `146` status `ready` deltaP `2.675` edge `-0.2158` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.7692` n `146` status `ready` deltaP `-11.2141` edge `-0.0622` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
