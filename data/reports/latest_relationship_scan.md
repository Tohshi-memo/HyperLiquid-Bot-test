# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T15:22:29.019534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3928`

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

- `news_risk_high->equity_4h` score `1.2844` n `109` status `ready` deltaP `13.458` edge `0.2154` maxDD `-8.2363`
- `news_risk_high->equity_24h` score `0.9896` n `109` status `ready` deltaP `28.6372` edge `1.0946` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.6058` n `109` status `ready` deltaP `12.6958` edge `0.02` maxDD `-0.9988`
- `news_risk_high->index_24h` score `-0.3055` n `109` status `ready` deltaP `0.8571` edge `0.1386` maxDD `-6.6786`
- `news_risk_high->index_1h` score `-0.4006` n `109` status `ready` deltaP `5.7559` edge `0.0017` maxDD `-0.8765`
- `news_risk_high->fx_1h` score `-0.5243` n `109` status `ready` deltaP `-0.662` edge `0.0007` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.7267` n `109` status `ready` deltaP `1.6371` edge `0.0187` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7345` n `109` status `ready` deltaP `-1.6559` edge `-0.0022` maxDD `-0.4745`
- `news_risk_high->crypto_alt_4h` score `-0.8883` n `109` status `ready` deltaP `1.0741` edge `0.1426` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.9175` n `109` status `ready` deltaP `-2.4433` edge `-0.0098` maxDD `-1.0293`
- `news_risk_high->equity_1h` score `-0.9559` n `109` status `ready` deltaP `0.4587` edge `0.0352` maxDD `-7.8651`
- `news_risk_high->crypto_major_4h` score `-1.0137` n `109` status `ready` deltaP `-1.9971` edge `0.0603` maxDD `-9.1553`
- `news_risk_high->fx_24h` score `-1.187` n `109` status `ready` deltaP `-13.4456` edge `0.0009` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.5053` n `109` status `ready` deltaP `-3.119` edge `-0.0041` maxDD `-4.7103`
- `news_risk_high->metal_4h` score `-1.8` n `109` status `ready` deltaP `-3.1942` edge `-0.0375` maxDD `-1.6299`
- `news_risk_high->commodity_1h` score `-2.9034` n `109` status `ready` deltaP `-14.5196` edge `-0.0085` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.0985` n `109` status `ready` deltaP `-0.0508` edge `-0.2073` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.3892` n `109` status `ready` deltaP `-27.6851` edge `-0.0291` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0731` n `109` status `ready` deltaP `-16.4376` edge `0.1813` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3095` n `109` status `ready` deltaP `-24.5469` edge `-0.0094` maxDD `-37.5528`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
