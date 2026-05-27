# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T13:37:23.833334+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1493` n `12`; crypto_alt avg `-0.3991` n `228`; crypto_major avg `-0.4772` n `8`; equity avg `-0.5393` n `67`; fx avg `-0.0116` n `6`; index avg `-0.3386` n `23`; metal avg `0.0097` n `18`; unknown avg `0.8982` n `418`
- 1h: commodity avg `0.6777` n `12`; crypto_alt avg `-1.0328` n `228`; crypto_major avg `-1.039` n `8`; equity avg `-0.9551` n `67`; fx avg `-0.0297` n `6`; index avg `-0.6269` n `23`; metal avg `-0.3953` n `18`; unknown avg `2.3078` n `418`
- 4h: commodity avg `0.2255` n `12`; crypto_alt avg `-0.391` n `228`; crypto_major avg `-0.9375` n `8`; equity avg `-0.7934` n `67`; fx avg `-0.0169` n `6`; index avg `-0.4204` n `23`; metal avg `-0.9128` n `18`; unknown avg `1.8988` n `418`
- 24h: commodity avg `-1.4438` n `12`; crypto_alt avg `-2.3554` n `228`; crypto_major avg `-1.6578` n `8`; equity avg `-0.0121` n `67`; fx avg `-0.0562` n `6`; index avg `-0.0279` n `23`; metal avg `-1.6872` n `18`; unknown avg `2.2653` n `398`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
