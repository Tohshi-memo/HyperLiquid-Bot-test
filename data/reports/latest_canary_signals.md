# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T10:22:32.355828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `13`; crypto_alt avg `-0.1077` n `235`; crypto_major avg `-0.1194` n `8`; equity avg `-0.0442` n `150`; fx avg `-0.0112` n `6`; index avg `-0.0116` n `26`; metal avg `-0.0079` n `20`; unknown avg `3.93` n `1078`
- 1h: commodity avg `-0.0274` n `13`; crypto_alt avg `-0.1625` n `235`; crypto_major avg `-0.0649` n `8`; equity avg `0.0169` n `150`; fx avg `-0.0103` n `6`; index avg `-0.0151` n `26`; metal avg `-0.028` n `20`; unknown avg `1.8775` n `1076`
- 4h: commodity avg `-0.1107` n `13`; crypto_alt avg `-0.0488` n `235`; crypto_major avg `-0.0033` n `8`; equity avg `0.1326` n `150`; fx avg `-0.0281` n `6`; index avg `0.0292` n `26`; metal avg `0.0028` n `20`; unknown avg `2.3789` n `1006`
- 24h: commodity avg `-0.5285` n `13`; crypto_alt avg `-1.7995` n `235`; crypto_major avg `-2.0807` n `8`; equity avg `-0.384` n `150`; fx avg `0.0748` n `6`; index avg `0.0709` n `26`; metal avg `0.4618` n `20`; unknown avg `7.3145` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
