# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-09T04:37:28.319520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8902`

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

- `market_context_high->unknown_4h` score `40.09` n `91` status `ready` deltaP `-3.5965` edge `3.4187` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `12.7048` n `37` status `ready` deltaP `43.4451` edge `0.7691` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `11.4455` n `37` status `ready` deltaP `43.2226` edge `0.6724` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `10.7032` n `37` status `ready` deltaP `28.0781` edge `0.7147` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `9.8747` n `90` status `ready` deltaP `22.3611` edge `1.4143` maxDD `-16.7906`
- `market_context_high->equity_24h` score `9.2353` n `90` status `ready` deltaP `30.0` edge `0.6125` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.845` n `37` status `ready` deltaP `50.8681` edge `0.2313` maxDD `0.0`
- `news_risk_high->equity_4h` score `6.0793` n `37` status `ready` deltaP `32.1358` edge `0.3129` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5895` n `37` status `ready` deltaP `44.7058` edge `0.0889` maxDD `-0.025`
- `market_context_high->crypto_alt_24h` score `3.5493` n `90` status `ready` deltaP `14.0625` edge `0.9551` maxDD `-34.5048`
- `news_risk_high->crypto_major_1h` score `3.31` n `37` status `ready` deltaP `13.5257` edge `0.2212` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.6102` n `37` status `ready` deltaP `31.5383` edge `0.0162` maxDD `-0.0484`
- `news_risk_high->commodity_24h` score `2.3896` n `37` status `ready` deltaP `27.9279` edge `0.0214` maxDD `-0.0096`
- `news_risk_high->crypto_alt_1h` score `1.9735` n `37` status `ready` deltaP `0.7607` edge `0.1911` maxDD `-1.2034`
- `market_context_high->crypto_major_4h` score `1.8238` n `91` status `ready` deltaP `17.8588` edge `0.2478` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.0798` n `90` status `ready` deltaP `19.2361` edge `0.1587` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `0.9145` n `37` status `ready` deltaP `13.4229` edge `0.0283` maxDD `-0.993`
- `news_risk_high->metal_1h` score `0.5529` n `37` status `ready` deltaP `8.711` edge `0.0185` maxDD `-0.44`
- `market_context_high->fx_1h` score `0.3877` n `91` status `ready` deltaP `8.1941` edge `0.0019` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.336` n `91` status `ready` deltaP `13.8569` edge `0.0103` maxDD `-0.3077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
