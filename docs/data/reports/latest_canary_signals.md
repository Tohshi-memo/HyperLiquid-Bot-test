# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T21:22:35.925060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `12`; crypto_alt avg `-0.1335` n `228`; crypto_major avg `-0.1499` n `8`; equity avg `0.017` n `85`; fx avg `-0.0296` n `6`; index avg `-0.0013` n `23`; metal avg `0.003` n `20`; unknown avg `-0.2888` n `717`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `-0.1618` n `228`; crypto_major avg `-0.1375` n `8`; equity avg `0.012` n `85`; fx avg `-0.0361` n `6`; index avg `-0.0155` n `23`; metal avg `0.0222` n `20`; unknown avg `-0.2686` n `717`
- 4h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.624` n `228`; crypto_major avg `-0.2726` n `8`; equity avg `-0.0621` n `85`; fx avg `-0.0142` n `6`; index avg `-0.0529` n `23`; metal avg `0.0216` n `20`; unknown avg `-0.3738` n `709`
- 24h: commodity avg `-0.8611` n `12`; crypto_alt avg `0.1691` n `228`; crypto_major avg `0.2174` n `8`; equity avg `-0.4627` n `85`; fx avg `0.1217` n `6`; index avg `0.0895` n `23`; metal avg `0.3793` n `18`; unknown avg `0.4404` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
