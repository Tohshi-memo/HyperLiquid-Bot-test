# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T12:07:11.292285+00:00`
- Correlation status: `ready`
- Asset price records: `548`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.2961` n `228`; crypto_major avg `0.1381` n `8`; equity avg `0.1185` n `65`; fx avg `-0.0073` n `4`; index avg `0.058` n `23`; metal avg `0.0553` n `18`; unknown avg `0.0844` n `366`
- 1h: commodity avg `-0.2571` n `12`; crypto_alt avg `0.1998` n `228`; crypto_major avg `0.067` n `8`; equity avg `-0.1554` n `65`; fx avg `-0.016` n `4`; index avg `0.0182` n `23`; metal avg `0.2648` n `18`; unknown avg `-0.0844` n `366`
- 4h: commodity avg `-0.3516` n `12`; crypto_alt avg `-0.006` n `228`; crypto_major avg `-0.5764` n `8`; equity avg `-0.2039` n `65`; fx avg `0.077` n `4`; index avg `-0.1748` n `23`; metal avg `0.1635` n `18`; unknown avg `0.1506` n `358`
- 24h: commodity avg `-0.8162` n `7`; crypto_alt avg `0.4571` n `223`; crypto_major avg `-2.2921` n `7`; equity avg `0.3639` n `47`; fx avg `0.1185` n `4`; index avg `0.0855` n `6`; metal avg `1.7677` n `7`; unknown avg `1.1411` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `544`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `544`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0982`, n `544`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0774`, n `540`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `540`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0748`, n `540`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `540`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `544`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0672`, n `540`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `544`, weak_sample_signal
