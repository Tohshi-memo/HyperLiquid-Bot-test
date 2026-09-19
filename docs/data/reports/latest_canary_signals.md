# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T04:37:28.784561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `-0.533` n `234`; crypto_major avg `-0.5441` n `8`; equity avg `-0.0602` n `140`; fx avg `-0.0006` n `6`; index avg `0.0206` n `26`; metal avg `0.0031` n `20`; unknown avg `0.1468` n `942`
- 1h: commodity avg `-0.043` n `12`; crypto_alt avg `-0.5538` n `234`; crypto_major avg `-0.4065` n `8`; equity avg `-0.0377` n `140`; fx avg `-0.0077` n `6`; index avg `-0.007` n `26`; metal avg `0.0066` n `20`; unknown avg `-0.3412` n `914`
- 4h: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.4591` n `234`; crypto_major avg `-0.4321` n `8`; equity avg `-0.1866` n `140`; fx avg `-0.0127` n `6`; index avg `-0.0166` n `26`; metal avg `-0.02` n `20`; unknown avg `0.2354` n `914`
- 24h: commodity avg `0.0972` n `12`; crypto_alt avg `4.0214` n `234`; crypto_major avg `4.5856` n `8`; equity avg `0.6672` n `140`; fx avg `0.0108` n `6`; index avg `0.0364` n `26`; metal avg `0.1057` n `20`; unknown avg `2.2991` n `767`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
