# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T15:52:28.850152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.935` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.0573` n `231`; crypto_major avg `-0.1542` n `8`; equity avg `0.0953` n `127`; fx avg `0.0011` n `6`; index avg `0.0384` n `26`; metal avg `0.0752` n `20`; unknown avg `0.1143` n `792`
- 1h: commodity avg `-0.0088` n `12`; crypto_alt avg `0.2264` n `231`; crypto_major avg `0.2299` n `8`; equity avg `-0.0811` n `127`; fx avg `0.0005` n `6`; index avg `0.0105` n `26`; metal avg `0.136` n `20`; unknown avg `-0.0555` n `791`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `1.2276` n `231`; crypto_major avg `1.61` n `8`; equity avg `-0.325` n `127`; fx avg `0.0251` n `6`; index avg `0.0025` n `26`; metal avg `0.1803` n `20`; unknown avg `0.0607` n `792`
- 24h: commodity avg `-0.0092` n `12`; crypto_alt avg `3.7173` n `231`; crypto_major avg `4.5667` n `8`; equity avg `1.6928` n `127`; fx avg `-0.064` n `6`; index avg `0.1879` n `26`; metal avg `0.1099` n `20`; unknown avg `0.8056` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
