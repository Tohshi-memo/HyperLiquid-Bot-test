# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T06:07:29.466186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.2948` n `228`; crypto_major avg `-0.138` n `8`; equity avg `-0.1512` n `86`; fx avg `0.0116` n `6`; index avg `-0.036` n `23`; metal avg `-0.0366` n `20`; unknown avg `-0.0809` n `749`
- 1h: commodity avg `0.1743` n `12`; crypto_alt avg `-0.0797` n `228`; crypto_major avg `-0.0932` n `8`; equity avg `0.0631` n `86`; fx avg `-0.0124` n `6`; index avg `0.029` n `23`; metal avg `0.0745` n `20`; unknown avg `125.9103` n `749`
- 4h: commodity avg `0.0335` n `12`; crypto_alt avg `-0.1514` n `228`; crypto_major avg `0.1311` n `8`; equity avg `-0.8899` n `86`; fx avg `-0.0253` n `6`; index avg `-0.2065` n `23`; metal avg `-0.1117` n `20`; unknown avg `0.828` n `733`
- 24h: commodity avg `0.4703` n `12`; crypto_alt avg `-2.9989` n `228`; crypto_major avg `-2.8997` n `8`; equity avg `-4.296` n `86`; fx avg `0.0614` n `6`; index avg `-0.6972` n `23`; metal avg `0.0906` n `20`; unknown avg `0.576` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
