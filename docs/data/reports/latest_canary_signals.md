# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T21:07:33.809819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `5.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.1231` n `8`; equity avg `-0.0273` n `92`; fx avg `0.0027` n `6`; index avg `0.0054` n `25`; metal avg `0.0111` n `20`; unknown avg `-0.3644` n `768`
- 1h: commodity avg `-0.0559` n `12`; crypto_alt avg `0.0164` n `230`; crypto_major avg `0.1198` n `8`; equity avg `-0.0041` n `92`; fx avg `0.0118` n `6`; index avg `-0.0003` n `25`; metal avg `-0.0402` n `20`; unknown avg `-0.1389` n `768`
- 4h: commodity avg `0.1264` n `12`; crypto_alt avg `-0.3184` n `230`; crypto_major avg `0.2833` n `8`; equity avg `0.1742` n `92`; fx avg `-0.0013` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.0244` n `766`
- 24h: commodity avg `0.3208` n `12`; crypto_alt avg `1.8567` n `230`; crypto_major avg `3.5065` n `8`; equity avg `1.3468` n `92`; fx avg `0.0027` n `6`; index avg `0.4284` n `25`; metal avg `0.5652` n `20`; unknown avg `0.2009` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
