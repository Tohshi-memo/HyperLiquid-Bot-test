# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T22:37:31.507729+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.066` n `228`; crypto_major avg `-0.0193` n `8`; equity avg `0.0307` n `78`; fx avg `-0.0179` n `6`; index avg `0.0032` n `23`; metal avg `0.0033` n `18`; unknown avg `-0.1329` n `687`
- 1h: commodity avg `0.1088` n `12`; crypto_alt avg `0.109` n `228`; crypto_major avg `0.1483` n `8`; equity avg `0.0127` n `78`; fx avg `0.0301` n `6`; index avg `0.0002` n `23`; metal avg `0.009` n `18`; unknown avg `-0.0262` n `687`
- 4h: commodity avg `0.1586` n `12`; crypto_alt avg `-0.0843` n `228`; crypto_major avg `0.0686` n `8`; equity avg `0.012` n `78`; fx avg `-0.0504` n `6`; index avg `-0.0126` n `23`; metal avg `0.1459` n `18`; unknown avg `-0.538` n `687`
- 24h: commodity avg `0.458` n `12`; crypto_alt avg `-3.681` n `228`; crypto_major avg `-4.5227` n `8`; equity avg `0.7148` n `78`; fx avg `-0.123` n `6`; index avg `0.209` n `23`; metal avg `-4.1082` n `18`; unknown avg `-0.7814` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
