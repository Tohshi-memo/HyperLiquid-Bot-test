# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T01:37:31.602229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `0.057` n `230`; crypto_major avg `0.0954` n `8`; equity avg `0.2189` n `112`; fx avg `-0.0152` n `6`; index avg `0.0164` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0507` n `782`
- 1h: commodity avg `-0.14` n `12`; crypto_alt avg `0.1446` n `230`; crypto_major avg `0.1356` n `8`; equity avg `-0.2424` n `112`; fx avg `-0.0446` n `6`; index avg `-0.1029` n `25`; metal avg `0.0664` n `20`; unknown avg `0.0454` n `782`
- 4h: commodity avg `0.0042` n `12`; crypto_alt avg `0.4002` n `230`; crypto_major avg `0.0398` n `8`; equity avg `0.0346` n `112`; fx avg `-0.0552` n `6`; index avg `-0.1277` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0147` n `782`
- 24h: commodity avg `0.3836` n `12`; crypto_alt avg `0.5243` n `230`; crypto_major avg `-0.8203` n `8`; equity avg `0.8347` n `109`; fx avg `0.045` n `6`; index avg `-0.1082` n `25`; metal avg `-0.2588` n `20`; unknown avg `113.1395` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
