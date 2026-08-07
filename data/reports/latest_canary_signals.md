# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T01:52:29.034708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0375` n `12`; crypto_alt avg `-0.0382` n `230`; crypto_major avg `-0.0382` n `8`; equity avg `0.0201` n `112`; fx avg `-0.0132` n `6`; index avg `-0.0272` n `25`; metal avg `0.0584` n `20`; unknown avg `-0.0553` n `782`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0155` n `230`; crypto_major avg `0.0313` n `8`; equity avg `-0.2324` n `112`; fx avg `-0.049` n `6`; index avg `-0.1398` n `25`; metal avg `0.1788` n `20`; unknown avg `-0.0886` n `782`
- 4h: commodity avg `-0.096` n `12`; crypto_alt avg `-0.0275` n `230`; crypto_major avg `-0.0294` n `8`; equity avg `-0.3271` n `112`; fx avg `-0.0532` n `6`; index avg `-0.1631` n `25`; metal avg `0.096` n `20`; unknown avg `0.0563` n `782`
- 24h: commodity avg `0.4402` n `12`; crypto_alt avg `0.5484` n `230`; crypto_major avg `-0.7953` n `8`; equity avg `0.6479` n `109`; fx avg `0.0229` n `6`; index avg `-0.1257` n `25`; metal avg `-0.2536` n `20`; unknown avg `113.1453` n `749`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
