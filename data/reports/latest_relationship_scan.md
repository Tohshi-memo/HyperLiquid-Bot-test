# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-07T09:22:16.178242+00:00`
- Price records: `537`
- Market context records: `633`
- Flow alert records: `1792`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_major_24h` score `5.8188` n `146` status `ready` deltaP `16.7241` edge `0.4068` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.3573` n `146` status `ready` deltaP `7.2516` edge `0.4029` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.0815` n `146` status `ready` deltaP `9.0896` edge `0.0161` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3302` n `146` status `ready` deltaP `1.8398` edge `0.0032` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.501` n `146` status `ready` deltaP `2.0095` edge `0.0423` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.7148` n `146` status `ready` deltaP `-0.4778` edge `-0.0031` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1513` n `146` status `ready` deltaP `-4.1558` edge `-0.0079` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.2431` n `146` status `ready` deltaP `5.4718` edge `-0.0086` maxDD `-8.1842`
- `market_context_high->equity_1h` score `-1.315` n `146` status `ready` deltaP `-2.5572` edge `-0.0115` maxDD `-4.4826`
- `market_context_high->crypto_major_1h` score `-1.7474` n `146` status `ready` deltaP `5.3676` edge `-0.0091` maxDD `-11.4508`
- `market_context_high->crypto_alt_4h` score `-2.0666` n `146` status `ready` deltaP `4.1635` edge `0.057` maxDD `-15.2248`
- `market_context_high->index_4h` score `-2.409` n `146` status `ready` deltaP `-1.6626` edge `-0.0374` maxDD `-6.5149`
- `market_context_high->crypto_major_4h` score `-2.5299` n `146` status `ready` deltaP `13.3765` edge `0.0706` maxDD `-22.648`
- `market_context_high->index_24h` score `-3.0555` n `146` status `ready` deltaP `-8.4026` edge `0.0009` maxDD `-5.9609`
- `market_context_high->metal_1h` score `-3.4245` n `146` status `ready` deltaP `-5.0464` edge `-0.0558` maxDD `-9.0076`
- `market_context_high->equity_4h` score `-3.4398` n `146` status `ready` deltaP `-4.1771` edge `-0.0436` maxDD `-10.5498`
- `market_context_high->commodity_4h` score `-3.4478` n `146` status `ready` deltaP `-5.5987` edge `0.1001` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-4.317` n `146` status `ready` deltaP `-3.0407` edge `-0.016` maxDD `-21.0414`
- `market_context_high->unknown_4h` score `-4.7768` n `146` status `ready` deltaP `1.7024` edge `-0.2216` maxDD `-8.3588`
- `market_context_high->equity_24h` score `-4.95` n `146` status `ready` deltaP `-11.614` edge `-0.0746` maxDD `-10.5047`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
