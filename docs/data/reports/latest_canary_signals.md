# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T05:22:31.466086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0252` n `12`; crypto_alt avg `-0.1665` n `230`; crypto_major avg `-0.1675` n `8`; equity avg `-0.1154` n `113`; fx avg `0.0054` n `6`; index avg `-0.0276` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.1694` n `785`
- 1h: commodity avg `0.1027` n `12`; crypto_alt avg `-0.2606` n `230`; crypto_major avg `-0.2824` n `8`; equity avg `-0.1389` n `113`; fx avg `0.0126` n `6`; index avg `-0.0241` n `25`; metal avg `-0.1107` n `20`; unknown avg `-0.164` n `785`
- 4h: commodity avg `0.061` n `12`; crypto_alt avg `-0.2918` n `230`; crypto_major avg `-0.0261` n `8`; equity avg `0.013` n `113`; fx avg `0.0073` n `6`; index avg `0.039` n `25`; metal avg `-0.2176` n `20`; unknown avg `-0.3037` n `785`
- 24h: commodity avg `0.9281` n `12`; crypto_alt avg `-0.724` n `230`; crypto_major avg `-0.6688` n `8`; equity avg `-0.9521` n `113`; fx avg `0.0813` n `6`; index avg `0.0237` n `25`; metal avg `0.3623` n `20`; unknown avg `103.9291` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
