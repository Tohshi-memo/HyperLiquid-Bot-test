# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T21:22:27.264427+00:00`
- Price records: `672`
- Market context records: `5813`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.2161` n `288` status `ready` deltaP `5.9535` edge `0.1241` maxDD `-6.9958`
- `market_context_high->equity_24h` score `0.0845` n `248` status `ready` deltaP `15.3954` edge `0.4123` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1839` n `288` status `ready` deltaP `3.52` edge `0.0015` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5919` n `288` status `ready` deltaP `-1.3764` edge `-0.0029` maxDD `-2.4381`
- `market_context_high->index_1h` score `-0.6521` n `288` status `ready` deltaP `0.0354` edge `0.003` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6624` n `288` status `ready` deltaP `1.8733` edge `-0.0006` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.6953` n `288` status `ready` deltaP `2.4826` edge `0.0262` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8946` n `288` status `ready` deltaP `3.1125` edge `0.0368` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.054` n `288` status `ready` deltaP `1.6218` edge `0.0348` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2348` n `288` status `ready` deltaP `-0.0423` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4303` n `288` status `ready` deltaP `1.101` edge `0.0042` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4377` n `248` status `ready` deltaP `9.9014` edge `0.0309` maxDD `-5.498`
- `market_context_high->metal_4h` score `-2.1691` n `288` status `ready` deltaP `-4.3191` edge `-0.0434` maxDD `-9.1388`
- `market_context_high->crypto_major_4h` score `-2.686` n `288` status `ready` deltaP `8.0708` edge `0.1596` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.745` n `288` status `ready` deltaP `-1.7022` edge `-0.0176` maxDD `-8.6511`
- `market_context_high->index_24h` score `-4.3297` n `248` status `ready` deltaP `3.7131` edge `0.0289` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.3694` n `288` status `ready` deltaP `5.7504` edge `0.0984` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-5.4019` n `248` status `ready` deltaP `-4.077` edge `-0.234` maxDD `-19.1764`
- `market_context_high->commodity_24h` score `-5.9785` n `248` status `ready` deltaP `-12.92` edge `-0.0648` maxDD `-31.91`
- `market_context_high->crypto_major_24h` score `-11.8362` n `248` status `ready` deltaP `-2.9121` edge `-0.2792` maxDD `-36.3523`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
