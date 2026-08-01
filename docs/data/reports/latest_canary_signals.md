# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T05:07:32.308017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0434` n `12`; crypto_alt avg `0.0414` n `230`; crypto_major avg `-0.0024` n `8`; equity avg `0.0133` n `102`; fx avg `0.0009` n `6`; index avg `-0.0073` n `25`; metal avg `0.0159` n `20`; unknown avg `0.0372` n `781`
- 1h: commodity avg `-0.0468` n `12`; crypto_alt avg `0.0732` n `230`; crypto_major avg `0.1013` n `8`; equity avg `0.0558` n `102`; fx avg `-0.0046` n `6`; index avg `0.0285` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.0095` n `781`
- 4h: commodity avg `-0.1143` n `12`; crypto_alt avg `0.1772` n `230`; crypto_major avg `0.0938` n `8`; equity avg `0.0092` n `102`; fx avg `0.0187` n `6`; index avg `0.0475` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.2981` n `781`
- 24h: commodity avg `0.9416` n `12`; crypto_alt avg `0.4411` n `230`; crypto_major avg `-1.5115` n `8`; equity avg `-2.7319` n `102`; fx avg `-0.1103` n `6`; index avg `-0.2903` n `25`; metal avg `-0.2946` n `20`; unknown avg `4.8058` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
