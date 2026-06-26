# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T00:22:28.547026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0488` n `12`; crypto_alt avg `0.1271` n `228`; crypto_major avg `0.0218` n `8`; equity avg `-0.2319` n `86`; fx avg `0.0375` n `6`; index avg `-0.0765` n `23`; metal avg `0.0451` n `20`; unknown avg `0.298` n `765`
- 1h: commodity avg `0.0322` n `12`; crypto_alt avg `0.15` n `228`; crypto_major avg `-0.1506` n `8`; equity avg `-0.5169` n `86`; fx avg `0.0444` n `6`; index avg `-0.1281` n `23`; metal avg `-0.1469` n `20`; unknown avg `1.4082` n `749`
- 4h: commodity avg `-0.0524` n `12`; crypto_alt avg `0.7996` n `228`; crypto_major avg `0.7045` n `8`; equity avg `-0.6085` n `86`; fx avg `0.0174` n `6`; index avg `-0.1405` n `23`; metal avg `-0.1646` n `20`; unknown avg `1.5155` n `749`
- 24h: commodity avg `0.3624` n `12`; crypto_alt avg `-1.1072` n `228`; crypto_major avg `-1.1525` n `8`; equity avg `-2.6843` n `86`; fx avg `0.0617` n `6`; index avg `-0.1974` n `23`; metal avg `0.1818` n `20`; unknown avg `1.6584` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
