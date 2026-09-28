# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T03:07:25.184556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.1161` n `234`; crypto_major avg `0.102` n `8`; equity avg `0.0327` n `141`; fx avg `-0.0006` n `6`; index avg `0.0056` n `26`; metal avg `0.041` n `20`; unknown avg `0.3036` n `960`
- 1h: commodity avg `-0.135` n `12`; crypto_alt avg `-0.3873` n `234`; crypto_major avg `-0.0148` n `8`; equity avg `-0.142` n `141`; fx avg `-0.0519` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0689` n `20`; unknown avg `316.7644` n `958`
- 4h: commodity avg `-0.0369` n `12`; crypto_alt avg `-1.1195` n `234`; crypto_major avg `-0.7396` n `8`; equity avg `-1.2179` n `141`; fx avg `0.0789` n `6`; index avg `-0.075` n `26`; metal avg `-0.4887` n `20`; unknown avg `129.3745` n `942`
- 24h: commodity avg `-0.4761` n `12`; crypto_alt avg `-0.7638` n `234`; crypto_major avg `-1.2848` n `8`; equity avg `-1.3401` n `141`; fx avg `0.059` n `6`; index avg `-0.136` n `26`; metal avg `-0.6776` n `20`; unknown avg `12.1519` n `817`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
