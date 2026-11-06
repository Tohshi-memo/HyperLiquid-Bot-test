# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T17:07:28.875090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4054`

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

- `news_risk_high->equity_4h` score `2.5516` n `102` status `ready` deltaP `17.8653` edge `0.2986` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0195` n `102` status `ready` deltaP `15.6654` edge `0.0283` maxDD `-0.4888`
- `news_risk_high->equity_24h` score `0.9055` n `102` status `ready` deltaP `30.5434` edge `1.0711` maxDD `-86.0244`
- `news_risk_high->index_1h` score `0.1345` n `102` status `ready` deltaP `9.1082` edge `0.0046` maxDD `-0.5128`
- `news_risk_high->equity_1h` score `0.0419` n `102` status `ready` deltaP `3.4725` edge `0.0685` maxDD `-3.9024`
- `news_risk_high->index_24h` score `-0.176` n `102` status `ready` deltaP `3.6022` edge `0.1448` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.387` n `102` status `ready` deltaP `-1.4001` edge `-0.0003` maxDD `-0.1984`
- `news_risk_high->crypto_major_4h` score `-0.4835` n `102` status `ready` deltaP `0.7831` edge `0.1014` maxDD `-9.1553`
- `news_risk_high->crypto_alt_4h` score `-0.6214` n `102` status `ready` deltaP `1.7217` edge `0.1725` maxDD `-14.0916`
- `news_risk_high->metal_1h` score `-0.7268` n `102` status `ready` deltaP `-1.5792` edge `-0.0078` maxDD `-0.7125`
- `news_risk_high->crypto_alt_1h` score `-0.7421` n `102` status `ready` deltaP `1.2651` edge `0.0192` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.7984` n `102` status `ready` deltaP `-2.72` edge `-0.0033` maxDD `-0.4745`
- `news_risk_high->metal_4h` score `-0.9231` n `102` status `ready` deltaP `0.0897` edge `-0.0284` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.1844` n `102` status `ready` deltaP `-14.1996` edge `0.0059` maxDD `-0.3804`
- `news_risk_high->crypto_major_1h` score `-1.4344` n `102` status `ready` deltaP `-3.3375` edge `-0.0034` maxDD `-4.1772`
- `news_risk_high->metal_24h` score `-2.8723` n `102` status `ready` deltaP `3.7448` edge `-0.2036` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.198` n `102` status `ready` deltaP `-17.6471` edge `-0.0122` maxDD `-3.2657`
- `news_risk_high->commodity_4h` score `-5.2336` n `102` status `ready` deltaP `-28.0188` edge `-0.0288` maxDD `-8.9765`
- `news_risk_high->crypto_major_24h` score `-6.0109` n `102` status `ready` deltaP `-15.4213` edge `0.1825` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.0234` n `102` status `ready` deltaP `-24.6798` edge `-0.014` maxDD `-35.2065`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
