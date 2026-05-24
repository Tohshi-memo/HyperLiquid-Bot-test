# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T10:52:14.989408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.0493` n `228`; crypto_major avg `-0.0022` n `8`; equity avg `-0.0562` n `67`; fx avg `0.0` n `6`; index avg `0.0289` n `23`; metal avg `-0.03` n `18`; unknown avg `0.1105` n `396`
- 1h: commodity avg `0.0428` n `12`; crypto_alt avg `-0.3419` n `228`; crypto_major avg `-0.3466` n `8`; equity avg `-0.0004` n `67`; fx avg `-0.0012` n `6`; index avg `-0.0124` n `23`; metal avg `0.0121` n `18`; unknown avg `0.3474` n `396`
- 4h: commodity avg `0.3709` n `12`; crypto_alt avg `-0.2021` n `228`; crypto_major avg `0.242` n `8`; equity avg `0.1623` n `67`; fx avg `-0.0045` n `6`; index avg `0.0081` n `23`; metal avg `0.0336` n `18`; unknown avg `-0.4167` n `396`
- 24h: commodity avg `-2.5935` n `12`; crypto_alt avg `3.6673` n `228`; crypto_major avg `4.4691` n `8`; equity avg `2.633` n `67`; fx avg `0.0587` n `6`; index avg `1.4556` n `23`; metal avg `1.3314` n `18`; unknown avg `1.3588` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
