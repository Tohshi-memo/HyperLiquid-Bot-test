# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T12:37:34.874624+00:00`
- Price records: `672`
- Market context records: `5352`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11470`

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

- `market_context_high->unknown_24h` score `15.1893` n `161` status `ready` deltaP `20.1852` edge `1.1402` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.4115` n `161` status `ready` deltaP `21.6873` edge `0.7604` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.5094` n `161` status `ready` deltaP `17.7396` edge `0.8204` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.7175` n `194` status `ready` deltaP `13.3361` edge `0.3668` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.4322` n `194` status `ready` deltaP `10.3595` edge `0.2977` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7038` n `194` status `ready` deltaP `9.7875` edge `0.2406` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8228` n `161` status `ready` deltaP `24.8081` edge `0.1036` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.3055` n `197` status `ready` deltaP `6.8976` edge `0.076` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1359` n `161` status `ready` deltaP `9.3988` edge `0.0382` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.0298` n `197` status `ready` deltaP `5.4728` edge `0.0114` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.0683` n `197` status `ready` deltaP `4.029` edge `0.092` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0991` n `197` status `ready` deltaP `1.3344` edge `0.079` maxDD `-5.0257`
- `market_context_high->index_4h` score `-0.4141` n `194` status `ready` deltaP `5.6119` edge `0.0254` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.424` n `197` status `ready` deltaP `-0.6771` edge `-0.0009` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5095` n `197` status `ready` deltaP `0.345` edge `-0.0001` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7175` n `194` status `ready` deltaP `1.221` edge `0.0028` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2497` n `194` status `ready` deltaP `7.7555` edge `-0.0376` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5262` n `197` status `ready` deltaP `-4.1392` edge `-0.0078` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.6494` n `194` status `ready` deltaP `-7.6817` edge `-0.036` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8286` n `194` status `ready` deltaP `-7.1662` edge `-0.0429` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
