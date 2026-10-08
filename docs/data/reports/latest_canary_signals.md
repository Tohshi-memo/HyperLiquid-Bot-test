# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T00:07:29.288861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `13`; crypto_alt avg `-0.063` n `235`; crypto_major avg `-0.0176` n `8`; equity avg `0.0063` n `150`; fx avg `-0.0451` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.0301` n `1069`
- 1h: commodity avg `0.0316` n `13`; crypto_alt avg `0.2604` n `235`; crypto_major avg `0.2032` n `8`; equity avg `0.0296` n `150`; fx avg `-0.0366` n `6`; index avg `-0.0119` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.1515` n `1069`
- 4h: commodity avg `0.1892` n `13`; crypto_alt avg `0.8127` n `235`; crypto_major avg `0.1679` n `8`; equity avg `0.2259` n `150`; fx avg `-0.0211` n `6`; index avg `0.017` n `26`; metal avg `0.0262` n `20`; unknown avg `-0.1423` n `1019`
- 24h: commodity avg `0.3974` n `13`; crypto_alt avg `-3.4222` n `235`; crypto_major avg `-3.1596` n `8`; equity avg `-1.2568` n `150`; fx avg `-0.1984` n `6`; index avg `-0.2024` n `26`; metal avg `-0.694` n `20`; unknown avg `247.876` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
