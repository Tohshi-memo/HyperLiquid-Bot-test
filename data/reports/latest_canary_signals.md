# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T03:52:33.101116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.0382` n `230`; crypto_major avg `0.0304` n `8`; equity avg `-0.0401` n `102`; fx avg `0.0216` n `6`; index avg `-0.028` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0113` n `781`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `-0.0678` n `230`; crypto_major avg `-0.1023` n `8`; equity avg `-0.0898` n `102`; fx avg `0.0235` n `6`; index avg `-0.0417` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0106` n `781`
- 4h: commodity avg `-0.1095` n `12`; crypto_alt avg `0.4799` n `230`; crypto_major avg `0.1323` n `8`; equity avg `0.0527` n `102`; fx avg `0.0316` n `6`; index avg `0.0225` n `25`; metal avg `-0.022` n `20`; unknown avg `-0.0806` n `781`
- 24h: commodity avg `0.9287` n `12`; crypto_alt avg `0.217` n `230`; crypto_major avg `-1.6026` n `8`; equity avg `-2.0941` n `102`; fx avg `-0.1088` n `6`; index avg `-0.1999` n `25`; metal avg `-0.1909` n `20`; unknown avg `4.8969` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
