# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T06:37:32.286754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.389` n `234`; crypto_major avg `0.3545` n `8`; equity avg `0.0966` n `140`; fx avg `0.0262` n `6`; index avg `0.0058` n `26`; metal avg `0.0171` n `20`; unknown avg `0.4367` n `944`
- 1h: commodity avg `0.039` n `12`; crypto_alt avg `0.732` n `234`; crypto_major avg `0.5355` n `8`; equity avg `0.0392` n `140`; fx avg `0.0241` n `6`; index avg `-0.003` n `26`; metal avg `-0.0008` n `20`; unknown avg `8.8149` n `914`
- 4h: commodity avg `0.1442` n `12`; crypto_alt avg `-0.3216` n `234`; crypto_major avg `-0.1379` n `8`; equity avg `-0.8992` n `140`; fx avg `0.0011` n `6`; index avg `-0.1044` n `26`; metal avg `-0.2522` n `20`; unknown avg `0.2058` n `908`
- 24h: commodity avg `-0.0401` n `12`; crypto_alt avg `2.6784` n `234`; crypto_major avg `4.0705` n `8`; equity avg `1.4126` n `140`; fx avg `-0.1839` n `6`; index avg `0.3204` n `26`; metal avg `-0.1571` n `20`; unknown avg `406.5931` n `778`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
