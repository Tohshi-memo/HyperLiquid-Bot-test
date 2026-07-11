# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T22:37:27.866896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1943` n `12`; crypto_alt avg `0.1106` n `230`; crypto_major avg `0.1213` n `8`; equity avg `0.0025` n `92`; fx avg `0.0029` n `6`; index avg `-0.0156` n `25`; metal avg `0.004` n `20`; unknown avg `0.0014` n `765`
- 1h: commodity avg `0.1951` n `12`; crypto_alt avg `-0.4706` n `230`; crypto_major avg `-0.3069` n `8`; equity avg `-0.0098` n `92`; fx avg `0.0051` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.1135` n `765`
- 4h: commodity avg `0.1485` n `12`; crypto_alt avg `-0.5801` n `230`; crypto_major avg `-0.2587` n `8`; equity avg `0.0065` n `92`; fx avg `0.0081` n `6`; index avg `-0.0195` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.2128` n `765`
- 24h: commodity avg `0.1948` n `12`; crypto_alt avg `0.1602` n `229`; crypto_major avg `0.4882` n `8`; equity avg `0.3432` n `92`; fx avg `0.0443` n `6`; index avg `0.0055` n `25`; metal avg `-0.0259` n `20`; unknown avg `2.6067` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
