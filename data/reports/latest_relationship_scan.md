# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T07:52:28.520507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `813.721` n `107` status `ready` deltaP `9.7806` edge `67.7829` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `32.5131` n `107` status `ready` deltaP `-1.9631` edge `2.7764` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8756` n `62` status `ready` deltaP `34.6184` edge `0.6125` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5891` n `62` status `ready` deltaP `22.0201` edge `0.5367` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5973` n `107` status `ready` deltaP `16.5147` edge `0.2861` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3844` n `62` status `ready` deltaP `24.3056` edge `0.12` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8554` n `62` status `ready` deltaP `32.0024` edge `0.0508` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.2971` n `62` status `ready` deltaP `5.0067` edge `0.168` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0044` n `62` status `ready` deltaP `7.1808` edge `0.1547` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9648` n `62` status `ready` deltaP `24.8745` edge `0.0129` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8538` n `62` status `ready` deltaP `17.4715` edge `0.0978` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4004` n `62` status `ready` deltaP `20.0285` edge `0.0876` maxDD `-0.993`
- `market_context_high->crypto_alt_4h` score `1.391` n `107` status `ready` deltaP `-0.0029` edge `0.2883` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.0375` n `107` status `ready` deltaP `7.3939` edge `0.3811` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.8684` n `62` status `ready` deltaP `1.9606` edge `0.1112` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.8357` n `107` status `ready` deltaP `13.3289` edge `0.005` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.8217` n `107` status `ready` deltaP `18.9067` edge `0.0181` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.5718` n `62` status `ready` deltaP `26.6746` edge `0.0521` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.3347` n `107` status `ready` deltaP `10.889` edge `0.0592` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.2372` n `107` status `ready` deltaP `6.8233` edge `0.0124` maxDD `-0.3829`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
