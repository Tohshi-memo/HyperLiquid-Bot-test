# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T10:27:11.712043+00:00`
- Price records: `672`
- Market context records: `3064`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6969`

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

- `market_context_high->crypto_alt_24h` score `16.7991` n `92` status `ready` deltaP `11.8207` edge `2.4666` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.4786` n `92` status `ready` deltaP `46.0825` edge `0.9234` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.4001` n `92` status `ready` deltaP `23.362` edge `1.0074` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.4992` n `92` status `ready` deltaP `29.212` edge `0.8599` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.4271` n `92` status `ready` deltaP `24.464` edge `1.4489` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3965` n `127` status `ready` deltaP `16.2929` edge `0.1558` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.2385` n `127` status `ready` deltaP `2.7547` edge `0.0671` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2531` n `129` status `ready` deltaP `-0.0348` edge `0.0214` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.562` n `129` status `ready` deltaP `2.8095` edge `0.0155` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.6246` n `129` status `ready` deltaP `-6.1667` edge `-0.0017` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.7352` n `129` status `ready` deltaP `3.5847` edge `0.0948` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7777` n `92` status `ready` deltaP `-0.3624` edge `-0.0101` maxDD `-0.6418`
- `market_context_high->unknown_1h` score `-1.038` n `129` status `ready` deltaP `2.5472` edge `-0.0304` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.0494` n `129` status `ready` deltaP `0.564` edge `0.0071` maxDD `-8.6319`
- `market_context_high->crypto_major_1h` score `-1.0814` n `129` status `ready` deltaP `2.2269` edge `0.0728` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.22` n `127` status `ready` deltaP `-9.9685` edge `-0.0057` maxDD `-1.0735`
- `market_context_high->metal_1h` score `-1.3003` n `129` status `ready` deltaP `-3.6752` edge `-0.0054` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3552` n `127` status `ready` deltaP `9.234` edge `0.0556` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.9665` n `127` status `ready` deltaP `18.2783` edge `0.3023` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.4979` n `127` status `ready` deltaP `7.6075` edge `0.0133` maxDD `-35.3306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
