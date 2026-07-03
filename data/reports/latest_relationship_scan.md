# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T19:07:39.656261+00:00`
- Price records: `672`
- Market context records: `5586`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11423`

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

- `market_context_high->equity_24h` score `3.9295` n `174` status `ready` deltaP `15.0084` edge `0.7353` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `1.1716` n `201` status `ready` deltaP `11.772` edge `0.2484` maxDD `-14.0065`
- `market_context_high->fx_24h` score `0.9826` n `174` status `ready` deltaP `18.8338` edge `0.0537` maxDD `-1.457`
- `market_context_high->equity_4h` score `0.5728` n `201` status `ready` deltaP `6.0596` edge `0.1712` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.5301` n `201` status `ready` deltaP `6.7733` edge `0.1631` maxDD `-9.46`
- `market_context_high->crypto_major_24h` score `0.3538` n `174` status `ready` deltaP `12.9311` edge `0.3973` maxDD `-29.6555`
- `market_context_high->equity_1h` score `-0.1799` n `213` status `ready` deltaP `6.1539` edge `0.0366` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2597` n `213` status `ready` deltaP `3.0446` edge `0.0074` maxDD `-0.9472`
- `market_context_high->fx_1h` score `-0.3025` n `213` status `ready` deltaP `1.0852` edge `0.0008` maxDD `-0.4122`
- `market_context_high->crypto_major_1h` score `-0.4252` n `213` status `ready` deltaP `3.5007` edge `0.0467` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5687` n `213` status `ready` deltaP `-0.8539` edge `0.0003` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.627` n `201` status `ready` deltaP `4.3661` edge `0.0087` maxDD `-0.8712`
- `market_context_high->crypto_alt_1h` score `-0.6497` n `213` status `ready` deltaP `0.5271` edge `0.0385` maxDD `-5.0257`
- `market_context_high->commodity_1h` score `-1.2375` n `213` status `ready` deltaP `-2.7115` edge `-0.0085` maxDD `-3.7906`
- `market_context_high->index_4h` score `-1.528` n `201` status `ready` deltaP `2.8334` edge `0.0147` maxDD `-2.874`
- `market_context_high->index_24h` score `-2.188` n `174` status `ready` deltaP `11.6499` edge `0.0405` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0085` n `201` status `ready` deltaP `-13.0718` edge `-0.0602` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.2233` n `201` status `ready` deltaP `-5.4734` edge `-0.0479` maxDD `-14.071`
- `market_context_high->metal_24h` score `-7.9818` n `174` status `ready` deltaP `-8.3273` edge `-0.2317` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-9.7463` n `174` status `ready` deltaP `2.7179` edge `0.0394` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
