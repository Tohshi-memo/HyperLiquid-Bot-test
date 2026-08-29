# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T01:07:23.327387+00:00`
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

- `news_risk_high->unknown_24h` score `56.4782` n `50` status `ready` deltaP `18.1976` edge `4.5852` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.5803` n `50` status `ready` deltaP `46.6066` edge `2.6151` maxDD `-2.8629`
- `news_risk_high->crypto_major_24h` score `9.2572` n `50` status `ready` deltaP `26.6343` edge `0.6432` maxDD `-2.6128`
- `news_risk_high->unknown_4h` score `8.7543` n `71` status `ready` deltaP `17.5863` edge `0.6433` maxDD `-1.4812`
- `news_risk_high->equity_24h` score `6.7999` n `50` status `ready` deltaP `30.1005` edge `0.4588` maxDD `-4.7584`
- `market_context_high->unknown_24h` score `5.7869` n `120` status `ready` deltaP `11.5309` edge `0.4786` maxDD `-3.1917`
- `news_risk_high->metal_24h` score `4.4766` n `50` status `ready` deltaP `43.4073` edge `0.0879` maxDD `-0.0053`
- `market_context_high->metal_24h` score `3.2938` n `120` status `ready` deltaP `28.7406` edge `0.1848` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.2258` n `74` status `ready` deltaP `8.7473` edge `0.2462` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.4466` n `50` status `ready` deltaP `26.9948` edge `0.039` maxDD `-0.2064`
- `news_risk_high->fx_4h` score `2.2211` n `71` status `ready` deltaP `32.6112` edge `0.0226` maxDD `-0.3931`
- `market_context_high->unknown_4h` score `2.1969` n `120` status `ready` deltaP `17.246` edge `0.1088` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.918` n `120` status `ready` deltaP `8.7924` edge `0.0629` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.539` n `74` status `ready` deltaP `11.705` edge `0.0057` maxDD `-0.1052`
- `news_risk_high->commodity_1h` score `0.3732` n `74` status `ready` deltaP `11.4096` edge `0.0038` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.0008` n `120` status `ready` deltaP `11.7784` edge `0.0131` maxDD `-3.3377`
- `market_context_high->fx_1h` score `-0.3717` n `120` status `ready` deltaP `3.9122` edge `-0.0005` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4665` n `74` status `ready` deltaP `-1.0438` edge `-0.0093` maxDD `-0.8174`
- `market_context_high->crypto_alt_4h` score `-0.5614` n `120` status `ready` deltaP `15.7723` edge `0.3075` maxDD `-31.4361`
- `market_context_high->crypto_major_4h` score `-0.6147` n `120` status `ready` deltaP `13.9431` edge `0.2009` maxDD `-20.9394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
