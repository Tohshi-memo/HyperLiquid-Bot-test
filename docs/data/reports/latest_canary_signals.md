# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T15:52:40.166777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.0365` n `230`; crypto_major avg `0.0717` n `8`; equity avg `0.1629` n `113`; fx avg `0.0074` n `6`; index avg `0.0295` n `25`; metal avg `0.0425` n `20`; unknown avg `0.0097` n `785`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `-0.279` n `230`; crypto_major avg `-0.3831` n `8`; equity avg `0.003` n `113`; fx avg `0.0006` n `6`; index avg `-0.0184` n `25`; metal avg `0.0738` n `20`; unknown avg `1.718` n `784`
- 4h: commodity avg `0.4335` n `12`; crypto_alt avg `-0.671` n `230`; crypto_major avg `-0.9311` n `8`; equity avg `-0.5427` n `113`; fx avg `0.0425` n `6`; index avg `-0.0117` n `25`; metal avg `0.1674` n `20`; unknown avg `1.632` n `784`
- 24h: commodity avg `1.1095` n `12`; crypto_alt avg `-0.4772` n `230`; crypto_major avg `-1.3636` n `8`; equity avg `-1.0275` n `113`; fx avg `0.253` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0313` n `20`; unknown avg `103.5877` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
