# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T03:37:32.060589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.1055` n `235`; crypto_major avg `0.0605` n `8`; equity avg `-0.0335` n `150`; fx avg `-0.0044` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.1404` n `1117`
- 1h: commodity avg `0.1118` n `13`; crypto_alt avg `-0.8958` n `235`; crypto_major avg `-0.3144` n `8`; equity avg `-0.1017` n `150`; fx avg `0.0012` n `6`; index avg `-0.0171` n `26`; metal avg `-0.0075` n `20`; unknown avg `-0.0034` n `1115`
- 4h: commodity avg `0.1478` n `13`; crypto_alt avg `-0.5661` n `235`; crypto_major avg `-0.2552` n `8`; equity avg `-0.1023` n `150`; fx avg `-0.0073` n `6`; index avg `-0.0129` n `26`; metal avg `0.0022` n `20`; unknown avg `-0.0911` n `1109`
- 24h: commodity avg `0.1914` n `13`; crypto_alt avg `0.6587` n `235`; crypto_major avg `0.286` n `8`; equity avg `-0.0044` n `150`; fx avg `-0.0044` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.3291` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
