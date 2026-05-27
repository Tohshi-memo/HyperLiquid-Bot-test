# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T05:37:16.036380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1131` n `12`; crypto_alt avg `0.1104` n `228`; crypto_major avg `0.2013` n `8`; equity avg `0.0589` n `67`; fx avg `-0.0015` n `6`; index avg `0.0141` n `23`; metal avg `-0.2539` n `18`; unknown avg `-0.3363` n `418`
- 1h: commodity avg `-0.0841` n `12`; crypto_alt avg `0.8847` n `228`; crypto_major avg `0.8378` n `8`; equity avg `0.0928` n `67`; fx avg `0.0089` n `6`; index avg `0.0055` n `23`; metal avg `-0.166` n `18`; unknown avg `0.3066` n `418`
- 4h: commodity avg `-0.3105` n `12`; crypto_alt avg `-0.5369` n `228`; crypto_major avg `0.2384` n `8`; equity avg `-0.3754` n `67`; fx avg `-0.036` n `6`; index avg `-0.1922` n `23`; metal avg `-0.5341` n `18`; unknown avg `-0.671` n `418`
- 24h: commodity avg `-0.4086` n `12`; crypto_alt avg `-1.5251` n `228`; crypto_major avg `-0.591` n `8`; equity avg `0.4699` n `67`; fx avg `-0.045` n `6`; index avg `0.806` n `23`; metal avg `-0.4082` n `18`; unknown avg `1.2542` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
