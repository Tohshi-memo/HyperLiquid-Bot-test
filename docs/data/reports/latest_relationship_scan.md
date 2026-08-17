# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T03:57:56.651908+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `market_context_high->commodity_24h` score `3.9437` n `69` status `ready` deltaP `34.6996` edge `0.1322` maxDD `-0.4576`
- `market_context_high->equity_24h` score `1.6895` n `69` status `ready` deltaP `16.3043` edge `0.053` maxDD `-0.6726`
- `market_context_high->crypto_major_24h` score `1.4801` n `69` status `ready` deltaP `2.2343` edge `0.2461` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4733` n `69` status `ready` deltaP `21.7014` edge `-0.0219` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.186` n `103` status `ready` deltaP `13.4842` edge `0.0575` maxDD `-0.8847`
- `market_context_high->metal_4h` score `-0.2366` n `103` status `ready` deltaP `16.0357` edge `0.0141` maxDD `-4.5909`
- `market_context_high->commodity_1h` score `-0.2756` n `111` status `ready` deltaP `0.1565` edge `0.0093` maxDD `-0.9873`
- `market_context_high->fx_1h` score `-0.3645` n `111` status `ready` deltaP `-1.199` edge `-0.0017` maxDD `-0.2968`
- `market_context_high->metal_1h` score `-0.5642` n `111` status `ready` deltaP `3.3083` edge `0.0025` maxDD `-1.7257`
- `market_context_high->crypto_major_4h` score `-0.6716` n `103` status `ready` deltaP `2.5796` edge `0.0175` maxDD `-4.6638`
- `market_context_high->fx_4h` score `-0.7607` n `103` status `ready` deltaP `-4.3526` edge `-0.0071` maxDD `-0.5796`
- `market_context_high->index_1h` score `-0.9019` n `111` status `ready` deltaP `-3.2839` edge `-0.0011` maxDD `-0.5064`
- `market_context_high->equity_1h` score `-1.0785` n `111` status `ready` deltaP `-5.0776` edge `-0.0213` maxDD `-3.3165`
- `market_context_high->crypto_alt_1h` score `-1.1215` n `111` status `ready` deltaP `-4.8026` edge `-0.0108` maxDD `-4.4101`
- `market_context_high->crypto_major_1h` score `-1.746` n `111` status `ready` deltaP `-4.0514` edge `-0.0181` maxDD `-4.0312`
- `market_context_high->index_4h` score `-1.8317` n `103` status `ready` deltaP `-10.0728` edge `-0.0046` maxDD `-0.8045`
- `market_context_high->fx_24h` score `-3.1573` n `69` status `ready` deltaP `-30.2763` edge `-0.0422` maxDD `-1.8596`
- `market_context_high->equity_4h` score `-3.3656` n `103` status `ready` deltaP `-17.8798` edge `-0.1316` maxDD `-8.1221`
- `market_context_high->metal_24h` score `-5.4988` n `69` status `ready` deltaP `-23.196` edge `-0.0524` maxDD `-7.0954`
- `market_context_high->crypto_alt_4h` score `-5.548` n `103` status `ready` deltaP `-8.1562` edge `-0.0398` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
