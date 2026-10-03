# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T12:22:31.494755+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4782`

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

- `market_context_high->unknown_1h` score `366.6021` n `50` status `ready` deltaP `11.4731` edge `30.4786` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `294.554` n `50` status `ready` deltaP `12.0244` edge `24.466` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.6167` n `50` status `ready` deltaP `28.4194` edge `1.1156` maxDD `-11.6271`
- `news_risk_high->crypto_major_4h` score `11.1395` n `62` status `ready` deltaP `39.2424` edge `0.687` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `11.0875` n `50` status `ready` deltaP `36.0728` edge `0.8251` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.2902` n `62` status `ready` deltaP `27.7045` edge `0.7213` maxDD `-2.8784`
- `news_risk_high->crypto_alt_4h` score `7.6688` n `62` status `ready` deltaP `27.2819` edge `0.5916` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.4809` n `50` status `ready` deltaP `18.5327` edge `0.5702` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.3366` n `50` status `ready` deltaP `18.2496` edge `0.5353` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4902` n `62` status `ready` deltaP `32.423` edge `0.1739` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `4.0102` n `62` status `ready` deltaP `27.007` edge `0.2154` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2866` n `50` status `ready` deltaP `14.8024` edge `0.2415` maxDD `-3.6376`
- `news_risk_high->crypto_major_1h` score `3.2309` n `62` status `ready` deltaP `14.067` edge `0.211` maxDD `-1.5096`
- `news_risk_high->index_4h` score `3.0929` n `62` status `ready` deltaP `33.3064` edge `0.0619` maxDD `-0.4296`
- `market_context_high->fx_4h` score `3.0638` n `50` status `ready` deltaP `34.4262` edge `0.0393` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9905` n `50` status `ready` deltaP `13.5509` edge `0.2039` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3582` n `62` status `ready` deltaP `18.9448` edge `0.1118` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9161` n `62` status `ready` deltaP `23.4113` edge `0.0186` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.7781` n `62` status `ready` deltaP `6.8669` edge `0.1543` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.5346` n `50` status `ready` deltaP `21.3892` edge `0.0117` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
