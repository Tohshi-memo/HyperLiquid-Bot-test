# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T11:52:33.577929+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4012`

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

- `news_risk_high->index_4h` score `-0.4159` n `123` status `ready` deltaP `7.2155` edge `0.0117` maxDD `-2.3836`
- `news_risk_high->crypto_alt_4h` score `-0.4175` n `123` status `ready` deltaP `5.5386` edge `0.1732` maxDD `-14.0916`
- `news_risk_high->equity_24h` score `-0.4302` n `123` status `ready` deltaP `20.352` edge `0.9678` maxDD `-86.0244`
- `news_risk_high->index_1h` score `-0.4706` n `123` status `ready` deltaP `5.0265` edge `0.0017` maxDD `-0.9544`
- `news_risk_high->fx_1h` score `-0.6011` n `123` status `ready` deltaP `-3.6354` edge `-0.0019` maxDD `-0.4079`
- `news_risk_high->index_24h` score `-0.7929` n `123` status `ready` deltaP `-4.9905` edge `0.1151` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.8134` n `123` status `ready` deltaP `-0.3006` edge `0.0205` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.8822` n `123` status `ready` deltaP `-4.0143` edge `-0.0043` maxDD `-0.5631`
- `news_risk_high->metal_1h` score `-1.4099` n `123` status `ready` deltaP `-4.8355` edge `-0.0155` maxDD `-1.914`
- `news_risk_high->fx_24h` score `-1.5002` n `123` status `ready` deltaP `-17.6569` edge `-0.0098` maxDD `-0.5191`
- `news_risk_high->equity_1h` score `-1.6183` n `123` status `ready` deltaP `-2.5461` edge `0.012` maxDD `-11.2005`
- `news_risk_high->crypto_major_4h` score `-1.8397` n `123` status `ready` deltaP `-4.0651` edge `0.0549` maxDD `-9.1553`
- `news_risk_high->crypto_major_1h` score `-1.9815` n `123` status `ready` deltaP `-5.0935` edge `-0.0145` maxDD `-5.6667`
- `news_risk_high->commodity_1h` score `-2.91` n `123` status `ready` deltaP `-14.6767` edge `-0.008` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-3.2544` n `123` status `ready` deltaP `-8.2317` edge `-0.0546` maxDD `-4.2709`
- `news_risk_high->equity_4h` score `-4.0808` n `123` status `ready` deltaP `7.6728` edge `0.0749` maxDD `-30.2897`
- `news_risk_high->commodity_4h` score `-4.6097` n `123` status `ready` deltaP `-20.7317` edge `-0.0105` maxDD `-9.5011`
- `news_risk_high->metal_24h` score `-5.6243` n `123` status `ready` deltaP `-7.2425` edge `-0.2308` maxDD `-8.5019`
- `news_risk_high->commodity_24h` score `-10.2661` n `123` status `ready` deltaP `-22.8556` edge `0.0207` maxDD `-40.5737`
- `news_risk_high->crypto_major_24h` score `-10.5486` n `123` status `ready` deltaP `-18.6035` edge `0.0953` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
