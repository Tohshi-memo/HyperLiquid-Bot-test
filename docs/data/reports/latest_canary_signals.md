# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T16:22:12.866510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.1466` n `228`; crypto_major avg `-0.0924` n `8`; equity avg `0.0004` n `88`; fx avg `0.005` n `6`; index avg `-0.0092` n `23`; metal avg `0.0125` n `20`; unknown avg `-0.3771` n `764`
- 1h: commodity avg `0.0679` n `12`; crypto_alt avg `-0.181` n `228`; crypto_major avg `-0.1062` n `8`; equity avg `-0.0389` n `88`; fx avg `0.0` n `6`; index avg `-0.0297` n `23`; metal avg `-0.0035` n `20`; unknown avg `-0.7716` n `764`
- 4h: commodity avg `0.1185` n `12`; crypto_alt avg `0.178` n `228`; crypto_major avg `-0.0463` n `8`; equity avg `0.0269` n `88`; fx avg `-0.0039` n `6`; index avg `-0.0129` n `23`; metal avg `-0.0513` n `20`; unknown avg `0.1003` n `764`
- 24h: commodity avg `0.4167` n `12`; crypto_alt avg `-0.7451` n `228`; crypto_major avg `-1.6067` n `8`; equity avg `0.0157` n `88`; fx avg `-0.0097` n `6`; index avg `-0.0702` n `23`; metal avg `-0.0693` n `20`; unknown avg `14.8557` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
