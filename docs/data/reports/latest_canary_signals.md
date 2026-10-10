# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T18:07:26.959023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `0.0438` n `235`; crypto_major avg `-0.0105` n `8`; equity avg `0.0043` n `150`; fx avg `0.0` n `6`; index avg `0.0001` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.3761` n `1107`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.0324` n `235`; crypto_major avg `0.028` n `8`; equity avg `0.003` n `150`; fx avg `-0.005` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.2599` n `1075`
- 4h: commodity avg `-0.0045` n `13`; crypto_alt avg `0.7203` n `235`; crypto_major avg `0.3222` n `8`; equity avg `0.0765` n `150`; fx avg `-0.0031` n `6`; index avg `0.01` n `26`; metal avg `-0.0214` n `20`; unknown avg `-0.014` n `1053`
- 24h: commodity avg `-0.3809` n `13`; crypto_alt avg `2.2032` n `235`; crypto_major avg `0.6659` n `8`; equity avg `0.1185` n `150`; fx avg `-0.0087` n `6`; index avg `0.0236` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.2669` n `944`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
