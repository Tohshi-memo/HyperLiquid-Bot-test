# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T06:52:24.601640+00:00`
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

- `market_context_high->unknown_24h` score `1044.5469` n `111` status `ready` deltaP `10.4542` edge `87.0139` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `31.304` n `111` status `ready` deltaP `-1.2222` edge `2.6707` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.8744` n `62` status `ready` deltaP `34.6184` edge `0.6124` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.5555` n `62` status `ready` deltaP `22.0201` edge `0.5339` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.7016` n `111` status `ready` deltaP `17.4577` edge `0.2885` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.2977` n `62` status `ready` deltaP `23.6111` edge `0.1174` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8384` n `62` status `ready` deltaP `31.8499` edge `0.0504` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.1371` n `62` status `ready` deltaP `4.3123` edge `0.1593` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `2.0656` n `62` status `ready` deltaP `7.4802` edge `0.1578` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9409` n `62` status `ready` deltaP `24.5751` edge `0.0129` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.8064` n `62` status `ready` deltaP `17.0142` edge `0.0969` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.6362` n `111` status `ready` deltaP `1.5464` edge `0.2984` maxDD `-7.1222`
- `news_risk_high->metal_4h` score `1.3689` n `62` status `ready` deltaP `19.5712` edge `0.0866` maxDD `-0.993`
- `market_context_high->crypto_major_24h` score `1.1212` n `111` status `ready` deltaP `7.8782` edge `0.3886` maxDD `-16.7906`
- `news_risk_high->crypto_alt_1h` score `0.9763` n `62` status `ready` deltaP `2.5594` edge `0.1162` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8837` n `111` status `ready` deltaP `19.5768` edge `0.0188` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.8001` n `111` status `ready` deltaP `13.5095` edge `0.005` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.6696` n `62` status `ready` deltaP `27.369` edge `0.06` maxDD `-8.196`
- `market_context_high->commodity_4h` score `0.3274` n `111` status `ready` deltaP `10.3329` edge `0.0284` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1827` n `111` status `ready` deltaP `6.4547` edge `0.0112` maxDD `-0.4536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
