# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T04:07:31.417574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `-0.3255` n `228`; crypto_major avg `-0.1221` n `8`; equity avg `-0.0511` n `74`; fx avg `0.028` n `6`; index avg `-0.0375` n `23`; metal avg `0.0028` n `18`; unknown avg `0.808` n `643`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `-0.4729` n `228`; crypto_major avg `-0.4403` n `8`; equity avg `-0.2913` n `74`; fx avg `0.0004` n `6`; index avg `-0.0451` n `23`; metal avg `-0.0302` n `18`; unknown avg `0.5067` n `643`
- 4h: commodity avg `0.0859` n `12`; crypto_alt avg `0.2951` n `228`; crypto_major avg `-0.2591` n `8`; equity avg `-0.2467` n `74`; fx avg `-0.0067` n `6`; index avg `0.0689` n `23`; metal avg `-0.048` n `18`; unknown avg `-0.2556` n `643`
- 24h: commodity avg `-0.5328` n `12`; crypto_alt avg `-0.0531` n `228`; crypto_major avg `-0.3489` n `8`; equity avg `-0.7709` n `74`; fx avg `-0.0067` n `6`; index avg `0.635` n `23`; metal avg `0.4067` n `18`; unknown avg `39.8093` n `515`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
