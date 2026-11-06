# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T16:52:29.871440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4038`

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

- `news_risk_high->equity_4h` score `2.4998` n `103` status `ready` deltaP `17.199` edge `0.2964` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0446` n `103` status `ready` deltaP `15.9795` edge `0.0283` maxDD `-0.4888`
- `news_risk_high->equity_24h` score `0.9875` n `103` status `ready` deltaP `30.7718` edge `1.0801` maxDD `-86.0244`
- `news_risk_high->index_1h` score `0.1051` n `103` status `ready` deltaP `8.7059` edge `0.0042` maxDD `-0.5675`
- `news_risk_high->equity_1h` score `-0.0779` n `103` status `ready` deltaP `3.0987` edge `0.0636` maxDD `-4.5394`
- `news_risk_high->index_24h` score `-0.137` n `103` status `ready` deltaP `3.2424` edge `0.1443` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.4067` n `103` status `ready` deltaP `-1.7644` edge `-0.0004` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.5139` n `103` status `ready` deltaP `0.4691` edge `0.0996` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.5922` n `103` status `ready` deltaP `2.1786` edge `0.1732` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.7568` n `103` status `ready` deltaP `0.9389` edge `0.0195` maxDD `-5.8225`
- `news_risk_high->metal_1h` score `-0.8204` n `103` status `ready` deltaP `-2.0551` edge `-0.008` maxDD `-0.733`
- `news_risk_high->fx_4h` score `-0.8277` n `103` status `ready` deltaP `-3.2531` edge `-0.0035` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.9521` n `103` status `ready` deltaP `-0.4529` edge `-0.0285` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.226` n `103` status `ready` deltaP `-14.7802` edge `0.0048` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-1.4603` n `103` status `ready` deltaP `-3.6161` edge `-0.0037` maxDD `-4.1772`
- `news_risk_high->metal_24h` score `-2.9128` n `103` status `ready` deltaP `3.0405` edge `-0.2041` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.1347` n `103` status `ready` deltaP `-16.9903` edge `-0.0113` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.3102` n `103` status `ready` deltaP `-28.1997` edge `-0.0306` maxDD `-9.247`
- `news_risk_high->crypto_major_24h` score `-6.0034` n `103` status `ready` deltaP `-15.7258` edge `0.1855` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.0695` n `103` status `ready` deltaP `-24.5731` edge `-0.0136` maxDD `-35.6027`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
