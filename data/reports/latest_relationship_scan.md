# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T01:22:27.838993+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4148`

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

- `news_risk_high->equity_4h` score `0.9819` n `69` status `ready` deltaP `7.8937` edge `0.1555` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.6972` n `69` status `ready` deltaP `12.7761` edge `0.0207` maxDD `-0.4888`
- `news_risk_high->index_24h` score `0.3` n `69` status `ready` deltaP `8.907` edge `0.1459` maxDD `-6.6786`
- `news_risk_high->index_1h` score `0.0147` n `69` status `ready` deltaP `6.6172` edge `0.0031` maxDD `-0.2931`
- `news_risk_high->fx_4h` score `-0.1254` n `69` status `ready` deltaP `3.7822` edge `0.0033` maxDD `-0.2336`
- `news_risk_high->equity_1h` score `-0.1363` n `69` status `ready` deltaP `-1.1737` edge `0.0453` maxDD `-1.396`
- `news_risk_high->fx_24h` score `-0.2011` n `69` status `ready` deltaP `-3.5855` edge `0.0514` maxDD `-0.2073`
- `news_risk_high->fx_1h` score `-0.3175` n `69` status `ready` deltaP `-0.5684` edge `0.0017` maxDD `-0.0888`
- `news_risk_high->metal_1h` score `-0.5071` n `69` status `ready` deltaP `-3.3715` edge `-0.0068` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-1.2413` n `69` status `ready` deltaP `-4.2285` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_major_1h` score `-2.2138` n `69` status `ready` deltaP `-8.3247` edge `-0.0351` maxDD `-4.1772`
- `news_risk_high->commodity_1h` score `-2.2844` n `69` status `ready` deltaP `-15.2651` edge `-0.0051` maxDD `-1.3464`
- `news_risk_high->crypto_major_4h` score `-2.5622` n `69` status `ready` deltaP `-6.524` edge `-0.0096` maxDD `-8.5004`
- `news_risk_high->crypto_alt_1h` score `-2.5759` n `69` status `ready` deltaP `-6.2766` edge `-0.053` maxDD `-5.5851`
- `news_risk_high->crypto_alt_4h` score `-2.8491` n `69` status `ready` deltaP `-7.8959` edge `-0.0506` maxDD `-13.9624`
- `news_risk_high->metal_24h` score `-3.4608` n `69` status `ready` deltaP `-1.8569` edge `-0.2417` maxDD `-8.5019`
- `news_risk_high->equity_24h` score `-3.5817` n `69` status `ready` deltaP `23.211` edge `0.5447` maxDD `-86.0244`
- `news_risk_high->commodity_4h` score `-4.5827` n `69` status `ready` deltaP `-31.6941` edge `-0.0108` maxDD `-4.1171`
- `news_risk_high->commodity_24h` score `-10.2559` n `69` status `ready` deltaP `-29.2119` edge `-0.092` maxDD `-28.0997`
- `news_risk_high->crypto_major_24h` score `-13.3484` n `69` status `ready` deltaP `-29.1969` edge `-0.0674` maxDD `-50.6925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
