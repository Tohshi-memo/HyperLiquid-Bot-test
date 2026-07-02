# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T16:24:11.732502+00:00`
- Price records: `672`
- Market context records: `5472`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11462`

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

- `market_context_high->crypto_major_24h` score `3.5607` n `193` status `ready` deltaP `16.628` edge `0.6399` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `2.3523` n `196` status `ready` deltaP `14.0213` edge `0.3318` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.2466` n `196` status `ready` deltaP `12.4626` edge `0.268` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.945` n `196` status `ready` deltaP `10.1045` edge `0.2588` maxDD `-9.46`
- `market_context_high->equity_24h` score `0.6614` n `193` status `ready` deltaP `9.3012` edge `0.501` maxDD `-31.6316`
- `market_context_high->equity_1h` score `0.4746` n `196` status `ready` deltaP `8.4413` edge `0.0798` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.1762` n `196` status `ready` deltaP `6.9932` edge `0.0174` maxDD `-0.9472`
- `market_context_high->fx_24h` score `0.1042` n `193` status `ready` deltaP `10.3807` edge `0.0322` maxDD `-1.0847`
- `market_context_high->fx_1h` score `-0.3259` n `196` status `ready` deltaP `1.0204` edge `0.0003` maxDD `-0.577`
- `market_context_high->metal_1h` score `-0.3999` n `196` status `ready` deltaP `3.0887` edge `0.0136` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5164` n `196` status `ready` deltaP `0.4827` edge `0.0499` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.6945` n `196` status `ready` deltaP `1.7964` edge `0.0547` maxDD `-6.9639`
- `market_context_high->index_4h` score `-0.8558` n `196` status `ready` deltaP `7.3357` edge `0.0407` maxDD `-2.874`
- `market_context_high->fx_4h` score `-0.9951` n `196` status `ready` deltaP `2.2182` edge `0.0048` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4655` n `196` status `ready` deltaP `-2.9451` edge `-0.0077` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8962` n `193` status `ready` deltaP `13.1827` edge `0.0677` maxDD `-16.8946`
- `market_context_high->commodity_4h` score `-4.21` n `196` status `ready` deltaP `-5.5033` edge `-0.0427` maxDD `-14.3822`
- `market_context_high->metal_4h` score `-4.2159` n `196` status `ready` deltaP `-9.1899` edge `-0.0376` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-7.0787` n `193` status `ready` deltaP `7.8332` edge `0.2276` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.081` n `193` status `ready` deltaP `-3.3543` edge `-0.1477` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
