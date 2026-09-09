# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T06:07:27.374975+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.0732` n `233`; crypto_major avg `0.1626` n `8`; equity avg `0.0924` n `134`; fx avg `-0.0401` n `6`; index avg `0.0047` n `26`; metal avg `0.0324` n `20`; unknown avg `-0.0722` n `778`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.1485` n `233`; crypto_major avg `-0.1481` n `8`; equity avg `-0.0373` n `134`; fx avg `-0.0173` n `6`; index avg `-0.0032` n `26`; metal avg `0.135` n `20`; unknown avg `0.1164` n `778`
- 4h: commodity avg `-0.1155` n `12`; crypto_alt avg `0.3102` n `233`; crypto_major avg `0.1735` n `8`; equity avg `-0.084` n `134`; fx avg `-0.0666` n `6`; index avg `-0.0261` n `26`; metal avg `0.1965` n `20`; unknown avg `0.4437` n `769`
- 24h: commodity avg `-0.1779` n `12`; crypto_alt avg `-0.0735` n `232`; crypto_major avg `1.1051` n `8`; equity avg `0.9523` n `134`; fx avg `-0.0922` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0565` n `20`; unknown avg `0.2241` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
