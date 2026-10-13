# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T03:52:27.514484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9686`

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

- `risk_on_high->crypto_alt_4h` score `5.5859` n `51` status `ready` deltaP `20.11` edge `0.3762` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.5859` n `51` status `ready` deltaP `20.11` edge `0.3762` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3254` n `45` status `ready` deltaP `30.087` edge `0.2432` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3254` n `45` status `ready` deltaP `30.087` edge `0.2432` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.7373` n `51` status `ready` deltaP `36.0324` edge `0.4524` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.7373` n `51` status `ready` deltaP `36.0324` edge `0.4524` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `4.7112` n `103` status `ready` deltaP `15.5222` edge `0.434` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `4.4754` n `103` status `ready` deltaP `19.7179` edge `0.3974` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.7607` n `115` status `ready` deltaP `13.1216` edge `0.166` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4172` n `115` status `ready` deltaP `7.2989` edge `0.15` maxDD `-3.7781`
- `market_context_high->unknown_4h` score `0.4302` n `103` status `ready` deltaP `-4.3822` edge `0.1297` maxDD `-1.8373`
- `market_context_high->fx_1h` score `-0.2526` n `115` status `ready` deltaP `2.1987` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_4h` score `-0.5333` n `103` status `ready` deltaP `7.7389` edge `0.0085` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.5622` n `115` status `ready` deltaP `5.4738` edge `0.0036` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5839` n `115` status `ready` deltaP `0.3474` edge `-0.0024` maxDD `-1.3154`
- `risk_on_high->crypto_major_1h` score `-0.6114` n `52` status `ready` deltaP `1.6467` edge `0.0103` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.6114` n `52` status `ready` deltaP `1.6467` edge `0.0103` maxDD `-3.7781`
- `risk_on_high->fx_1h` score `-0.6326` n `52` status `ready` deltaP `-1.5304` edge `-0.0045` maxDD `-0.3742`
- `risk_on_and_context->fx_1h` score `-0.6326` n `52` status `ready` deltaP `-1.5304` edge `-0.0045` maxDD `-0.3742`
- `risk_on_high->metal_1h` score `-0.6562` n `52` status `ready` deltaP `-1.0479` edge `-0.004` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
