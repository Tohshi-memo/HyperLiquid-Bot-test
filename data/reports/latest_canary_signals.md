# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T10:22:28.679976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.1115` n `228`; crypto_major avg `-0.1436` n `8`; equity avg `0.0123` n `79`; fx avg `0.0119` n `6`; index avg `0.0042` n `23`; metal avg `-0.0181` n `18`; unknown avg `-0.0556` n `701`
- 1h: commodity avg `0.0529` n `12`; crypto_alt avg `0.0876` n `228`; crypto_major avg `0.0992` n `8`; equity avg `0.1193` n `79`; fx avg `0.0147` n `6`; index avg `0.0395` n `23`; metal avg `0.0346` n `18`; unknown avg `-0.0244` n `701`
- 4h: commodity avg `0.1425` n `12`; crypto_alt avg `0.2483` n `228`; crypto_major avg `0.4479` n `8`; equity avg `0.421` n `79`; fx avg `0.0584` n `6`; index avg `0.0944` n `23`; metal avg `0.041` n `18`; unknown avg `-0.1519` n `693`
- 24h: commodity avg `-0.1874` n `12`; crypto_alt avg `-0.4957` n `228`; crypto_major avg `-0.214` n `8`; equity avg `-0.0576` n `79`; fx avg `0.0583` n `6`; index avg `0.0705` n `23`; metal avg `0.5092` n `18`; unknown avg `0.0808` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
