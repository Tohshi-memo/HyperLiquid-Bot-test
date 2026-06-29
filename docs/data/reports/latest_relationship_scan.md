# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T15:07:29.126141+00:00`
- Price records: `672`
- Market context records: `5155`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5612`

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

- `market_context_high->unknown_24h` score `30.2962` n `63` status `ready` deltaP `34.4494` edge `2.314` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.409` n `132` status `ready` deltaP `19.831` edge `0.5041` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.1047` n `143` status `ready` deltaP `10.3409` edge `0.4206` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.0123` n `132` status `ready` deltaP `15.3317` edge `0.4754` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.9507` n `63` status `ready` deltaP `19.8909` edge `0.8408` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.7523` n `63` status `ready` deltaP `18.0803` edge `0.8549` maxDD `-22.6266`
- `market_context_high->crypto_major_4h` score `4.0269` n `132` status `ready` deltaP `13.9689` edge `0.4717` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0117` n `63` status `ready` deltaP `20.2381` edge `0.156` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9691` n `63` status `ready` deltaP `0.9424` edge `0.2488` maxDD `-5.4668`
- `market_context_high->equity_4h` score `0.8015` n `132` status `ready` deltaP `9.8485` edge `0.165` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.7207` n `143` status `ready` deltaP `7.3364` edge `0.1357` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7027` n `143` status `ready` deltaP `4.892` edge `0.1221` maxDD `-5.0257`
- `market_context_high->equity_1h` score `-0.0105` n `143` status `ready` deltaP `6.4916` edge `0.0519` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.054` n `143` status `ready` deltaP `5.2406` edge `0.0154` maxDD `-1.9139`
- `market_context_high->index_1h` score `-0.1407` n `143` status `ready` deltaP `3.2453` edge `0.0107` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2009` n `143` status `ready` deltaP `2.8475` edge `0.0005` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.3705` n `132` status `ready` deltaP `5.0305` edge `0.0307` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4041` n `63` status `ready` deltaP `7.0437` edge `0.0089` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.5779` n `132` status `ready` deltaP `3.4645` edge `0.0062` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6217` n `143` status `ready` deltaP `0.2491` edge `-0.0005` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
