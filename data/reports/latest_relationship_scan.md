# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T03:07:29.594444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `risk_on_high->crypto_alt_4h` score `5.3299` n `48` status `ready` deltaP `20.6301` edge `0.3514` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.3299` n `48` status `ready` deltaP `20.6301` edge `0.3514` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.1874` n `42` status `ready` deltaP `30.087` edge `0.2317` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.1874` n `42` status `ready` deltaP `30.087` edge `0.2317` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `4.6281` n `100` status `ready` deltaP `15.7134` edge `0.4258` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `4.2216` n `48` status `ready` deltaP `35.2643` edge `0.3914` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2216` n `48` status `ready` deltaP `35.2643` edge `0.3914` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `4.1042` n `100` status `ready` deltaP `19.0976` edge `0.3706` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.5781` n `112` status `ready` deltaP `12.639` edge `0.154` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.2681` n `112` status `ready` deltaP `6.5601` edge `0.1425` maxDD `-3.7781`
- `market_context_high->metal_4h` score `-0.3468` n `100` status `ready` deltaP `8.6098` edge `0.009` maxDD `-1.624`
- `market_context_high->fx_1h` score `-0.3488` n `112` status `ready` deltaP `1.161` edge `0.0012` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4284` n `112` status `ready` deltaP `4.4589` edge `0.0023` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.5371` n `52` status `ready` deltaP `2.0958` edge `0.0135` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.5371` n `52` status `ready` deltaP `2.0958` edge `0.0135` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `-0.5547` n `100` status `ready` deltaP `-4.9939` edge `0.0517` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.5787` n `112` status `ready` deltaP `-0.134` edge `-0.0031` maxDD `-1.2829`
- `risk_on_high->fx_1h` score `-0.6169` n `52` status `ready` deltaP `-1.3802` edge `-0.0042` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6169` n `52` status `ready` deltaP `-1.3802` edge `-0.0042` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6461` n `52` status `ready` deltaP `-0.8982` edge `-0.0037` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
