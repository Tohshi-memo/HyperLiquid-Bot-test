# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T20:14:39.910759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1397` n `12`; crypto_alt avg `-0.1976` n `228`; crypto_major avg `-0.2445` n `8`; equity avg `-0.0` n `67`; fx avg `0.0277` n `6`; index avg `-0.0541` n `23`; metal avg `-0.0296` n `18`; unknown avg `-0.0189` n `396`
- 1h: commodity avg `-0.1344` n `12`; crypto_alt avg `-0.3029` n `228`; crypto_major avg `-0.3081` n `8`; equity avg `0.0785` n `67`; fx avg `0.0384` n `6`; index avg `-0.0162` n `23`; metal avg `-0.0869` n `18`; unknown avg `-0.0146` n `396`
- 4h: commodity avg `0.2036` n `12`; crypto_alt avg `-0.344` n `228`; crypto_major avg `-0.321` n `8`; equity avg `0.1723` n `67`; fx avg `0.04` n `6`; index avg `0.0468` n `23`; metal avg `-0.139` n `18`; unknown avg `-0.3328` n `396`
- 24h: commodity avg `-0.4092` n `12`; crypto_alt avg `-0.7269` n `228`; crypto_major avg `1.2586` n `8`; equity avg `1.1553` n `67`; fx avg `0.1364` n `6`; index avg `0.1765` n `23`; metal avg `0.3447` n `18`; unknown avg `0.4068` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
