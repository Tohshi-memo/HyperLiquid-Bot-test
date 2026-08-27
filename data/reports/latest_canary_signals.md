# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T01:52:26.851136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `0.1032` n `231`; crypto_major avg `0.1114` n `8`; equity avg `-0.033` n `126`; fx avg `-0.0009` n `6`; index avg `-0.0002` n `25`; metal avg `0.05` n `20`; unknown avg `-0.1788` n `793`
- 1h: commodity avg `-0.0029` n `12`; crypto_alt avg `0.2627` n `231`; crypto_major avg `0.5026` n `8`; equity avg `0.421` n `126`; fx avg `0.01` n `6`; index avg `0.0602` n `25`; metal avg `0.2116` n `20`; unknown avg `0.5194` n `793`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `0.8905` n `231`; crypto_major avg `0.8765` n `8`; equity avg `-0.2745` n `126`; fx avg `-0.0831` n `6`; index avg `-0.0656` n `25`; metal avg `0.2751` n `20`; unknown avg `-0.1009` n `793`
- 24h: commodity avg `0.3699` n `12`; crypto_alt avg `1.0424` n `231`; crypto_major avg `1.1342` n `8`; equity avg `1.769` n `125`; fx avg `-0.1129` n `6`; index avg `0.3103` n `25`; metal avg `-0.174` n `20`; unknown avg `0.9111` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
