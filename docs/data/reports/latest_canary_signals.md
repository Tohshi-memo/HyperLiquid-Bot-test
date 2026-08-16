# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T15:41:22.431213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.0528` n `230`; crypto_major avg `0.031` n `8`; equity avg `0.024` n `114`; fx avg `-0.0043` n `6`; index avg `0.0016` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0636` n `791`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `0.1313` n `230`; crypto_major avg `0.0744` n `8`; equity avg `0.0369` n `114`; fx avg `0.0068` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0067` n `20`; unknown avg `0.0719` n `791`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.1464` n `230`; crypto_major avg `0.1781` n `8`; equity avg `0.0358` n `114`; fx avg `0.0001` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.1038` n `791`
- 24h: commodity avg `0.0651` n `12`; crypto_alt avg `-0.1584` n `230`; crypto_major avg `0.0483` n `8`; equity avg `0.2922` n `114`; fx avg `-0.0072` n `6`; index avg `0.0237` n `25`; metal avg `0.0344` n `20`; unknown avg `0.1825` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
