# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T07:22:27.239921+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1709.0736` n `118` status `ready` deltaP `1.2153` edge `142.4147` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.849` n `48` status `ready` deltaP `10.791` edge `8.5868` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.7301` n `44` status `ready` deltaP `30.1926` edge `4.228` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.8606` n `44` status `ready` deltaP `14.9148` edge `2.3436` maxDD `-2.7051`
- `market_context_high->equity_24h` score `28.0852` n `44` status `ready` deltaP `36.0954` edge `2.1312` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9269` n `44` status `ready` deltaP `33.4912` edge `0.4461` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9059` n `44` status `ready` deltaP `34.5644` edge `0.1189` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.1179` n `44` status `ready` deltaP `34.7838` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7023` n `44` status `ready` deltaP `15.23` edge `0.1613` maxDD `-1.3444`
- `market_context_high->equity_1h` score `0.9779` n `48` status `ready` deltaP `11.7266` edge `0.0436` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8948` n `44` status `ready` deltaP `7.331` edge `0.0883` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `0.8015` n `48` status `ready` deltaP `7.7221` edge `0.1011` maxDD `-4.8632`
- `market_context_high->crypto_major_4h` score `0.792` n `44` status `ready` deltaP `6.4579` edge `0.1134` maxDD `-5.2359`
- `news_risk_high->index_24h` score `0.5785` n `118` status `ready` deltaP `13.73` edge `0.0262` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.5594` n `48` status `ready` deltaP `9.3438` edge `0.008` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.5423` n `48` status `ready` deltaP `6.9611` edge `0.0877` maxDD `-5.7799`
- `news_risk_high->metal_24h` score `0.5056` n `118` status `ready` deltaP `14.9188` edge `0.124` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.3841` n `48` status `ready` deltaP `11.6392` edge `0.0073` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1342` n `48` status `ready` deltaP `4.9401` edge `0.0101` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.1259` n `139` status `ready` deltaP `2.3145` edge `0.0031` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
