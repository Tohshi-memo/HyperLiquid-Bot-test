# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T22:46:04.915369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `-0.0811` n `228`; crypto_major avg `-0.0292` n `8`; equity avg `-0.0049` n `74`; fx avg `0.0088` n `6`; index avg `0.0079` n `23`; metal avg `0.0001` n `18`; unknown avg `-0.0142` n `645`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.157` n `228`; crypto_major avg `-0.1977` n `8`; equity avg `-0.019` n `74`; fx avg `0.0367` n `6`; index avg `-0.0986` n `23`; metal avg `-0.6794` n `18`; unknown avg `0.822` n `644`
- 4h: commodity avg `0.2193` n `12`; crypto_alt avg `0.433` n `228`; crypto_major avg `0.5464` n `8`; equity avg `0.1946` n `74`; fx avg `-0.0356` n `6`; index avg `0.1059` n `23`; metal avg `0.0432` n `18`; unknown avg `1.5439` n `644`
- 24h: commodity avg `-0.1954` n `12`; crypto_alt avg `2.6384` n `228`; crypto_major avg `1.3894` n `8`; equity avg `0.4226` n `74`; fx avg `0.0376` n `6`; index avg `0.5079` n `23`; metal avg `0.3139` n `18`; unknown avg `0.1163` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
