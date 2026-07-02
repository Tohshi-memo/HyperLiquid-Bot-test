# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T23:07:26.030715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0289` n `229`; crypto_major avg `-0.1057` n `8`; equity avg `-0.153` n `88`; fx avg `-0.0037` n `6`; index avg `-0.0244` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.0164` n `765`
- 1h: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.0661` n `229`; crypto_major avg `-0.0827` n `8`; equity avg `-0.102` n `88`; fx avg `-0.0073` n `6`; index avg `-0.0139` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0424` n `765`
- 4h: commodity avg `0.0171` n `12`; crypto_alt avg `0.01` n `229`; crypto_major avg `-0.5156` n `8`; equity avg `0.4539` n `88`; fx avg `-0.0063` n `6`; index avg `0.1477` n `25`; metal avg `0.1243` n `20`; unknown avg `2.9371` n `765`
- 24h: commodity avg `0.1002` n `12`; crypto_alt avg `1.8162` n `228`; crypto_major avg `2.4384` n `8`; equity avg `-2.3891` n `88`; fx avg `-0.1402` n `6`; index avg `-0.46` n `25`; metal avg `0.9448` n `20`; unknown avg `3.9547` n `739`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
