# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T23:52:26.567641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `56.0285` n `50` status `ready` deltaP `17.331` edge `4.5535` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4795` n `50` status `ready` deltaP `46.6066` edge `2.6067` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `8.8791` n `50` status `ready` deltaP `26.2877` edge `0.614` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.7771` n `71` status `ready` deltaP `17.5863` edge `0.6452` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.6235` n `50` status `ready` deltaP `30.1005` edge `0.4441` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.3372` n `120` status `ready` deltaP `10.6643` edge `0.4469` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4562` n `50` status `ready` deltaP `43.4073` edge `0.0862` maxDD `-0.0053`
- `news_risk_high->unknown_1h` score `3.4766` n `71` status `ready` deltaP `8.807` edge `0.2667` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.2734` n `120` status `ready` deltaP `28.7406` edge `0.1831` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4298` n `50` status `ready` deltaP `26.9948` edge `0.0376` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2197` n `120` status `ready` deltaP `17.246` edge `0.1107` maxDD `-0.5894`
- `news_risk_high->fx_4h` score `2.1821` n `71` status `ready` deltaP `32.1539` edge `0.0224` maxDD `-0.3931`
- `market_context_high->unknown_1h` score `0.8892` n `120` status `ready` deltaP `8.6427` edge `0.0615` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.595` n `71` status `ready` deltaP `12.3598` edge `0.0059` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.3844` n `71` status `ready` deltaP `11.6113` edge `0.0039` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0435` n `120` status `ready` deltaP `12.5406` edge `0.0137` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3958` n `120` status `ready` deltaP `3.4631` edge `-0.0006` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4359` n `71` status `ready` deltaP `-0.4322` edge `-0.0096` maxDD `-0.8054`
- `news_risk_high->index_4h` score `-0.6965` n `71` status `ready` deltaP `-0.7407` edge `-0.0202` maxDD `-1.7996`
- `news_risk_high->metal_1h` score `-0.7009` n `71` status `ready` deltaP `-0.8539` edge `-0.0266` maxDD `-2.605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
