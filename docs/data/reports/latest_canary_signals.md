# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T02:22:27.103552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `-0.1387` n `228`; crypto_major avg `-0.0421` n `8`; equity avg `0.013` n `78`; fx avg `-0.1002` n `6`; index avg `0.023` n `23`; metal avg `-0.0045` n `18`; unknown avg `0.0175` n `702`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `0.0028` n `228`; crypto_major avg `0.0293` n `8`; equity avg `0.0535` n `78`; fx avg `-0.0479` n `6`; index avg `0.0177` n `23`; metal avg `0.008` n `18`; unknown avg `0.0129` n `701`
- 4h: commodity avg `0.0414` n `12`; crypto_alt avg `0.3498` n `228`; crypto_major avg `-0.0284` n `8`; equity avg `0.1024` n `78`; fx avg `-0.1078` n `6`; index avg `0.0135` n `23`; metal avg `-0.0287` n `18`; unknown avg `69.497` n `701`
- 24h: commodity avg `0.1843` n `12`; crypto_alt avg `1.6254` n `228`; crypto_major avg `1.6917` n `8`; equity avg `0.5169` n `78`; fx avg `-0.0595` n `6`; index avg `0.0333` n `23`; metal avg `-0.0385` n `18`; unknown avg `1.6774` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
