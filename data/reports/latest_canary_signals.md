# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T08:52:36.995014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `13`; crypto_alt avg `0.1149` n `235`; crypto_major avg `0.0877` n `8`; equity avg `0.039` n `150`; fx avg `-0.016` n `6`; index avg `0.0044` n `26`; metal avg `-0.0762` n `20`; unknown avg `0.2074` n `1078`
- 1h: commodity avg `-0.1004` n `13`; crypto_alt avg `0.0604` n `235`; crypto_major avg `-0.0294` n `8`; equity avg `0.1344` n `150`; fx avg `-0.0261` n `6`; index avg `0.0177` n `26`; metal avg `-0.0632` n `20`; unknown avg `1.1291` n `1006`
- 4h: commodity avg `-0.102` n `13`; crypto_alt avg `0.7508` n `235`; crypto_major avg `0.4708` n `8`; equity avg `0.7359` n `150`; fx avg `0.0186` n `6`; index avg `0.097` n `26`; metal avg `0.1049` n `20`; unknown avg `0.5492` n `988`
- 24h: commodity avg `-0.4609` n `13`; crypto_alt avg `-0.8895` n `235`; crypto_major avg `-1.7963` n `8`; equity avg `-0.3218` n `150`; fx avg `0.1085` n `6`; index avg `0.0667` n `26`; metal avg `0.3809` n `20`; unknown avg `7.2987` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
