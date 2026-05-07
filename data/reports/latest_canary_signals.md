# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T00:37:21.530617+00:00`
- Correlation status: `ready`
- Asset price records: `502`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.98` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `-0.2908` n `228`; crypto_major avg `-0.2051` n `8`; equity avg `-0.1024` n `65`; fx avg `0.0275` n `4`; index avg `0.0096` n `23`; metal avg `-0.0513` n `18`; unknown avg `0.0044` n `356`
- 1h: commodity avg `0.1181` n `12`; crypto_alt avg `-0.3437` n `228`; crypto_major avg `-0.27` n `8`; equity avg `-0.3856` n `65`; fx avg `0.0541` n `4`; index avg `-0.0067` n `23`; metal avg `0.0231` n `18`; unknown avg `-0.0376` n `356`
- 4h: commodity avg `0.1033` n `12`; crypto_alt avg `-0.2218` n `228`; crypto_major avg `-0.4108` n `8`; equity avg `-0.561` n `65`; fx avg `0.0635` n `4`; index avg `-0.0733` n `23`; metal avg `-0.0075` n `18`; unknown avg `-0.0356` n `356`
- 24h: commodity avg `-1.8789` n `7`; crypto_alt avg `1.914` n `223`; crypto_major avg `0.207` n `7`; equity avg `1.6645` n `47`; fx avg `-0.3086` n `4`; index avg `1.3719` n `6`; metal avg `2.6975` n `7`; unknown avg `3.5325` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1292`, n `498`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `498`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0822`, n `494`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0804`, n `494`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0738`, n `494`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `494`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0716`, n `494`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0643`, n `498`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0597`, n `494`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `498`, weak_sample_signal
