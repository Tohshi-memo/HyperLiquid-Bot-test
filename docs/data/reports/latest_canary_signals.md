# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T09:22:32.990055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `0.0972` n `230`; crypto_major avg `0.1204` n `8`; equity avg `-0.0023` n `102`; fx avg `-0.013` n `6`; index avg `-0.0051` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.028` n `774`
- 1h: commodity avg `0.039` n `12`; crypto_alt avg `0.0786` n `230`; crypto_major avg `0.1098` n `8`; equity avg `0.1001` n `102`; fx avg `0.0001` n `6`; index avg `0.0159` n `25`; metal avg `-0.03` n `20`; unknown avg `-0.0427` n `774`
- 4h: commodity avg `-0.188` n `12`; crypto_alt avg `-0.1946` n `230`; crypto_major avg `-0.2624` n `8`; equity avg `0.0819` n `102`; fx avg `-0.0163` n `6`; index avg `0.0261` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0023` n `758`
- 24h: commodity avg `-0.5059` n `12`; crypto_alt avg `-3.3708` n `230`; crypto_major avg `-3.3413` n `8`; equity avg `-3.9936` n `102`; fx avg `-0.1547` n `6`; index avg `-0.8527` n `25`; metal avg `-0.4556` n `20`; unknown avg `998.4779` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
