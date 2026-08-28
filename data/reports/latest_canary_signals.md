# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T07:07:22.814416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0572` n `12`; crypto_alt avg `-0.453` n `231`; crypto_major avg `-0.4333` n `8`; equity avg `-0.0329` n `127`; fx avg `-0.0017` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0333` n `20`; unknown avg `-0.0811` n `792`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0606` n `231`; crypto_major avg `-0.2104` n `8`; equity avg `0.0268` n `127`; fx avg `-0.0023` n `6`; index avg `0.0242` n `26`; metal avg `0.3279` n `20`; unknown avg `-0.0417` n `792`
- 4h: commodity avg `0.0199` n `12`; crypto_alt avg `0.3089` n `231`; crypto_major avg `0.1294` n `8`; equity avg `-0.4494` n `127`; fx avg `-0.0591` n `6`; index avg `-0.0511` n `26`; metal avg `0.3328` n `20`; unknown avg `-0.1363` n `760`
- 24h: commodity avg `0.5612` n `12`; crypto_alt avg `0.3495` n `231`; crypto_major avg `1.4979` n `8`; equity avg `-0.495` n `127`; fx avg `-0.0864` n `6`; index avg `0.0251` n `26`; metal avg `0.438` n `20`; unknown avg `0.3598` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
