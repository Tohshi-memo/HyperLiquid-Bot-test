# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T04:37:25.070010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.1825` n `230`; crypto_major avg `-0.056` n `8`; equity avg `-0.0284` n `112`; fx avg `0.0005` n `6`; index avg `-0.0172` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.2054` n `782`
- 1h: commodity avg `0.0724` n `12`; crypto_alt avg `-0.367` n `230`; crypto_major avg `-0.2273` n `8`; equity avg `-0.0613` n `112`; fx avg `-0.0152` n `6`; index avg `0.0001` n `25`; metal avg `0.017` n `20`; unknown avg `-0.3716` n `782`
- 4h: commodity avg `0.0167` n `12`; crypto_alt avg `-0.3899` n `230`; crypto_major avg `-0.315` n `8`; equity avg `0.2629` n `112`; fx avg `-0.0377` n `6`; index avg `-0.0686` n `25`; metal avg `0.1896` n `20`; unknown avg `-0.3528` n `782`
- 24h: commodity avg `0.7642` n `12`; crypto_alt avg `-0.1198` n `230`; crypto_major avg `-1.1031` n `8`; equity avg `0.7144` n `109`; fx avg `0.0238` n `6`; index avg `-0.1243` n `25`; metal avg `-0.0003` n `20`; unknown avg `113.1148` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
