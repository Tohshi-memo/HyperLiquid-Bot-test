# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T12:22:31.914507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1047` n `12`; crypto_alt avg `-0.0099` n `230`; crypto_major avg `0.1131` n `8`; equity avg `0.0211` n `112`; fx avg `0.004` n `6`; index avg `-0.0124` n `25`; metal avg `-0.0556` n `20`; unknown avg `0.054` n `782`
- 1h: commodity avg `0.1172` n `12`; crypto_alt avg `-0.0313` n `230`; crypto_major avg `0.1832` n `8`; equity avg `-0.0326` n `112`; fx avg `0.0109` n `6`; index avg `0.0163` n `25`; metal avg `-0.1118` n `20`; unknown avg `0.0424` n `782`
- 4h: commodity avg `-0.2168` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `1.0017` n `8`; equity avg `0.1915` n `112`; fx avg `-0.0019` n `6`; index avg `0.0447` n `25`; metal avg `-0.1618` n `20`; unknown avg `0.2184` n `782`
- 24h: commodity avg `0.2436` n `12`; crypto_alt avg `0.5988` n `230`; crypto_major avg `0.6722` n `8`; equity avg `2.4024` n `109`; fx avg `-0.0659` n `6`; index avg `0.1475` n `25`; metal avg `0.2152` n `20`; unknown avg `0.4474` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
