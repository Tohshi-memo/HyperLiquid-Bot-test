# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T02:37:27.322174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0259` n `12`; crypto_alt avg `-0.0209` n `233`; crypto_major avg `-0.0225` n `8`; equity avg `-0.0031` n `136`; fx avg `-0.005` n `6`; index avg `-0.001` n `26`; metal avg `0.0015` n `20`; unknown avg `0.6832` n `838`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.2302` n `233`; crypto_major avg `0.0536` n `8`; equity avg `-0.0231` n `136`; fx avg `-0.0033` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0088` n `20`; unknown avg `2.9956` n `836`
- 4h: commodity avg `-0.056` n `12`; crypto_alt avg `1.2457` n `233`; crypto_major avg `0.2942` n `8`; equity avg `0.1104` n `136`; fx avg `-0.0003` n `6`; index avg `0.0126` n `26`; metal avg `-0.0298` n `20`; unknown avg `0.7916` n `820`
- 24h: commodity avg `-0.6034` n `12`; crypto_alt avg `1.6857` n `233`; crypto_major avg `1.4251` n `8`; equity avg `1.0735` n `136`; fx avg `-0.1612` n `6`; index avg `0.3335` n `26`; metal avg `0.3156` n `20`; unknown avg `30.1779` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
