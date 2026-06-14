# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T18:22:23.279578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1018` n `12`; crypto_alt avg `-0.1365` n `228`; crypto_major avg `-0.1484` n `8`; equity avg `-0.0445` n `74`; fx avg `0.0012` n `6`; index avg `-0.0106` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.3` n `645`
- 1h: commodity avg `0.1156` n `12`; crypto_alt avg `-0.5496` n `228`; crypto_major avg `-0.4336` n `8`; equity avg `-0.091` n `74`; fx avg `-0.0072` n `6`; index avg `-0.0059` n `23`; metal avg `-0.0089` n `18`; unknown avg `-0.5629` n `645`
- 4h: commodity avg `-0.2843` n `12`; crypto_alt avg `-0.6777` n `228`; crypto_major avg `-0.5798` n `8`; equity avg `-0.0668` n `74`; fx avg `-0.0157` n `6`; index avg `0.0811` n `23`; metal avg `0.0267` n `18`; unknown avg `-0.3049` n `645`
- 24h: commodity avg `0.0781` n `12`; crypto_alt avg `-1.6728` n `228`; crypto_major avg `-0.7976` n `8`; equity avg `0.2742` n `74`; fx avg `-0.0557` n `6`; index avg `0.25` n `23`; metal avg `0.151` n `18`; unknown avg `0.8795` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
