# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T23:37:30.293843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.0049` n `230`; crypto_major avg `-0.0104` n `8`; equity avg `-0.0332` n `112`; fx avg `-0.0005` n `6`; index avg `0.0086` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.025` n `782`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.173` n `230`; crypto_major avg `-0.2547` n `8`; equity avg `0.062` n `112`; fx avg `-0.009` n `6`; index avg `0.0133` n `25`; metal avg `0.053` n `20`; unknown avg `-0.1633` n `782`
- 4h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.1422` n `230`; crypto_major avg `-0.239` n `8`; equity avg `0.2384` n `112`; fx avg `-0.0019` n `6`; index avg `0.0184` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.1036` n `781`
- 24h: commodity avg `0.6382` n `12`; crypto_alt avg `-0.0234` n `230`; crypto_major avg `-1.2863` n `8`; equity avg `0.5379` n `109`; fx avg `0.0163` n `6`; index avg `-0.1564` n `25`; metal avg `-0.1413` n `20`; unknown avg `112.7032` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
