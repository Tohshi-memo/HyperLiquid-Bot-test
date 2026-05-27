# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T11:07:24.005567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0996` n `12`; crypto_alt avg `0.2505` n `228`; crypto_major avg `0.1977` n `8`; equity avg `0.1698` n `67`; fx avg `0.0093` n `6`; index avg `0.1083` n `23`; metal avg `0.0974` n `18`; unknown avg `0.2216` n `418`
- 1h: commodity avg `0.2553` n `12`; crypto_alt avg `0.3562` n `228`; crypto_major avg `0.2023` n `8`; equity avg `0.0726` n `67`; fx avg `-0.017` n `6`; index avg `0.0891` n `23`; metal avg `-0.7243` n `18`; unknown avg `0.2244` n `418`
- 4h: commodity avg `-0.1441` n `12`; crypto_alt avg `-0.1298` n `228`; crypto_major avg `0.2299` n `8`; equity avg `0.6396` n `67`; fx avg `-0.0663` n `6`; index avg `0.3197` n `23`; metal avg `-0.4072` n `18`; unknown avg `-0.1526` n `418`
- 24h: commodity avg `-0.8307` n `12`; crypto_alt avg `-2.07` n `228`; crypto_major avg `-0.8284` n `8`; equity avg `0.7672` n `67`; fx avg `-0.0463` n `6`; index avg `0.7756` n `23`; metal avg `-1.1976` n `18`; unknown avg `0.3254` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
