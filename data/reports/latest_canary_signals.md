# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T11:07:30.988212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0672` n `12`; crypto_alt avg `-0.182` n `228`; crypto_major avg `-0.195` n `8`; equity avg `-0.0131` n `78`; fx avg `0.094` n `6`; index avg `0.0021` n `23`; metal avg `-0.0743` n `18`; unknown avg `-0.02` n `702`
- 1h: commodity avg `-0.0901` n `12`; crypto_alt avg `-0.0704` n `228`; crypto_major avg `-0.0752` n `8`; equity avg `0.0075` n `78`; fx avg `-0.0023` n `6`; index avg `0.0005` n `23`; metal avg `-0.0561` n `18`; unknown avg `-0.0632` n `702`
- 4h: commodity avg `-0.0876` n `12`; crypto_alt avg `0.4428` n `228`; crypto_major avg `-0.1287` n `8`; equity avg `-0.0457` n `78`; fx avg `-0.0069` n `6`; index avg `-0.0002` n `23`; metal avg `-0.0834` n `18`; unknown avg `-0.0362` n `694`
- 24h: commodity avg `0.0099` n `12`; crypto_alt avg `1.4516` n `228`; crypto_major avg `0.0671` n `8`; equity avg `0.4518` n `78`; fx avg `0.0262` n `6`; index avg `0.0347` n `23`; metal avg `-0.0623` n `18`; unknown avg `0.2981` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
