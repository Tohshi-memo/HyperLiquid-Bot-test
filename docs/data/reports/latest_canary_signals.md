# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T04:22:25.324369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.2442` n `229`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0341` n `88`; fx avg `0.0035` n `6`; index avg `-0.001` n `25`; metal avg `0.004` n `20`; unknown avg `-0.1543` n `765`
- 1h: commodity avg `-0.019` n `12`; crypto_alt avg `-0.1079` n `229`; crypto_major avg `0.3437` n `8`; equity avg `0.0152` n `88`; fx avg `0.0126` n `6`; index avg `0.0095` n `25`; metal avg `0.0118` n `20`; unknown avg `4.0983` n `765`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.2843` n `229`; crypto_major avg `0.1269` n `8`; equity avg `0.1633` n `88`; fx avg `-0.0112` n `6`; index avg `-0.0076` n `25`; metal avg `-0.004` n `20`; unknown avg `0.1365` n `763`
- 24h: commodity avg `-0.0514` n `12`; crypto_alt avg `2.4333` n `229`; crypto_major avg `3.2581` n `8`; equity avg `0.5964` n `88`; fx avg `-0.1599` n `6`; index avg `0.0975` n `25`; metal avg `-0.1858` n `20`; unknown avg `4.3046` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
