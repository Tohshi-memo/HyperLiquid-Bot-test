# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T23:07:26.532689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.0746` n `230`; crypto_major avg `0.0747` n `8`; equity avg `-0.0398` n `120`; fx avg `-0.0012` n `6`; index avg `0.0223` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.0504` n `789`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.0103` n `230`; crypto_major avg `0.0057` n `8`; equity avg `-0.2079` n `120`; fx avg `-0.0036` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0362` n `20`; unknown avg `-0.144` n `789`
- 4h: commodity avg `0.0774` n `12`; crypto_alt avg `-0.3316` n `230`; crypto_major avg `-0.171` n `8`; equity avg `-0.3755` n `120`; fx avg `-0.0094` n `6`; index avg `-0.05` n `25`; metal avg `-0.161` n `20`; unknown avg `-0.1701` n `789`
- 24h: commodity avg `0.3034` n `12`; crypto_alt avg `-0.4588` n `230`; crypto_major avg `0.1524` n `8`; equity avg `-4.6866` n `120`; fx avg `-0.0217` n `6`; index avg `-0.7189` n `25`; metal avg `-0.7988` n `20`; unknown avg `-0.2021` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
