# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T07:52:31.813192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0169` n `230`; crypto_major avg `0.0692` n `8`; equity avg `0.0808` n `102`; fx avg `0.0217` n `6`; index avg `0.0194` n `25`; metal avg `-0.0248` n `20`; unknown avg `-0.0086` n `781`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `-0.2433` n `230`; crypto_major avg `-0.1195` n `8`; equity avg `0.0242` n `102`; fx avg `0.0201` n `6`; index avg `0.0054` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0563` n `781`
- 4h: commodity avg `-0.0965` n `12`; crypto_alt avg `-0.1536` n `230`; crypto_major avg `-0.0999` n `8`; equity avg `0.0886` n `102`; fx avg `0.0209` n `6`; index avg `0.0371` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0543` n `765`
- 24h: commodity avg `0.882` n `12`; crypto_alt avg `-0.1471` n `230`; crypto_major avg `-1.3527` n `8`; equity avg `-2.3698` n `102`; fx avg `-0.0136` n `6`; index avg `-0.2818` n `25`; metal avg `-0.1742` n `20`; unknown avg `4.741` n `763`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
