# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T16:07:28.107517+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3932`

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

- `news_risk_high->equity_4h` score `2.1994` n `106` status `ready` deltaP `15.2755` edge `0.2707` maxDD `-4.2454`
- `news_risk_high->equity_24h` score `1.0178` n `106` status `ready` deltaP `30.3943` edge `1.0865` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.8828` n `106` status `ready` deltaP `14.3609` edge `0.0256` maxDD `-0.4888`
- `news_risk_high->index_1h` score `-0.0885` n `106` status `ready` deltaP `7.2619` edge `0.0031` maxDD `-0.7111`
- `news_risk_high->index_24h` score `-0.2261` n `106` status `ready` deltaP `1.9651` edge `0.1414` maxDD `-6.6786`
- `news_risk_high->equity_1h` score `-0.4768` n `106` status `ready` deltaP `1.8868` edge `0.052` maxDD `-6.0569`
- `news_risk_high->fx_1h` score `-0.5336` n `106` status `ready` deltaP `-0.7174` edge `0.0003` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.7234` n `106` status `ready` deltaP `-0.7248` edge `0.0807` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.7317` n `106` status `ready` deltaP `1.6107` edge `0.1591` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.7621` n `106` status `ready` deltaP `1.4518` edge `0.0154` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7781` n `106` status `ready` deltaP `-2.4189` edge `-0.0027` maxDD `-0.4745`
- `news_risk_high->metal_1h` score `-0.7835` n `106` status `ready` deltaP `-1.5422` edge `-0.0081` maxDD `-0.7531`
- `news_risk_high->metal_4h` score `-1.0483` n `106` status `ready` deltaP `-1.8666` edge `-0.0314` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.2011` n `106` status `ready` deltaP `-14.0171` edge `0.0029` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.5507` n `106` status `ready` deltaP `-3.7595` edge `-0.0087` maxDD `-4.3033`
- `news_risk_high->commodity_1h` score `-2.9554` n `106` status `ready` deltaP `-15.0943` edge `-0.009` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-2.9778` n `106` status `ready` deltaP `1.8966` edge `-0.2048` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.4913` n `106` status `ready` deltaP `-28.7218` edge `-0.0307` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0808` n `106` status `ready` deltaP `-16.5241` edge `0.1809` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.1731` n `106` status `ready` deltaP `-24.3651` edge `-0.0114` maxDD `-36.5805`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
