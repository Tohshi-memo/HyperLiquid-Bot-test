# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T14:37:28.926234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `0.005` n `230`; crypto_major avg `0.0033` n `8`; equity avg `-0.018` n `102`; fx avg `0.0021` n `6`; index avg `0.0213` n `25`; metal avg `-0.0073` n `20`; unknown avg `0.0004` n `782`
- 1h: commodity avg `-0.0697` n `12`; crypto_alt avg `0.0429` n `230`; crypto_major avg `0.0087` n `8`; equity avg `-0.0161` n `102`; fx avg `-0.008` n `6`; index avg `0.0278` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0314` n `782`
- 4h: commodity avg `0.0104` n `12`; crypto_alt avg `0.2389` n `230`; crypto_major avg `0.1834` n `8`; equity avg `-0.0676` n `102`; fx avg `-0.061` n `6`; index avg `-0.0103` n `25`; metal avg `-0.013` n `20`; unknown avg `-0.0952` n `781`
- 24h: commodity avg `0.4162` n `12`; crypto_alt avg `0.4309` n `230`; crypto_major avg `-0.5575` n `8`; equity avg `-0.6111` n `102`; fx avg `-0.0303` n `6`; index avg `0.0591` n `25`; metal avg `0.1188` n `20`; unknown avg `4.2645` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
