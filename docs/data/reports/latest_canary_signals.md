# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T18:07:36.191925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.1815` n `230`; crypto_major avg `0.2231` n `8`; equity avg `0.0076` n `107`; fx avg `0.0044` n `6`; index avg `0.0284` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0298` n `782`
- 1h: commodity avg `-0.0697` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `-0.0141` n `8`; equity avg `0.2029` n `107`; fx avg `0.0025` n `6`; index avg `0.0585` n `25`; metal avg `-0.06` n `20`; unknown avg `-0.1505` n `782`
- 4h: commodity avg `-0.1069` n `12`; crypto_alt avg `0.4159` n `230`; crypto_major avg `0.4567` n `8`; equity avg `1.3829` n `107`; fx avg `0.0629` n `6`; index avg `0.3021` n `25`; metal avg `0.1168` n `20`; unknown avg `-0.1502` n `782`
- 24h: commodity avg `-1.1128` n `12`; crypto_alt avg `-0.1621` n `230`; crypto_major avg `0.2937` n `8`; equity avg `3.7193` n `107`; fx avg `0.1061` n `6`; index avg `0.776` n `25`; metal avg `1.1674` n `20`; unknown avg `0.3849` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
