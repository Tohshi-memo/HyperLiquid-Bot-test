# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T11:37:26.460197+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11560`

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

- `news_risk_high->unknown_24h` score `49.6569` n `56` status `ready` deltaP `14.4593` edge `4.0962` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.3335` n `56` status `ready` deltaP `36.4087` edge `2.0057` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.4649` n `108` status `ready` deltaP `17.7662` edge `0.6602` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2939` n `80` status `ready` deltaP `10.9756` edge `0.5103` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.0467` n `108` status `ready` deltaP `30.7871` edge `0.2339` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.973` n `108` status `ready` deltaP `18.383` edge `0.1659` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6895` n `80` status `ready` deltaP `5.6737` edge `0.222` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.6447` n `56` status `ready` deltaP `23.4375` edge `0.372` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.1954` n `56` status `ready` deltaP `19.7917` edge `0.3894` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.7031` n `56` status `ready` deltaP `36.8056` edge `0.0444` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.3916` n `56` status `ready` deltaP `19.7172` edge `0.0265` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0551` n `119` status `ready` deltaP `8.7619` edge `0.0787` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7615` n `80` status `ready` deltaP `14.491` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.426` n `80` status `ready` deltaP `12.2006` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3202` n `108` status `ready` deltaP `6.4307` edge `0.0078` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.4066` n `80` status `ready` deltaP `0.0075` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`
- `market_context_high->crypto_major_4h` score `-0.5269` n `108` status `ready` deltaP `14.8148` edge `0.2024` maxDD `-20.9394`
- `news_risk_high->commodity_4h` score `-0.6352` n `80` status `ready` deltaP `6.4329` edge `0.0098` maxDD `-2.0635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
