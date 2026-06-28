# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T01:37:28.877162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.0057` n `228`; crypto_major avg `0.0623` n `8`; equity avg `0.0186` n `88`; fx avg `0.0019` n `6`; index avg `0.0051` n `23`; metal avg `0.0043` n `20`; unknown avg `20.0661` n `764`
- 1h: commodity avg `0.2032` n `12`; crypto_alt avg `-0.0945` n `228`; crypto_major avg `0.0516` n `8`; equity avg `-0.1029` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0394` n `23`; metal avg `-0.0095` n `20`; unknown avg `19.6202` n `764`
- 4h: commodity avg `0.3184` n `12`; crypto_alt avg `-0.0347` n `228`; crypto_major avg `-0.2745` n `8`; equity avg `-0.1619` n `88`; fx avg `-0.022` n `6`; index avg `-0.1009` n `23`; metal avg `0.0161` n `20`; unknown avg `-0.7326` n `764`
- 24h: commodity avg `0.4081` n `12`; crypto_alt avg `-0.5914` n `228`; crypto_major avg `-0.7185` n `8`; equity avg `0.1055` n `88`; fx avg `-0.0012` n `6`; index avg `-0.1103` n `23`; metal avg `-0.0555` n `20`; unknown avg `-0.7783` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2134`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
