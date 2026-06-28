# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T11:37:26.040737+00:00`
- Price records: `672`
- Market context records: `5036`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10200`

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

- `market_context_high->unknown_1h` score `14.087` n `95` status `ready` deltaP `2.641` edge `1.2064` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.0439` n `93` status `ready` deltaP `22.2118` edge `0.7078` maxDD `-5.5109`
- `market_context_high->crypto_major_4h` score `5.4491` n `93` status `ready` deltaP `16.4897` edge `0.5026` maxDD `-8.3416`
- `market_context_high->crypto_alt_4h` score `5.284` n `93` status `ready` deltaP `14.1785` edge `0.4852` maxDD `-7.8181`
- `market_context_high->metal_4h` score `1.227` n `93` status `ready` deltaP `13.0868` edge `0.1229` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.8059` n `95` status `ready` deltaP `7.7403` edge `0.0729` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.6567` n `95` status `ready` deltaP `5.6208` edge `0.109` maxDD `-4.6734`
- `market_context_high->equity_4h` score `0.3758` n `93` status `ready` deltaP `2.3587` edge `0.1706` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3373` n `95` status `ready` deltaP `6.0699` edge `0.0373` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1342` n `95` status `ready` deltaP `4.7321` edge `0.0879` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.0125` n `74` status `ready` deltaP `10.0789` edge `0.0074` maxDD `-1.7626`
- `market_context_high->index_4h` score `-0.1922` n `93` status `ready` deltaP `3.1045` edge `0.0394` maxDD `-1.0893`
- `market_context_high->commodity_1h` score `-0.316` n `95` status `ready` deltaP `1.5695` edge `0.015` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.6396` n `95` status `ready` deltaP `1.2748` edge `0.0123` maxDD `-0.5946`
- `market_context_high->commodity_4h` score `-0.7649` n `93` status `ready` deltaP `4.1552` edge `-0.0005` maxDD `-5.021`
- `market_context_high->fx_4h` score `-1.0181` n `93` status `ready` deltaP `-4.3732` edge `-0.0025` maxDD `-1.2426`
- `market_context_high->fx_1h` score `-1.7063` n `95` status `ready` deltaP `-11.3662` edge `-0.0054` maxDD `-0.5482`
- `market_context_high->metal_24h` score `-3.6772` n `74` status `ready` deltaP `5.9028` edge `0.0347` maxDD `-32.9721`
- `market_context_high->commodity_24h` score `-4.6436` n `74` status `ready` deltaP `0.4129` edge `-0.0872` maxDD `-27.5371`
- `market_context_high->unknown_24h` score `-5.0366` n `74` status `ready` deltaP `27.0364` edge `-0.5657` maxDD `-1.4072`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
