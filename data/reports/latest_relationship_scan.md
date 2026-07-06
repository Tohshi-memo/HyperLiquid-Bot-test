# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T17:52:28.423755+00:00`
- Price records: `672`
- Market context records: `5902`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11166`

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

- `news_risk_high->fx_4h` score `3.6047` n `30` status `ready` deltaP `37.4085` edge `0.0556` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `1.9878` n `30` status `ready` deltaP `24.0818` edge `0.019` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.9322` n `30` status `ready` deltaP `11.3872` edge `0.0903` maxDD `-2.0691`
- `market_context_high->equity_4h` score `0.728` n `222` status `ready` deltaP `6.9312` edge `0.1239` maxDD `-4.0887`
- `news_risk_high->crypto_alt_1h` score `0.2325` n `30` status `ready` deltaP `5.1697` edge `0.0415` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.2344` n `222` status `ready` deltaP `4.6745` edge `0.0308` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.3606` n `222` status `ready` deltaP `2.7095` edge `0.0028` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4507` n `30` status `ready` deltaP `1.0878` edge `-0.0284` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.5007` n `222` status `ready` deltaP `-1.5092` edge `-0.0017` maxDD `-1.5283`
- `market_context_high->crypto_major_1h` score `-0.5798` n `222` status `ready` deltaP `3.4593` edge `0.0347` maxDD `-6.2348`
- `market_context_high->index_1h` score `-0.6344` n `222` status `ready` deltaP `0.0068` edge `0.0034` maxDD `-0.7819`
- `market_context_high->crypto_alt_1h` score `-0.67` n `222` status `ready` deltaP `2.5571` edge `0.0305` maxDD `-6.6758`
- `market_context_high->fx_1h` score `-0.8291` n `222` status `ready` deltaP `-2.8551` edge `-0.0012` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2245` n `30` status `ready` deltaP `-12.2455` edge `-0.0239` maxDD `-1.1161`
- `market_context_high->commodity_4h` score `-1.5991` n `222` status `ready` deltaP `-2.4267` edge `-0.0175` maxDD `-6.3734`
- `market_context_high->metal_4h` score `-1.7131` n `222` status `ready` deltaP `-3.5541` edge `-0.0327` maxDD `-5.725`
- `news_risk_high->commodity_4h` score `-1.8947` n `30` status `ready` deltaP `-14.9492` edge `-0.0557` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `-1.9509` n `222` status `ready` deltaP `8.0738` edge `0.1333` maxDD `-25.6458`
- `market_context_high->index_4h` score `-2.0569` n `222` status `ready` deltaP `-1.7523` edge `0.009` maxDD `-3.165`
- `market_context_high->fx_24h` score `-2.0886` n `215` status `ready` deltaP `1.4583` edge `0.0043` maxDD `-5.5435`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
