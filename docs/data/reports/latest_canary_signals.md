# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T07:37:27.140992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `-0.0478` n `230`; crypto_major avg `-0.0021` n `8`; equity avg `0.0047` n `112`; fx avg `0.0046` n `6`; index avg `0.0002` n `25`; metal avg `-0.0221` n `20`; unknown avg `-0.0656` n `782`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `-0.1162` n `230`; crypto_major avg `-0.0497` n `8`; equity avg `0.0037` n `112`; fx avg `0.0108` n `6`; index avg `0.0331` n `25`; metal avg `-0.0322` n `20`; unknown avg `-0.0739` n `782`
- 4h: commodity avg `0.0571` n `12`; crypto_alt avg `0.0412` n `230`; crypto_major avg `-0.0542` n `8`; equity avg `0.4098` n `112`; fx avg `-0.0357` n `6`; index avg `0.0885` n `25`; metal avg `0.2754` n `20`; unknown avg `-0.128` n `766`
- 24h: commodity avg `0.5388` n `12`; crypto_alt avg `0.061` n `230`; crypto_major avg `-0.9807` n `8`; equity avg `1.381` n `109`; fx avg `-0.1029` n `6`; index avg `-0.0119` n `25`; metal avg `0.2833` n `20`; unknown avg `110.659` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
