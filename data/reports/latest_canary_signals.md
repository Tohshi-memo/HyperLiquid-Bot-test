# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T23:52:29.462768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0708` n `12`; crypto_alt avg `-0.0644` n `228`; crypto_major avg `-0.0661` n `8`; equity avg `-0.0416` n `78`; fx avg `0.0249` n `6`; index avg `0.0276` n `23`; metal avg `-0.0175` n `18`; unknown avg `0.248` n `679`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `0.0948` n `228`; crypto_major avg `-0.0239` n `8`; equity avg `0.0779` n `78`; fx avg `0.0075` n `6`; index avg `0.0731` n `23`; metal avg `-0.0393` n `18`; unknown avg `-0.0475` n `679`
- 4h: commodity avg `0.1085` n `12`; crypto_alt avg `0.29` n `228`; crypto_major avg `0.0864` n `8`; equity avg `0.2114` n `78`; fx avg `0.0049` n `6`; index avg `0.0642` n `23`; metal avg `0.1066` n `18`; unknown avg `-0.3967` n `679`
- 24h: commodity avg `0.3842` n `12`; crypto_alt avg `-3.5408` n `228`; crypto_major avg `-4.4666` n `8`; equity avg `0.8906` n `78`; fx avg `-0.089` n `6`; index avg `0.2877` n `23`; metal avg `-4.1105` n `18`; unknown avg `-0.4002` n `564`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
