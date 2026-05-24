# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T22:15:16.403149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.2893` n `228`; crypto_major avg `0.1803` n `8`; equity avg `0.0371` n `67`; fx avg `-0.0015` n `6`; index avg `0.0139` n `23`; metal avg `0.1379` n `18`; unknown avg `0.0905` n `396`
- 1h: commodity avg `-0.6624` n `12`; crypto_alt avg `-0.1123` n `228`; crypto_major avg `0.0656` n `8`; equity avg `-0.1802` n `67`; fx avg `0.0063` n `6`; index avg `0.0081` n `23`; metal avg `1.0406` n `18`; unknown avg `0.4481` n `396`
- 4h: commodity avg `-0.6848` n `12`; crypto_alt avg `-0.7161` n `228`; crypto_major avg `-0.2798` n `8`; equity avg `-0.1064` n `67`; fx avg `0.069` n `6`; index avg `-0.1062` n `23`; metal avg `0.7503` n `18`; unknown avg `-0.5129` n `396`
- 24h: commodity avg `0.6264` n `12`; crypto_alt avg `-2.0661` n `228`; crypto_major avg `0.4083` n `8`; equity avg `0.3221` n `67`; fx avg `0.0786` n `6`; index avg `-0.07` n `23`; metal avg `0.828` n `18`; unknown avg `0.1467` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
