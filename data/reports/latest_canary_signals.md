# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T10:07:30.290430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.948` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.922` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7588` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.1621` n `228`; crypto_major avg `0.1432` n `8`; equity avg `0.1399` n `86`; fx avg `0.0002` n `6`; index avg `0.0009` n `23`; metal avg `0.0873` n `20`; unknown avg `0.0314` n `764`
- 1h: commodity avg `-0.0409` n `12`; crypto_alt avg `0.3174` n `228`; crypto_major avg `0.1744` n `8`; equity avg `0.3175` n `86`; fx avg `-0.0244` n `6`; index avg `0.0532` n `23`; metal avg `0.252` n `20`; unknown avg `-0.103` n `764`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `-1.7229` n `228`; crypto_major avg `-1.8279` n `8`; equity avg `0.1201` n `86`; fx avg `-0.0793` n `6`; index avg `-0.0691` n `23`; metal avg `0.0941` n `20`; unknown avg `-0.4498` n `620`
- 24h: commodity avg `-0.6783` n `12`; crypto_alt avg `-3.7547` n `228`; crypto_major avg `-4.0805` n `8`; equity avg `-4.2029` n `85`; fx avg `-0.1275` n `6`; index avg `-0.8312` n `23`; metal avg `-1.3507` n `18`; unknown avg `0.6171` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
