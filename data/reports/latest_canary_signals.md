# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T05:37:21.173032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `0.1303` n `231`; crypto_major avg `-0.0074` n `8`; equity avg `-0.0085` n `128`; fx avg `-0.0005` n `6`; index avg `0.0037` n `26`; metal avg `0.0013` n `20`; unknown avg `-0.2396` n `793`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `0.3128` n `231`; crypto_major avg `0.0719` n `8`; equity avg `0.0042` n `128`; fx avg `-0.0012` n `6`; index avg `0.0358` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.4387` n `793`
- 4h: commodity avg `0.0075` n `12`; crypto_alt avg `0.3929` n `231`; crypto_major avg `0.052` n `8`; equity avg `0.0235` n `128`; fx avg `0.0052` n `6`; index avg `0.008` n `26`; metal avg `-0.0053` n `20`; unknown avg `-0.6939` n `793`
- 24h: commodity avg `0.0172` n `12`; crypto_alt avg `0.3213` n `231`; crypto_major avg `0.5067` n `8`; equity avg `0.2885` n `128`; fx avg `-0.0132` n `6`; index avg `0.0753` n `26`; metal avg `0.0787` n `20`; unknown avg `0.1302` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
