# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T23:07:32.199244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `0.0084` n `8`; equity avg `-0.0966` n `114`; fx avg `-0.0329` n `6`; index avg `-0.0198` n `25`; metal avg `-0.0004` n `20`; unknown avg `-0.0309` n `793`
- 1h: commodity avg `-0.0383` n `12`; crypto_alt avg `-0.2921` n `230`; crypto_major avg `-0.0139` n `8`; equity avg `-0.1276` n `114`; fx avg `-0.0417` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0184` n `20`; unknown avg `-0.0839` n `792`
- 4h: commodity avg `0.1292` n `12`; crypto_alt avg `-0.3576` n `230`; crypto_major avg `0.0159` n `8`; equity avg `0.0072` n `114`; fx avg `-0.0329` n `6`; index avg `0.0022` n `25`; metal avg `0.0202` n `20`; unknown avg `-0.0825` n `792`
- 24h: commodity avg `0.5635` n `12`; crypto_alt avg `0.3306` n `230`; crypto_major avg `1.374` n `8`; equity avg `1.1309` n `114`; fx avg `-0.0039` n `6`; index avg `0.0595` n `25`; metal avg `0.1264` n `20`; unknown avg `0.2569` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
