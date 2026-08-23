# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T12:37:28.969690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0325` n `230`; crypto_major avg `-0.006` n `8`; equity avg `0.0028` n `121`; fx avg `-0.0018` n `6`; index avg `-0.0007` n `25`; metal avg `0.0163` n `20`; unknown avg `0.8707` n `795`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.0452` n `230`; crypto_major avg `-0.3225` n `8`; equity avg `0.043` n `121`; fx avg `0.0015` n `6`; index avg `0.0118` n `25`; metal avg `0.0193` n `20`; unknown avg `1.8553` n `795`
- 4h: commodity avg `-0.0132` n `12`; crypto_alt avg `2.0123` n `230`; crypto_major avg `0.8305` n `8`; equity avg `0.2331` n `121`; fx avg `-0.0015` n `6`; index avg `0.0397` n `25`; metal avg `0.0375` n `20`; unknown avg `2.1727` n `794`
- 24h: commodity avg `-0.0084` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `0.3276` n `8`; equity avg `0.4496` n `121`; fx avg `0.0365` n `6`; index avg `0.0368` n `25`; metal avg `0.0677` n `20`; unknown avg `5.8266` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
