# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T11:22:27.105273+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `49.5782` n `56` status `ready` deltaP `14.2857` edge `4.0908` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.2891` n `56` status `ready` deltaP `36.4087` edge `2.002` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.4673` n `109` status `ready` deltaP `17.6606` edge `0.6611` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2939` n `80` status `ready` deltaP `10.9756` edge `0.5103` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.0116` n `109` status `ready` deltaP `30.7833` edge `0.231` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.9259` n `109` status `ready` deltaP `18.5444` edge `0.1609` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6907` n `80` status `ready` deltaP `5.6737` edge `0.2221` maxDD `-0.8558`
- `news_risk_high->equity_24h` score `2.6131` n `56` status `ready` deltaP `23.2639` edge `0.3691` maxDD `-12.4677`
- `news_risk_high->fx_4h` score `2.3925` n `80` status `ready` deltaP `34.8171` edge `0.0222` maxDD `-0.3953`
- `news_risk_high->crypto_major_24h` score `2.1497` n `56` status `ready` deltaP `19.6181` edge `0.3847` maxDD `-16.524`
- `news_risk_high->metal_24h` score `1.684` n `56` status `ready` deltaP `36.6319` edge `0.0431` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.3741` n `56` status `ready` deltaP `19.5436` edge `0.0262` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.0515` n `119` status `ready` deltaP `8.7619` edge `0.0784` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.7495` n `80` status `ready` deltaP `14.3413` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4338` n `80` status `ready` deltaP `12.3503` edge `0.0053` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.3018` n `109` status `ready` deltaP `6.7535` edge `0.008` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.4066` n `80` status `ready` deltaP `0.0075` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.5206` n `80` status `ready` deltaP `2.0732` edge `-0.0164` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.6265` n `80` status `ready` deltaP `6.5854` edge `0.0099` maxDD `-2.0635`
- `market_context_high->crypto_major_4h` score `-0.6309` n `109` status `ready` deltaP `14.2202` edge `0.1977` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
