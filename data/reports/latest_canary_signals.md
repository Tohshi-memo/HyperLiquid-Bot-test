# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T00:07:33.369782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `0.1276` n `229`; crypto_major avg `0.1948` n `8`; equity avg `0.0208` n `88`; fx avg `-0.0094` n `6`; index avg `-0.0022` n `25`; metal avg `-0.002` n `20`; unknown avg `0.5371` n `765`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.2593` n `229`; crypto_major avg `0.3532` n `8`; equity avg `0.0043` n `88`; fx avg `-0.0131` n `6`; index avg `-0.0207` n `25`; metal avg `0.011` n `20`; unknown avg `0.8336` n `765`
- 4h: commodity avg `0.0005` n `12`; crypto_alt avg `0.39` n `229`; crypto_major avg `0.3424` n `8`; equity avg `0.0171` n `88`; fx avg `-0.0264` n `6`; index avg `-0.0401` n `25`; metal avg `0.0366` n `20`; unknown avg `1.4024` n `765`
- 24h: commodity avg `0.1818` n `12`; crypto_alt avg `3.2986` n `229`; crypto_major avg `3.3538` n `8`; equity avg `1.6368` n `88`; fx avg `-0.1811` n `6`; index avg `0.3868` n `25`; metal avg `0.5111` n `20`; unknown avg `7.0669` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
