# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T19:07:29.248674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `0.0407` n `230`; crypto_major avg `0.0589` n `8`; equity avg `-0.0033` n `92`; fx avg `-0.0042` n `6`; index avg `0.0005` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.0409` n `765`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.0749` n `230`; crypto_major avg `0.1776` n `8`; equity avg `0.0465` n `92`; fx avg `-0.0065` n `6`; index avg `-0.0125` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0565` n `765`
- 4h: commodity avg `0.0447` n `12`; crypto_alt avg `0.0611` n `230`; crypto_major avg `0.0806` n `8`; equity avg `0.1533` n `92`; fx avg `-0.0049` n `6`; index avg `-0.0007` n `25`; metal avg `0.003` n `20`; unknown avg `0.1356` n `765`
- 24h: commodity avg `0.0031` n `12`; crypto_alt avg `1.3338` n `229`; crypto_major avg `1.0803` n `8`; equity avg `0.2122` n `92`; fx avg `-0.0041` n `6`; index avg `0.0092` n `25`; metal avg `0.0783` n `20`; unknown avg `2.3832` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
