# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T18:52:29.113625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4093`

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

- `news_risk_high->equity_4h` score `2.3637` n `95` status `ready` deltaP `16.6207` edge `0.2828` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0424` n `95` status `ready` deltaP `15.9964` edge `0.028` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.7745` n `95` status `ready` deltaP `6.9965` edge `0.1076` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.3895` n `95` status `ready` deltaP `12.849` edge `0.0096` maxDD `-0.2931`
- `news_risk_high->equity_24h` score `0.072` n `95` status `ready` deltaP `28.8096` edge `0.9758` maxDD `-86.0244`
- `news_risk_high->crypto_major_4h` score `-0.2041` n `95` status `ready` deltaP `3.5606` edge `0.1187` maxDD `-9.1553`
- `news_risk_high->metal_1h` score `-0.219` n `95` status `ready` deltaP `1.434` edge `-0.0019` maxDD `-0.5256`
- `news_risk_high->index_24h` score `-0.2964` n `95` status `ready` deltaP `2.0378` edge `0.1452` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.3304` n `95` status `ready` deltaP `-0.3577` edge `0.0` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.4289` n `95` status `ready` deltaP `3.525` edge `0.0443` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.5833` n `95` status `ready` deltaP `-0.6274` edge `-0.0026` maxDD `-0.4401`
- `news_risk_high->crypto_major_1h` score `-0.6456` n `95` status `ready` deltaP `-1.4387` edge `0.0207` maxDD `-4.1772`
- `news_risk_high->crypto_alt_4h` score `-0.6935` n `95` status `ready` deltaP `0.6643` edge `0.1703` maxDD `-14.0916`
- `news_risk_high->metal_4h` score `-0.833` n `95` status `ready` deltaP `1.4923` edge `-0.0262` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.5055` n `95` status `ready` deltaP `-11.5515` edge `0.0138` maxDD `-0.313`
- `news_risk_high->metal_24h` score `-2.8346` n `95` status `ready` deltaP `4.694` edge `-0.2051` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2393` n `95` status `ready` deltaP `-18.5708` edge `-0.0138` maxDD `-2.9201`
- `news_risk_high->commodity_4h` score `-4.608` n `95` status `ready` deltaP `-26.9512` edge `-0.0131` maxDD `-6.6313`
- `news_risk_high->crypto_major_24h` score `-6.1893` n `95` status `ready` deltaP `-15.0416` edge `0.1571` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.5464` n `95` status `ready` deltaP `-25.0406` edge `-0.0119` maxDD `-32.0026`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
