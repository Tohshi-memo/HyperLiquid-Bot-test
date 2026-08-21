# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T10:22:26.927406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8479` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.3085` n `230`; crypto_major avg `0.119` n `8`; equity avg `-0.0314` n `121`; fx avg `-0.0012` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0167` n `20`; unknown avg `-0.0147` n `793`
- 1h: commodity avg `0.1604` n `12`; crypto_alt avg `1.452` n `230`; crypto_major avg `0.9112` n `8`; equity avg `0.2076` n `121`; fx avg `0.0041` n `6`; index avg `0.0083` n `25`; metal avg `-0.14` n `20`; unknown avg `0.1773` n `793`
- 4h: commodity avg `0.218` n `12`; crypto_alt avg `2.5169` n `230`; crypto_major avg `1.9849` n `8`; equity avg `0.7128` n `121`; fx avg `-0.0191` n `6`; index avg `0.0193` n `25`; metal avg `0.137` n `20`; unknown avg `0.4685` n `793`
- 24h: commodity avg `0.207` n `12`; crypto_alt avg `6.9999` n `230`; crypto_major avg `6.8218` n `8`; equity avg `0.4626` n `121`; fx avg `-0.0807` n `6`; index avg `-0.0182` n `25`; metal avg `0.7886` n `20`; unknown avg `2.5312` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
