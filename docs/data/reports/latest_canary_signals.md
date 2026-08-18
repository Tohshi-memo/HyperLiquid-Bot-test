# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T14:07:37.269233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0399` n `12`; crypto_alt avg `0.1512` n `230`; crypto_major avg `0.2029` n `8`; equity avg `0.0686` n `114`; fx avg `-0.0011` n `6`; index avg `0.0189` n `25`; metal avg `0.0298` n `20`; unknown avg `0.0958` n `795`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.0343` n `230`; crypto_major avg `0.1604` n `8`; equity avg `-0.3936` n `114`; fx avg `0.0226` n `6`; index avg `-0.0402` n `25`; metal avg `-0.0533` n `20`; unknown avg `-0.0681` n `795`
- 4h: commodity avg `0.1016` n `12`; crypto_alt avg `0.1374` n `230`; crypto_major avg `0.1414` n `8`; equity avg `-0.46` n `114`; fx avg `0.0252` n `6`; index avg `-0.034` n `25`; metal avg `-0.092` n `20`; unknown avg `0.0457` n `795`
- 24h: commodity avg `0.5691` n `12`; crypto_alt avg `-0.6321` n `230`; crypto_major avg `0.201` n `8`; equity avg `-2.9683` n `114`; fx avg `-0.0382` n `6`; index avg `-0.5703` n `25`; metal avg `-0.3153` n `20`; unknown avg `-0.1208` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
