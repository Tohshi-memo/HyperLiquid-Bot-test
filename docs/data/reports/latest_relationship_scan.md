# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T14:37:17.483281+00:00`
- Price records: `672`
- Market context records: `2359`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `news_risk_high->crypto_alt_24h` score `21.4897` n `43` status `ready` deltaP `50.0363` edge `1.5161` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.3687` n `43` status `ready` deltaP `45.9383` edge `1.1851` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8087` n `43` status `ready` deltaP `29.7925` edge `1.0669` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.327` n `43` status `ready` deltaP `19.7674` edge `0.8702` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.2661` n `140` status `ready` deltaP `20.0` edge `1.0281` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.7841` n `43` status `ready` deltaP `27.6405` edge `0.487` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.5321` n `140` status `ready` deltaP `24.4346` edge `0.4226` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.2269` n `154` status `ready` deltaP `24.9921` edge `0.5333` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `5.8752` n `154` status `ready` deltaP `21.0445` edge `0.6172` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.4199` n `154` status `ready` deltaP `22.0384` edge `0.3657` maxDD `-1.8773`
- `news_risk_high->index_24h` score `5.0632` n `43` status `ready` deltaP `13.0976` edge `0.3765` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.8666` n `43` status `ready` deltaP `32.7673` edge `0.3444` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4018` n `43` status `ready` deltaP `36.1879` edge `0.0607` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.0537` n `140` status `ready` deltaP `12.5992` edge `0.1389` maxDD `-1.4737`
- `news_risk_high->fx_4h` score `1.9491` n `43` status `ready` deltaP `24.9929` edge `0.0142` maxDD `-0.1382`
- `market_context_high->crypto_alt_1h` score `1.8679` n `158` status `ready` deltaP `12.9444` edge `0.1881` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.8404` n `158` status `ready` deltaP `14.7275` edge `0.1746` maxDD `-4.2199`
- `market_context_high->index_4h` score `1.8381` n `154` status `ready` deltaP `19.5834` edge `0.1052` maxDD `-2.2732`
- `market_context_high->equity_24h` score `1.6736` n `140` status `ready` deltaP `19.9752` edge `0.159` maxDD `-6.8828`
- `market_context_high->equity_4h` score `0.9873` n `154` status `ready` deltaP `10.6687` edge `0.1516` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
