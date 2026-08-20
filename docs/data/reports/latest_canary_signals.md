# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:22:26.653166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.474` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.2459` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8558` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.161` n `230`; crypto_major avg `-0.0022` n `8`; equity avg `0.033` n `121`; fx avg `0.0328` n `6`; index avg `0.0076` n `25`; metal avg `-0.0514` n `20`; unknown avg `0.0404` n `792`
- 1h: commodity avg `0.0861` n `12`; crypto_alt avg `0.0502` n `230`; crypto_major avg `0.6908` n `8`; equity avg `-0.2411` n `121`; fx avg `0.05` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0655` n `20`; unknown avg `0.4465` n `792`
- 4h: commodity avg `-0.1968` n `12`; crypto_alt avg `1.0467` n `230`; crypto_major avg `2.2772` n `8`; equity avg `0.0313` n `121`; fx avg `0.0174` n `6`; index avg `0.09` n `25`; metal avg `0.4214` n `20`; unknown avg `0.128` n `792`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `5.7102` n `230`; crypto_major avg `9.3105` n `8`; equity avg `-0.9992` n `121`; fx avg `0.1872` n `6`; index avg `-0.084` n `25`; metal avg `0.2413` n `20`; unknown avg `2.1614` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
