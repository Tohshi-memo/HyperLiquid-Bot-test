# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T16:09:23.113737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1617` n `12`; crypto_alt avg `0.1761` n `229`; crypto_major avg `0.1564` n `8`; equity avg `0.1666` n `91`; fx avg `-0.0092` n `6`; index avg `0.0442` n `25`; metal avg `0.0355` n `20`; unknown avg `0.0631` n `766`
- 1h: commodity avg `-0.0293` n `12`; crypto_alt avg `0.047` n `229`; crypto_major avg `0.0762` n `8`; equity avg `0.2118` n `91`; fx avg `-0.0306` n `6`; index avg `0.0702` n `25`; metal avg `0.0956` n `20`; unknown avg `-0.0987` n `766`
- 4h: commodity avg `-0.4844` n `12`; crypto_alt avg `-0.283` n `229`; crypto_major avg `-0.5533` n `8`; equity avg `-0.5539` n `91`; fx avg `-0.0902` n `6`; index avg `0.0997` n `25`; metal avg `0.1386` n `20`; unknown avg `-0.2322` n `766`
- 24h: commodity avg `-0.4954` n `12`; crypto_alt avg `0.8817` n `229`; crypto_major avg `1.1096` n `8`; equity avg `-1.1635` n `91`; fx avg `-0.1647` n `6`; index avg `0.0118` n `25`; metal avg `-0.1383` n `20`; unknown avg `-0.218` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
