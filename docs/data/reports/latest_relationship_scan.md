# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T12:37:31.796285+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8366`

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

- `market_context_high->unknown_4h` score `40.0824` n `149` status `ready` deltaP `-0.311` edge `3.3656` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.9611` n `52` status `ready` deltaP `-7.5516` edge `1.2363` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.9611` n `52` status `ready` deltaP `-7.5516` edge `1.2363` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8461` n `52` status `ready` deltaP `49.8264` edge `0.405` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8461` n `52` status `ready` deltaP `49.8264` edge `0.405` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.547` n `149` status `ready` deltaP `43.115` edge `0.394` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.1984` n `94` status `ready` deltaP `21.2572` edge `0.4834` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8195` n `52` status `ready` deltaP `32.5399` edge `0.053` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7192` n `149` status `ready` deltaP `29.0422` edge `0.0748` maxDD `-0.345`
- `market_context_high->commodity_1h` score `1.087` n `149` status `ready` deltaP `15.9115` edge `0.0222` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.7776` n `52` status `ready` deltaP `17.0005` edge `-0.0443` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.7776` n `52` status `ready` deltaP `17.0005` edge `-0.0443` maxDD `-0.0054`
- `news_risk_high->equity_4h` score `0.7361` n `94` status `ready` deltaP `12.3021` edge `0.0982` maxDD `-3.5339`
- `market_context_high->fx_24h` score `0.6428` n `149` status `ready` deltaP `14.2256` edge `-0.0197` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.4637` n `52` status `ready` deltaP `8.9936` edge `0.0139` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4637` n `52` status `ready` deltaP `8.9936` edge `0.0139` maxDD `-0.1507`
- `news_risk_high->crypto_major_4h` score `0.4385` n `94` status `ready` deltaP `13.2103` edge `0.2928` maxDD `-19.972`
- `news_risk_high->equity_1h` score `0.3177` n `95` status `ready` deltaP `10.2899` edge `0.0243` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2863` n `94` status `ready` deltaP `8.4847` edge `0.0248` maxDD `-0.2398`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
