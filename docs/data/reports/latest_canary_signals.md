# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T06:37:25.236774+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `0.158` n `235`; crypto_major avg `0.0442` n `8`; equity avg `0.0002` n `150`; fx avg `0.0057` n `6`; index avg `-0.0005` n `26`; metal avg `0.0035` n `20`; unknown avg `0.233` n `1117`
- 1h: commodity avg `0.0363` n `13`; crypto_alt avg `0.2578` n `235`; crypto_major avg `-0.039` n `8`; equity avg `-0.0215` n `150`; fx avg `0.0064` n `6`; index avg `0.0005` n `26`; metal avg `0.0059` n `20`; unknown avg `0.6851` n `1099`
- 4h: commodity avg `0.1022` n `13`; crypto_alt avg `-0.5087` n `235`; crypto_major avg `-0.429` n `8`; equity avg `-0.112` n `150`; fx avg `0.0073` n `6`; index avg `-0.0169` n `26`; metal avg `-0.01` n `20`; unknown avg `0.9218` n `1093`
- 24h: commodity avg `0.1447` n `13`; crypto_alt avg `0.812` n `235`; crypto_major avg `-0.1275` n `8`; equity avg `-0.0197` n `150`; fx avg `-0.0043` n `6`; index avg `-0.0351` n `26`; metal avg `0.0002` n `20`; unknown avg `0.6938` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
