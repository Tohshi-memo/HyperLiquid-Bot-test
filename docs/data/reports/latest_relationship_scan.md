# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T22:37:34.398384+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4102`

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

- `news_risk_high->equity_4h` score `1.2403` n `80` status `ready` deltaP `11.0671` edge `0.1758` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.3472` n `80` status `ready` deltaP `11.0976` edge `0.0183` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.2686` n `80` status `ready` deltaP `4.9027` edge `0.0567` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.2517` n `80` status `ready` deltaP `10.9955` edge `0.0043` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `0.1266` n `80` status `ready` deltaP `8.6585` edge `0.0031` maxDD `-0.2336`
- `news_risk_high->index_24h` score `-0.1069` n `80` status `ready` deltaP `1.9671` edge `0.14` maxDD `-6.6786`
- `news_risk_high->fx_24h` score `-0.185` n `80` status `ready` deltaP `-0.9835` edge `0.0354` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.2914` n `80` status `ready` deltaP `1.9087` edge `0.0016` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.4443` n `80` status `ready` deltaP `-2.2979` edge `-0.0059` maxDD `-0.5256`
- `news_risk_high->crypto_major_1h` score `-0.7622` n `80` status `ready` deltaP `-1.5045` edge `0.0062` maxDD `-4.1772`
- `news_risk_high->crypto_alt_1h` score `-0.9756` n `80` status `ready` deltaP `0.0449` edge `-0.0026` maxDD `-5.8225`
- `news_risk_high->metal_4h` score `-1.2436` n `80` status `ready` deltaP `-4.5427` edge `-0.0386` maxDD `-1.5773`
- `news_risk_high->crypto_major_4h` score `-1.2454` n `80` status `ready` deltaP `-3.3537` edge `0.0313` maxDD `-9.1553`
- `news_risk_high->equity_24h` score `-2.246` n `80` status `ready` deltaP `24.0728` edge `0.7102` maxDD `-86.0244`
- `news_risk_high->crypto_alt_4h` score `-2.7275` n `80` status `ready` deltaP `-6.8902` edge `-0.0401` maxDD `-14.0916`
- `news_risk_high->commodity_1h` score `-2.9669` n `80` status `ready` deltaP `-18.3982` edge `-0.0071` maxDD `-1.7322`
- `news_risk_high->metal_24h` score `-3.1153` n `80` status `ready` deltaP `2.3722` edge `-0.2256` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-3.9686` n `80` status `ready` deltaP `-25.4878` edge `-0.001` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-9.4268` n `80` status `ready` deltaP `-26.2587` edge `-0.0391` maxDD `-28.3791`
- `news_risk_high->crypto_major_24h` score `-12.0715` n `80` status `ready` deltaP `-25.7907` edge `0.0163` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
