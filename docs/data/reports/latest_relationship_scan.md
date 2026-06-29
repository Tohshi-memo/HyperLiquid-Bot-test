# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T16:07:28.295101+00:00`
- Price records: `672`
- Market context records: `5159`
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

- `market_context_high->unknown_24h` score `30.191` n `63` status `ready` deltaP `33.9286` edge `2.3087` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `6.1676` n `136` status `ready` deltaP `20.0233` edge `0.4827` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.7554` n `136` status `ready` deltaP `14.7148` edge `0.4581` maxDD `-9.46`
- `market_context_high->crypto_alt_24h` score `4.7221` n `63` status `ready` deltaP `19.5437` edge `0.8138` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.4694` n `63` status `ready` deltaP `17.5595` edge `0.8221` maxDD `-22.6266`
- `market_context_high->unknown_1h` score `4.2132` n `147` status `ready` deltaP `10.0269` edge `0.3484` maxDD `-2.7986`
- `market_context_high->crypto_major_4h` score `3.9094` n `136` status `ready` deltaP `13.5491` edge `0.4647` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `2.0321` n `63` status `ready` deltaP `20.2381` edge `0.1577` maxDD `-5.1955`
- `market_context_high->metal_24h` score `0.9465` n `63` status `ready` deltaP `0.9424` edge `0.2459` maxDD `-5.4668`
- `market_context_high->crypto_major_1h` score `0.8874` n `147` status `ready` deltaP `8.2193` edge `0.1437` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.8438` n `147` status `ready` deltaP `5.7558` edge `0.1281` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.4903` n `136` status `ready` deltaP `8.0882` edge `0.1508` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.1884` n `147` status `ready` deltaP `7.1296` edge `0.0647` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.0661` n `147` status `ready` deltaP `5.212` edge `0.0152` maxDD `-2.0075`
- `market_context_high->index_1h` score `-0.0838` n `147` status `ready` deltaP `4.5582` edge `0.013` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.1848` n `147` status `ready` deltaP `3.1427` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4641` n `136` status `ready` deltaP `3.5599` edge `0.0285` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.4849` n `63` status `ready` deltaP `6.3492` edge `0.0068` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.5279` n `136` status `ready` deltaP `4.2772` edge `0.0072` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5663` n `147` status `ready` deltaP `1.0886` edge `0.001` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
