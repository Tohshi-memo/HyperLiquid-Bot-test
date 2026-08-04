# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T15:23:00.196684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1003` n `12`; crypto_alt avg `-0.1821` n `230`; crypto_major avg `-0.1837` n `8`; equity avg `0.1638` n `107`; fx avg `-0.0026` n `6`; index avg `0.0562` n `25`; metal avg `-0.0788` n `20`; unknown avg `0.0196` n `782`
- 1h: commodity avg `0.0565` n `12`; crypto_alt avg `0.1834` n `230`; crypto_major avg `0.3639` n `8`; equity avg `0.91` n `107`; fx avg `0.0087` n `6`; index avg `0.1326` n `25`; metal avg `0.0439` n `20`; unknown avg `0.0448` n `782`
- 4h: commodity avg `-0.9385` n `12`; crypto_alt avg `-0.3476` n `230`; crypto_major avg `-0.0084` n `8`; equity avg `1.2978` n `107`; fx avg `-0.0401` n `6`; index avg `0.3451` n `25`; metal avg `0.4034` n `20`; unknown avg `-0.2214` n `781`
- 24h: commodity avg `-0.9727` n `12`; crypto_alt avg `-0.2881` n `230`; crypto_major avg `0.297` n `8`; equity avg `4.2026` n `107`; fx avg `0.0706` n `6`; index avg `0.7899` n `25`; metal avg `1.0092` n `20`; unknown avg `0.7149` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
