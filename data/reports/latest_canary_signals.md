# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T13:22:32.137818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.062` n `12`; crypto_alt avg `-0.3482` n `234`; crypto_major avg `-0.0238` n `8`; equity avg `-0.0082` n `140`; fx avg `0.0038` n `6`; index avg `-0.0056` n `26`; metal avg `0.0309` n `20`; unknown avg `14.4869` n `944`
- 1h: commodity avg `-0.1161` n `12`; crypto_alt avg `0.1304` n `234`; crypto_major avg `0.2744` n `8`; equity avg `0.0158` n `140`; fx avg `-0.0072` n `6`; index avg `-0.0172` n `26`; metal avg `0.123` n `20`; unknown avg `17.8365` n `942`
- 4h: commodity avg `-0.324` n `12`; crypto_alt avg `0.8655` n `234`; crypto_major avg `1.1063` n `8`; equity avg `0.1057` n `140`; fx avg `0.019` n `6`; index avg `0.0183` n `26`; metal avg `0.2203` n `20`; unknown avg `0.7017` n `910`
- 24h: commodity avg `-0.9244` n `12`; crypto_alt avg `7.3018` n `234`; crypto_major avg `6.2881` n `8`; equity avg `2.0667` n `140`; fx avg `-0.0576` n `6`; index avg `0.3559` n `26`; metal avg `0.2927` n `20`; unknown avg `3.9888` n `733`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
