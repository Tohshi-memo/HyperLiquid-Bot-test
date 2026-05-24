# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T14:22:15.099746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.7361` n `12`; crypto_alt avg `-0.4862` n `228`; crypto_major avg `-0.5499` n `8`; equity avg `-0.2799` n `67`; fx avg `-0.0079` n `6`; index avg `-0.1215` n `23`; metal avg `-0.4269` n `18`; unknown avg `0.6471` n `396`
- 1h: commodity avg `0.8599` n `12`; crypto_alt avg `-1.0567` n `228`; crypto_major avg `-1.0502` n `8`; equity avg `-0.4254` n `67`; fx avg `0.0067` n `6`; index avg `-0.1706` n `23`; metal avg `-0.535` n `18`; unknown avg `0.5636` n `396`
- 4h: commodity avg `0.9878` n `12`; crypto_alt avg `-1.2063` n `228`; crypto_major avg `-0.8213` n `8`; equity avg `-0.2776` n `67`; fx avg `0.0169` n `6`; index avg `-0.2518` n `23`; metal avg `-0.6973` n `18`; unknown avg `1.3009` n `396`
- 24h: commodity avg `-1.3643` n `12`; crypto_alt avg `1.2152` n `228`; crypto_major avg `2.9049` n `8`; equity avg `2.0733` n `67`; fx avg `0.0855` n `6`; index avg `0.7974` n `23`; metal avg `0.5798` n `18`; unknown avg `1.5139` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
