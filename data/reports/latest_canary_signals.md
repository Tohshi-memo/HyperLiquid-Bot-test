# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T17:37:28.540411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `-0.0288` n `230`; crypto_major avg `0.1047` n `8`; equity avg `0.0803` n `92`; fx avg `0.008` n `6`; index avg `-0.0008` n `25`; metal avg `0.0152` n `20`; unknown avg `0.0123` n `766`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `-0.363` n `230`; crypto_major avg `-0.4354` n `8`; equity avg `-0.0039` n `92`; fx avg `-0.0172` n `6`; index avg `0.0121` n `25`; metal avg `0.0179` n `20`; unknown avg `0.3383` n `766`
- 4h: commodity avg `-0.1302` n `12`; crypto_alt avg `-0.2415` n `230`; crypto_major avg `0.0689` n `8`; equity avg `0.1445` n `92`; fx avg `-0.0197` n `6`; index avg `0.066` n `25`; metal avg `-0.0901` n `20`; unknown avg `-0.2858` n `758`
- 24h: commodity avg `0.3874` n `12`; crypto_alt avg `1.7325` n `230`; crypto_major avg `3.1225` n `8`; equity avg `1.1273` n `92`; fx avg `-0.016` n `6`; index avg `0.3347` n `25`; metal avg `0.6429` n `20`; unknown avg `-0.0638` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
