# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T04:07:28.801072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.7232` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.1974` n `228`; crypto_major avg `0.162` n `8`; equity avg `0.2908` n `86`; fx avg `-0.0002` n `6`; index avg `0.079` n `23`; metal avg `0.0258` n `20`; unknown avg `1.5264` n `765`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `1.8179` n `228`; crypto_major avg `1.8666` n `8`; equity avg `0.4522` n `86`; fx avg `0.0149` n `6`; index avg `0.0643` n `23`; metal avg `0.1434` n `20`; unknown avg `1.9536` n `749`
- 4h: commodity avg `-0.1562` n `12`; crypto_alt avg `-0.4574` n `228`; crypto_major avg `-0.3704` n `8`; equity avg `-1.8395` n `86`; fx avg `0.0314` n `6`; index avg `-0.44` n `23`; metal avg `-0.3485` n `20`; unknown avg `-0.2903` n `749`
- 24h: commodity avg `0.3017` n `12`; crypto_alt avg `-1.3802` n `228`; crypto_major avg `-1.2339` n `8`; equity avg `-3.8259` n `86`; fx avg `0.0162` n `6`; index avg `-0.6239` n `23`; metal avg `-0.1431` n `20`; unknown avg `0.6413` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
