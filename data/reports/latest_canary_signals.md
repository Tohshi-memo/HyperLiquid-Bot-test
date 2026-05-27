# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T12:37:21.079937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1007` n `12`; crypto_alt avg `-0.105` n `228`; crypto_major avg `-0.3041` n `8`; equity avg `-0.1561` n `67`; fx avg `0.0302` n `6`; index avg `-0.0705` n `23`; metal avg `-0.3071` n `18`; unknown avg `-0.2888` n `418`
- 1h: commodity avg `-0.7779` n `12`; crypto_alt avg `0.3066` n `228`; crypto_major avg `0.0428` n `8`; equity avg `-0.0286` n `67`; fx avg `0.023` n `6`; index avg `0.0624` n `23`; metal avg `0.2268` n `18`; unknown avg `-0.0641` n `418`
- 4h: commodity avg `-0.3986` n `12`; crypto_alt avg `0.0164` n `228`; crypto_major avg `-0.0037` n `8`; equity avg `0.1926` n `67`; fx avg `-0.0144` n `6`; index avg `0.1752` n `23`; metal avg `-0.3776` n `18`; unknown avg `-0.1822` n `418`
- 24h: commodity avg `-1.5518` n `12`; crypto_alt avg `-1.6535` n `228`; crypto_major avg `-0.8379` n `8`; equity avg `0.7534` n `67`; fx avg `-0.0173` n `6`; index avg `0.8347` n `23`; metal avg `-1.0872` n `18`; unknown avg `0.206` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1952`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1907`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1751`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1724`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1658`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1474`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1402`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1376`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1319`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1313`, n `669`, weak_sample_signal
