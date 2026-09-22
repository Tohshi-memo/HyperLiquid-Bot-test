# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T18:37:35.663334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_4h` score `46.2426` n `46` status `ready` deltaP `7.0122` edge `3.8068` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.5787` n `46` status `ready` deltaP `12.8397` edge `2.3949` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2872` n `46` status `ready` deltaP `12.3189` edge `1.2852` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `14.4057` n `46` status `ready` deltaP `12.3264` edge `1.1183` maxDD `0.0`
- `market_context_high->index_24h` score `5.5788` n `46` status `ready` deltaP `20.1314` edge `0.3394` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `5.2766` n `97` status `ready` deltaP `39.331` edge `0.2954` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.5067` n `97` status `ready` deltaP `-9.6166` edge `1.1255` maxDD `-46.1999`
- `news_risk_high->crypto_alt_4h` score `3.0767` n `97` status `ready` deltaP `12.3884` edge `0.2736` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `3.0659` n `97` status `ready` deltaP `15.5896` edge `0.2093` maxDD `-2.619`
- `news_risk_high->crypto_alt_1h` score `2.3444` n `97` status `ready` deltaP `13.149` edge `0.1431` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.868` n `46` status `ready` deltaP `22.2494` edge `0.0207` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6752` n `97` status `ready` deltaP `14.646` edge `0.0813` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2085` n `97` status `ready` deltaP `18.7955` edge `0.039` maxDD `-0.421`
- `market_context_high->metal_24h` score `1.1543` n `46` status `ready` deltaP `22.962` edge `-0.0335` maxDD `-0.2042`
- `news_risk_high->crypto_alt_24h` score `0.9494` n `97` status `ready` deltaP `-8.2922` edge `0.6225` maxDD `-32.7147`
- `market_context_high->equity_1h` score `0.7166` n `46` status `ready` deltaP `6.4632` edge `0.0409` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.6052` n `46` status `ready` deltaP `9.9063` edge `0.0097` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5835` n `97` status `ready` deltaP `14.6491` edge `0.0107` maxDD `-0.7788`
- `news_risk_high->metal_24h` score `0.5126` n `97` status `ready` deltaP `19.0399` edge `0.0232` maxDD `-2.4203`
- `news_risk_high->fx_24h` score `0.5116` n `97` status `ready` deltaP `19.6252` edge `0.0937` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
