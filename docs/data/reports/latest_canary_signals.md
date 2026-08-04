# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T17:22:40.113434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5466` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0359` n `12`; crypto_alt avg `-0.0244` n `230`; crypto_major avg `-0.0993` n `8`; equity avg `0.0172` n `107`; fx avg `-0.0053` n `6`; index avg `-0.0128` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0805` n `782`
- 1h: commodity avg `0.0129` n `12`; crypto_alt avg `0.1301` n `230`; crypto_major avg `0.0934` n `8`; equity avg `0.0502` n `107`; fx avg `0.0124` n `6`; index avg `0.0558` n `25`; metal avg `0.1209` n `20`; unknown avg `-0.0844` n `782`
- 4h: commodity avg `-0.2478` n `12`; crypto_alt avg `0.1535` n `230`; crypto_major avg `0.1097` n `8`; equity avg `1.6563` n `107`; fx avg `0.0367` n `6`; index avg `0.3713` n `25`; metal avg `0.2939` n `20`; unknown avg `-0.3192` n `781`
- 24h: commodity avg `-1.1169` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `0.2863` n `8`; equity avg `4.12` n `107`; fx avg `0.0774` n `6`; index avg `0.7991` n `25`; metal avg `1.2433` n `20`; unknown avg `0.4087` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
