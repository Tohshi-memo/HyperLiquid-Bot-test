# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T01:07:30.606636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-0.166` n `235`; crypto_major avg `-0.0437` n `8`; equity avg `0.0044` n `150`; fx avg `-0.0013` n `6`; index avg `0.0012` n `26`; metal avg `0.0022` n `20`; unknown avg `0.061` n `1114`
- 1h: commodity avg `0.0136` n `13`; crypto_alt avg `0.1984` n `235`; crypto_major avg `0.2109` n `8`; equity avg `0.0824` n `150`; fx avg `0.0019` n `6`; index avg `0.0225` n `26`; metal avg `0.0232` n `20`; unknown avg `0.1118` n `1114`
- 4h: commodity avg `-0.1396` n `13`; crypto_alt avg `1.179` n `235`; crypto_major avg `0.3083` n `8`; equity avg `0.049` n `150`; fx avg `0.0062` n `6`; index avg `0.0207` n `26`; metal avg `0.0124` n `20`; unknown avg `0.1452` n `1100`
- 24h: commodity avg `-0.1485` n `13`; crypto_alt avg `2.9466` n `235`; crypto_major avg `0.7615` n `8`; equity avg `0.9071` n `150`; fx avg `-0.031` n `6`; index avg `0.1469` n `26`; metal avg `0.3922` n `20`; unknown avg `13.241` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
