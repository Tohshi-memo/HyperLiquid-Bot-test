# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T08:52:29.166871+00:00`
- Price records: `672`
- Market context records: `5965`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11254`

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

- `news_risk_high->fx_24h` score `7.0706` n `30` status `ready` deltaP `64.7569` edge `0.1575` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.1959` n `30` status `ready` deltaP `37.5348` edge `0.2033` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.843` n `30` status `ready` deltaP `39.8476` edge `0.0592` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.11` n `30` status `ready` deltaP `25.4291` edge `0.0202` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4904` n `233` status `ready` deltaP `9.4715` edge `0.1705` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8614` n `30` status `ready` deltaP `10.489` edge `0.0872` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2239` n `30` status `ready` deltaP `5.6188` edge `0.0374` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1304` n `30` status `ready` deltaP `7.3264` edge `0.0216` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3931` n `30` status `ready` deltaP `1.8363` edge `-0.026` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3966` n `243` status `ready` deltaP `4.0949` edge `0.0347` maxDD `-4.3608`
- `market_context_high->equity_24h` score `-0.4` n `214` status `ready` deltaP `21.4953` edge `0.3172` maxDD `-31.2762`
- `market_context_high->metal_1h` score `-0.4551` n `243` status `ready` deltaP `2.824` edge `0.0027` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5578` n `243` status `ready` deltaP `-2.3379` edge `-0.0002` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6407` n `243` status `ready` deltaP `0.6918` edge `0.0046` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6681` n `243` status `ready` deltaP `-0.5791` edge `-0.0007` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.1256` n `30` status `ready` deltaP `-10.7485` edge `-0.0212` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1537` n `243` status `ready` deltaP `1.4767` edge `0.019` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1576` n `243` status `ready` deltaP `1.627` edge `0.016` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4574` n `233` status `ready` deltaP `-1.4413` edge `-0.0059` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.5627` n `233` status `ready` deltaP `-1.9078` edge `-0.0244` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
