# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T09:52:11.860785+00:00`
- Correlation status: `ready`
- Asset price records: `539`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1866` n `12`; crypto_alt avg `-0.1044` n `228`; crypto_major avg `-0.144` n `8`; equity avg `0.0411` n `65`; fx avg `-0.0003` n `4`; index avg `-0.0522` n `23`; metal avg `0.0117` n `18`; unknown avg `0.2294` n `358`
- 1h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.3503` n `228`; crypto_major avg `-0.3728` n `8`; equity avg `0.4094` n `65`; fx avg `0.0301` n `4`; index avg `-0.1405` n `23`; metal avg `0.1507` n `18`; unknown avg `0.0855` n `358`
- 4h: commodity avg `-0.8113` n `12`; crypto_alt avg `0.4145` n `228`; crypto_major avg `0.1447` n `8`; equity avg `0.4002` n `65`; fx avg `0.0511` n `4`; index avg `-0.0514` n `23`; metal avg `1.1697` n `18`; unknown avg `0.4795` n `356`
- 24h: commodity avg `-0.854` n `7`; crypto_alt avg `-0.0908` n `223`; crypto_major avg `-1.9765` n `7`; equity avg `0.4858` n `47`; fx avg `0.1133` n `4`; index avg `0.5437` n `6`; metal avg `1.5259` n `7`; unknown avg `0.7833` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `535`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1232`, n `535`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0957`, n `535`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0873`, n `531`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0833`, n `531`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0797`, n `531`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0791`, n `531`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `531`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `531`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `535`, weak_sample_signal
