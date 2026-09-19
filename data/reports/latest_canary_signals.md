# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T21:52:29.388248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `0.3293` n `234`; crypto_major avg `0.1881` n `8`; equity avg `0.0293` n `140`; fx avg `0.0043` n `6`; index avg `0.0009` n `26`; metal avg `0.0011` n `20`; unknown avg `1.0174` n `943`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `-0.6255` n `234`; crypto_major avg `-0.5186` n `8`; equity avg `0.0051` n `140`; fx avg `0.0195` n `6`; index avg `0.0301` n `26`; metal avg `-0.004` n `20`; unknown avg `0.4687` n `941`
- 4h: commodity avg `0.0153` n `12`; crypto_alt avg `-0.8479` n `234`; crypto_major avg `-0.9485` n `8`; equity avg `0.1195` n `140`; fx avg `-0.0328` n `6`; index avg `0.0323` n `26`; metal avg `0.0048` n `20`; unknown avg `107.9533` n `919`
- 24h: commodity avg `0.0532` n `12`; crypto_alt avg `0.4865` n `234`; crypto_major avg `-0.4328` n `8`; equity avg `-0.0444` n `140`; fx avg `-0.0739` n `6`; index avg `0.019` n `26`; metal avg `-0.0153` n `20`; unknown avg `5.7455` n `836`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
