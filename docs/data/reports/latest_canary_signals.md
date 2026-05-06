# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T16:07:23.096289+00:00`
- Correlation status: `ready`
- Asset price records: `468`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `7.68` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.7408` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `0.1811` n `228`; crypto_major avg `0.0623` n `8`; equity avg `0.1387` n `65`; fx avg `0.0415` n `4`; index avg `0.0181` n `23`; metal avg `-0.1599` n `18`; unknown avg `0.1029` n `356`
- 1h: commodity avg `0.1487` n `12`; crypto_alt avg `0.4067` n `228`; crypto_major avg `0.2113` n `8`; equity avg `0.2361` n `65`; fx avg `0.051` n `4`; index avg `0.029` n `23`; metal avg `-0.2062` n `18`; unknown avg `0.2427` n `356`
- 4h: commodity avg `0.3213` n `7`; crypto_alt avg `-0.4504` n `223`; crypto_major avg `-1.3551` n `7`; equity avg `-0.2671` n `47`; fx avg `0.0626` n `4`; index avg `-0.3934` n `6`; metal avg `0.3857` n `7`; unknown avg `8.4277` n `313`
- 24h: commodity avg `-2.3062` n `7`; crypto_alt avg `3.0974` n `223`; crypto_major avg `1.0238` n `7`; equity avg `2.3429` n `47`; fx avg `-0.4249` n `4`; index avg `1.798` n `6`; metal avg `2.8986` n `7`; unknown avg `17.9866` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2422`, n `464`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1758`, n `460`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1605`, n `460`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1503`, n `464`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1493`, n `460`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1367`, n `460`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `464`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `464`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `464`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `464`, weak_sample_signal
