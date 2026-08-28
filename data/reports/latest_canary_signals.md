# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T09:37:23.465784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0482` n `12`; crypto_alt avg `-0.181` n `231`; crypto_major avg `-0.1263` n `8`; equity avg `-0.0131` n `127`; fx avg `0.0038` n `6`; index avg `0.0` n `26`; metal avg `0.0149` n `20`; unknown avg `-0.045` n `792`
- 1h: commodity avg `0.154` n `12`; crypto_alt avg `-0.2941` n `231`; crypto_major avg `-0.6115` n `8`; equity avg `-0.1365` n `127`; fx avg `0.0163` n `6`; index avg `-0.0155` n `26`; metal avg `0.0611` n `20`; unknown avg `-0.0644` n `792`
- 4h: commodity avg `0.0191` n `12`; crypto_alt avg `-0.3057` n `231`; crypto_major avg `-0.6042` n `8`; equity avg `-0.1407` n `127`; fx avg `-0.0377` n `6`; index avg `0.0024` n `26`; metal avg `0.4627` n `20`; unknown avg `-0.0576` n `760`
- 24h: commodity avg `0.2418` n `12`; crypto_alt avg `-1.5041` n `231`; crypto_major avg `-0.9635` n `8`; equity avg `-1.2004` n `127`; fx avg `-0.0826` n `6`; index avg `-0.0404` n `26`; metal avg `0.7113` n `20`; unknown avg `0.2184` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
