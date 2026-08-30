# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T19:22:24.256053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1229` n `12`; crypto_alt avg `-0.0683` n `231`; crypto_major avg `-0.1707` n `8`; equity avg `-0.0089` n `128`; fx avg `0.0009` n `6`; index avg `-0.0058` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.094` n `793`
- 1h: commodity avg `0.1394` n `12`; crypto_alt avg `0.154` n `231`; crypto_major avg `-0.0254` n `8`; equity avg `0.0061` n `128`; fx avg `-0.0006` n `6`; index avg `-0.0169` n `26`; metal avg `0.0065` n `20`; unknown avg `0.0494` n `793`
- 4h: commodity avg `0.1942` n `12`; crypto_alt avg `0.7022` n `231`; crypto_major avg `0.4203` n `8`; equity avg `0.1088` n `128`; fx avg `0.0031` n `6`; index avg `0.0143` n `26`; metal avg `0.0591` n `20`; unknown avg `0.4843` n `793`
- 24h: commodity avg `0.179` n `12`; crypto_alt avg `1.6234` n `231`; crypto_major avg `0.9208` n `8`; equity avg `0.319` n `128`; fx avg `0.0303` n `6`; index avg `0.0683` n `26`; metal avg `0.1098` n `20`; unknown avg `0.071` n `740`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
