# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T06:46:04.663026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `-0.047` n `234`; crypto_major avg `-0.0595` n `8`; equity avg `-0.008` n `140`; fx avg `0.0046` n `6`; index avg `-0.0053` n `26`; metal avg `0.0115` n `20`; unknown avg `0.3847` n `944`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0462` n `234`; crypto_major avg `-0.0805` n `8`; equity avg `-0.2304` n `140`; fx avg `0.0348` n `6`; index avg `-0.043` n `26`; metal avg `-0.093` n `20`; unknown avg `0.5829` n `914`
- 4h: commodity avg `0.1017` n `12`; crypto_alt avg `0.1563` n `234`; crypto_major avg `0.1635` n `8`; equity avg `-0.9444` n `140`; fx avg `-0.0002` n `6`; index avg `-0.1129` n `26`; metal avg `-0.187` n `20`; unknown avg `0.5373` n `908`
- 24h: commodity avg `-0.095` n `12`; crypto_alt avg `2.6185` n `234`; crypto_major avg `4.0452` n `8`; equity avg `1.3717` n `140`; fx avg `-0.1763` n `6`; index avg `0.3111` n `26`; metal avg `-0.1789` n `20`; unknown avg `1126.7062` n `792`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
