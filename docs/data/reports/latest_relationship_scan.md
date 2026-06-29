# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T18:22:33.791971+00:00`
- Price records: `672`
- Market context records: `5169`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `28.3561` n `68` status `ready` deltaP `32.8329` edge `2.1631` maxDD `-0.8515`
- `market_context_high->crypto_alt_24h` score `7.9644` n `68` status `ready` deltaP `21.5993` edge `0.8584` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.9777` n `144` status `ready` deltaP `20.2744` edge `0.4652` maxDD `-5.5109`
- `market_context_high->crypto_major_24h` score `5.4072` n `68` status `ready` deltaP `19.9653` edge `0.9263` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.8953` n `144` status `ready` deltaP `15.1593` edge `0.4668` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3582` n `144` status `ready` deltaP `14.0752` edge `0.4986` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.4399` n `151` status `ready` deltaP `10.0062` edge `0.2841` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.9834` n `144` status `ready` deltaP `8.8076` edge `0.1871` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.8142` n `151` status `ready` deltaP `8.2196` edge `0.1376` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.756` n `151` status `ready` deltaP `5.4388` edge `0.1229` maxDD `-5.0257`
- `market_context_high->commodity_24h` score `0.3747` n `68` status `ready` deltaP `15.6862` edge `0.1192` maxDD `-7.7252`
- `market_context_high->equity_1h` score `0.3026` n `151` status `ready` deltaP `7.8518` edge `0.0694` maxDD `-5.0555`
- `market_context_high->metal_24h` score `0.0356` n `68` status `ready` deltaP `-1.8587` edge `0.2015` maxDD `-8.097`
- `market_context_high->index_1h` score `-0.0382` n `151` status `ready` deltaP `5.0531` edge `0.0135` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0477` n `151` status `ready` deltaP `5.3347` edge `0.0175` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2259` n `151` status `ready` deltaP `2.3813` edge `0.0004` maxDD `-0.6194`
- `market_context_high->fx_24h` score `-0.339` n `68` status `ready` deltaP `7.5878` edge `0.0107` maxDD `-0.8294`
- `market_context_high->index_4h` score `-0.3461` n `144` status `ready` deltaP `5.1999` edge `0.0327` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.502` n `144` status `ready` deltaP `4.7595` edge `0.0073` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5495` n `151` status `ready` deltaP `1.4425` edge `0.0008` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
