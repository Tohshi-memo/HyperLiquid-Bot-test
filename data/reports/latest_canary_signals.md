# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T09:07:31.285053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2249` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0917` n `12`; crypto_alt avg `-0.0273` n `231`; crypto_major avg `-0.0175` n `8`; equity avg `-0.1397` n `127`; fx avg `-0.0005` n `6`; index avg `-0.0285` n `26`; metal avg `-0.0429` n `20`; unknown avg `0.002` n `792`
- 1h: commodity avg `0.1343` n `12`; crypto_alt avg `0.6888` n `231`; crypto_major avg `0.6441` n `8`; equity avg `0.1054` n `127`; fx avg `-0.0042` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0965` n `20`; unknown avg `-0.0342` n `792`
- 4h: commodity avg `-0.0172` n `12`; crypto_alt avg `1.8425` n `231`; crypto_major avg `1.9745` n `8`; equity avg `0.7077` n `127`; fx avg `-0.0214` n `6`; index avg `0.0539` n `26`; metal avg `-0.2504` n `20`; unknown avg `0.2656` n `775`
- 24h: commodity avg `0.5199` n `12`; crypto_alt avg `1.7762` n `231`; crypto_major avg `2.2129` n `8`; equity avg `2.0572` n `127`; fx avg `-0.097` n `6`; index avg `0.2991` n `26`; metal avg `-0.3971` n `20`; unknown avg `0.4216` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
