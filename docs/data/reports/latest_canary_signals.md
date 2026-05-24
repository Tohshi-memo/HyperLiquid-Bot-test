# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T10:37:17.285453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.1284` n `228`; crypto_major avg `-0.0279` n `8`; equity avg `0.0483` n `67`; fx avg `0.0` n `6`; index avg `-0.0168` n `23`; metal avg `-0.0241` n `18`; unknown avg `0.0479` n `396`
- 1h: commodity avg `0.1135` n `12`; crypto_alt avg `-0.357` n `228`; crypto_major avg `-0.2567` n `8`; equity avg `0.1933` n `67`; fx avg `-0.0049` n `6`; index avg `-0.0362` n `23`; metal avg `0.0345` n `18`; unknown avg `0.0873` n `396`
- 4h: commodity avg `0.3841` n `12`; crypto_alt avg `0.2278` n `228`; crypto_major avg `0.6408` n `8`; equity avg `0.2908` n `67`; fx avg `0.0047` n `6`; index avg `0.01` n `23`; metal avg `0.0813` n `18`; unknown avg `-0.8692` n `396`
- 24h: commodity avg `-2.6883` n `12`; crypto_alt avg `3.5902` n `228`; crypto_major avg `4.3495` n `8`; equity avg `2.7465` n `67`; fx avg `0.0643` n `6`; index avg `1.4119` n `23`; metal avg `1.3836` n `18`; unknown avg `1.3716` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
