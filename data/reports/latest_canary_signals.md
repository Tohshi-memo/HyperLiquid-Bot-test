# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T19:52:15.349795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `0.0642` n `228`; crypto_major avg `0.0093` n `8`; equity avg `0.0779` n `67`; fx avg `0.0064` n `6`; index avg `0.0238` n `23`; metal avg `0.0045` n `18`; unknown avg `0.1152` n `396`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `0.0169` n `228`; crypto_major avg `0.0459` n `8`; equity avg `0.0861` n `67`; fx avg `0.0149` n `6`; index avg `0.0511` n `23`; metal avg `-0.0548` n `18`; unknown avg `0.0202` n `396`
- 4h: commodity avg `0.2335` n `12`; crypto_alt avg `0.0129` n `228`; crypto_major avg `0.0662` n `8`; equity avg `0.23` n `67`; fx avg `0.025` n `6`; index avg `0.0911` n `23`; metal avg `-0.0893` n `18`; unknown avg `-0.2401` n `396`
- 24h: commodity avg `-0.4015` n `12`; crypto_alt avg `-0.5896` n `228`; crypto_major avg `1.4469` n `8`; equity avg `1.1318` n `67`; fx avg `0.1321` n `6`; index avg `0.2732` n `23`; metal avg `0.3668` n `18`; unknown avg `0.3809` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
