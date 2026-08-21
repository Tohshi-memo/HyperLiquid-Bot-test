# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T18:28:55.484993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0176` n `12`; crypto_alt avg `0.0804` n `230`; crypto_major avg `0.0749` n `8`; equity avg `0.0055` n `121`; fx avg `-0.0033` n `6`; index avg `-0.005` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0448` n `793`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `0.7636` n `230`; crypto_major avg `0.4423` n `8`; equity avg `0.0874` n `121`; fx avg `0.0093` n `6`; index avg `-0.0128` n `25`; metal avg `-0.0051` n `20`; unknown avg `-0.1587` n `793`
- 4h: commodity avg `0.0835` n `12`; crypto_alt avg `0.8256` n `230`; crypto_major avg `0.5421` n `8`; equity avg `0.3002` n `121`; fx avg `0.0245` n `6`; index avg `0.0417` n `25`; metal avg `-0.0177` n `20`; unknown avg `0.0936` n `793`
- 24h: commodity avg `0.2986` n `12`; crypto_alt avg `7.9445` n `230`; crypto_major avg `4.8472` n `8`; equity avg `1.4152` n `121`; fx avg `-0.096` n `6`; index avg `0.1483` n `25`; metal avg `0.658` n `20`; unknown avg `1.2265` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2006`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
