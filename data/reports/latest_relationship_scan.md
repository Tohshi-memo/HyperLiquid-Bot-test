# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T23:52:25.800783+00:00`
- Price records: `672`
- Market context records: `7303`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13813`

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

- `market_context_high->fx_1h` score `-0.0992` n `126` status `ready` deltaP `5.148` edge `0.0019` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.559` n `126` status `ready` deltaP `-0.4719` edge `-0.0113` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.6558` n `126` status `ready` deltaP `-1.1382` edge `0.0274` maxDD `-5.9775`
- `market_context_high->commodity_4h` score `-0.7396` n `121` status `ready` deltaP `2.0737` edge `-0.0118` maxDD `-2.4139`
- `market_context_high->fx_24h` score `-0.8388` n `115` status `ready` deltaP `1.913` edge `0.0025` maxDD `-2.1564`
- `market_context_high->fx_4h` score `-0.9761` n `121` status `ready` deltaP `3.5914` edge `0.0109` maxDD `-1.4649`
- `market_context_high->crypto_major_1h` score `-1.0942` n `126` status `ready` deltaP `3.4146` edge `0.0271` maxDD `-7.6171`
- `market_context_high->index_1h` score `-1.2965` n `126` status `ready` deltaP `-5.2124` edge `-0.0091` maxDD `-2.1355`
- `market_context_high->unknown_4h` score `-1.3771` n `121` status `ready` deltaP `5.3871` edge `0.0852` maxDD `-6.2031`
- `market_context_high->unknown_1h` score `-1.7324` n `126` status `ready` deltaP `0.8079` edge `-0.0874` maxDD `-1.3217`
- `market_context_high->crypto_alt_4h` score `-1.9203` n `121` status `ready` deltaP `2.7476` edge `0.0098` maxDD `-15.2776`
- `market_context_high->metal_1h` score `-2.1729` n `126` status `ready` deltaP `-10.0941` edge `-0.0034` maxDD `-1.4971`
- `market_context_high->metal_4h` score `-2.3996` n `121` status `ready` deltaP `-8.558` edge `-0.0024` maxDD `-4.8549`
- `market_context_high->crypto_major_4h` score `-2.8665` n `121` status `ready` deltaP `3.3499` edge `-0.0004` maxDD `-23.4879`
- `market_context_high->unknown_24h` score `-3.1033` n `116` status `ready` deltaP `-7.7706` edge `-0.0367` maxDD `-12.7487`
- `market_context_high->commodity_24h` score `-3.4721` n `115` status `ready` deltaP `-6.9565` edge `-0.1632` maxDD `-2.3815`
- `market_context_high->equity_1h` score `-4.4009` n `126` status `ready` deltaP `-9.1806` edge `-0.0679` maxDD `-14.3442`
- `market_context_high->index_4h` score `-4.516` n `121` status `ready` deltaP `-13.2143` edge `-0.0487` maxDD `-8.8298`
- `market_context_high->crypto_alt_24h` score `-8.9947` n `116` status `ready` deltaP `3.1728` edge `-0.2589` maxDD `-63.2332`
- `market_context_high->metal_24h` score `-10.775` n `116` status `ready` deltaP `-28.2388` edge `-0.1244` maxDD `-20.154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
