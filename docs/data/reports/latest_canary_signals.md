# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T08:52:28.105533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0229` n `12`; crypto_alt avg `0.2742` n `228`; crypto_major avg `0.1321` n `8`; equity avg `0.0452` n `79`; fx avg `-0.0048` n `6`; index avg `0.0098` n `23`; metal avg `0.0607` n `18`; unknown avg `-0.0087` n `701`
- 1h: commodity avg `-0.1188` n `12`; crypto_alt avg `0.046` n `228`; crypto_major avg `-0.0769` n `8`; equity avg `-0.0358` n `79`; fx avg `-0.008` n `6`; index avg `0.0019` n `23`; metal avg `0.0142` n `18`; unknown avg `-0.125` n `701`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `0.307` n `228`; crypto_major avg `0.525` n `8`; equity avg `0.4331` n `79`; fx avg `-0.0023` n `6`; index avg `0.08` n `23`; metal avg `0.2654` n `18`; unknown avg `0.1779` n `661`
- 24h: commodity avg `-0.2176` n `12`; crypto_alt avg `0.2023` n `228`; crypto_major avg `0.3667` n `8`; equity avg `-0.2295` n `79`; fx avg `0.0142` n `6`; index avg `0.0126` n `23`; metal avg `0.38` n `18`; unknown avg `0.0863` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
