# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T07:22:32.051968+00:00`
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

- `market_context_high->unknown_24h` score `931.2813` n `109` status `ready` deltaP `10.1236` edge `77.5773` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `31.8557` n `109` status `ready` deltaP `-1.5859` edge `2.7191` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.872` n `62` status `ready` deltaP `34.6184` edge `0.6122` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5723` n `62` status `ready` deltaP `22.0201` edge `0.5353` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.6585` n `109` status `ready` deltaP `16.9948` edge `0.288` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.3399` n `62` status `ready` deltaP `23.9583` edge `0.1186` maxDD `0.0`
- `news_risk_high->index_4h` score `2.853` n `62` status `ready` deltaP `32.0024` edge `0.0506` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.2105` n `62` status `ready` deltaP `4.6595` edge `0.1631` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0248` n `62` status `ready` deltaP `7.1808` edge `0.1564` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9528` n `62` status `ready` deltaP `24.7248` edge `0.0129` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.821` n `62` status `ready` deltaP `17.1666` edge `0.0971` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.513` n `109` status `ready` deltaP `0.786` edge `0.2932` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3886` n `62` status `ready` deltaP `19.876` edge `0.0871` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.0818` n `109` status `ready` deltaP `7.6468` edge `0.3851` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.926` n `62` status `ready` deltaP `2.26` edge `0.114` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8543` n `109` status `ready` deltaP `19.2535` edge `0.0185` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7529` n `109` status `ready` deltaP `12.9649` edge `0.0047` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.6203` n `62` status `ready` deltaP `27.0218` edge `0.056` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.2551` n `109` status `ready` deltaP `9.6386` edge `0.027` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2219` n `109` status `ready` deltaP `6.7118` edge `0.0122` maxDD `-0.4094`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
