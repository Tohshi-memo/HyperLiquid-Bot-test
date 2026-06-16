# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T15:37:49.404327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1402` n `12`; crypto_alt avg `0.397` n `228`; crypto_major avg `0.4006` n `8`; equity avg `0.0739` n `77`; fx avg `0.0065` n `6`; index avg `0.0775` n `23`; metal avg `0.0827` n `18`; unknown avg `0.1108` n `687`
- 1h: commodity avg `-0.0631` n `12`; crypto_alt avg `0.5724` n `228`; crypto_major avg `0.5157` n `8`; equity avg `0.0139` n `77`; fx avg `0.0539` n `6`; index avg `-0.1315` n `23`; metal avg `0.0943` n `18`; unknown avg `0.7414` n `687`
- 4h: commodity avg `-0.2818` n `12`; crypto_alt avg `-1.0839` n `228`; crypto_major avg `-0.8409` n `8`; equity avg `-1.3315` n `77`; fx avg `0.014` n `6`; index avg `-0.6362` n `23`; metal avg `-0.1089` n `18`; unknown avg `0.6538` n `687`
- 24h: commodity avg `-0.6454` n `12`; crypto_alt avg `-1.8225` n `228`; crypto_major avg `-0.4143` n `8`; equity avg `4.1306` n `77`; fx avg `-0.0293` n `6`; index avg `-0.4731` n `23`; metal avg `-0.3289` n `18`; unknown avg `0.5316` n `623`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
