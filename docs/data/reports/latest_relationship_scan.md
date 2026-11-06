# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T17:37:33.074246+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4082`

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

- `news_risk_high->equity_4h` score `2.5637` n `100` status `ready` deltaP `17.5427` edge `0.3023` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.124` n `100` status `ready` deltaP `16.8659` edge `0.029` maxDD `-0.4888`
- `news_risk_high->equity_24h` score `0.7499` n `100` status `ready` deltaP `30.0728` edge `1.0543` maxDD `-86.0244`
- `news_risk_high->equity_1h` score `0.3323` n `100` status `ready` deltaP `4.4012` edge `0.0816` maxDD `-2.4672`
- `news_risk_high->index_1h` score `0.2113` n `100` status `ready` deltaP `10.0958` edge `0.006` maxDD `-0.3636`
- `news_risk_high->index_24h` score `-0.1039` n `100` status `ready` deltaP `4.3536` edge `0.1458` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.3296` n `100` status `ready` deltaP `-0.3413` edge `0.0` maxDD `-0.1984`
- `news_risk_high->metal_1h` score `-0.3593` n `100` status `ready` deltaP `-0.5988` edge `-0.0062` maxDD `-0.536`
- `news_risk_high->crypto_major_4h` score `-0.3814` n `100` status `ready` deltaP `1.5915` edge `0.1091` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5228` n `100` status `ready` deltaP `2.628` edge `0.1791` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.7283` n `100` status `ready` deltaP `1.2455` edge `0.0211` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7462` n `100` status `ready` deltaP `-1.7744` edge `-0.0029` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.8574` n `100` status `ready` deltaP `1.0549` edge `-0.0264` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-1.4198` n `100` status `ready` deltaP `-3.4551` edge `-0.0014` maxDD `-4.1772`
- `news_risk_high->fx_24h` score `-1.6928` n `100` status `ready` deltaP `-13.0035` edge `0.0082` maxDD `-0.3393`
- `news_risk_high->metal_24h` score `-2.8344` n `100` status `ready` deltaP `4.3692` edge `-0.2029` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.3291` n `100` status `ready` deltaP `-18.8503` edge `-0.0151` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.1104` n `100` status `ready` deltaP `-27.6463` edge `-0.0263` maxDD `-8.554`
- `news_risk_high->crypto_major_24h` score `-6.0095` n `100` status `ready` deltaP `-14.7938` edge `0.1785` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.9323` n `100` status `ready` deltaP `-24.8891` edge `-0.0147` maxDD `-34.4315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
