# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T11:07:32.826117+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `-0.0225` n `230`; crypto_major avg `-0.0894` n `8`; equity avg `0.1655` n `113`; fx avg `0.0064` n `6`; index avg `0.0177` n `25`; metal avg `-0.0274` n `20`; unknown avg `2.4727` n `787`
- 1h: commodity avg `-0.0447` n `12`; crypto_alt avg `0.0356` n `230`; crypto_major avg `-0.1333` n `8`; equity avg `0.1189` n `113`; fx avg `0.0174` n `6`; index avg `0.0043` n `25`; metal avg `-0.068` n `20`; unknown avg `2.5517` n `787`
- 4h: commodity avg `-0.2153` n `12`; crypto_alt avg `-0.2086` n `230`; crypto_major avg `-0.1878` n `8`; equity avg `0.6036` n `113`; fx avg `-0.0176` n `6`; index avg `0.0805` n `25`; metal avg `0.0806` n `20`; unknown avg `1.4291` n `787`
- 24h: commodity avg `-0.0828` n `12`; crypto_alt avg `-0.722` n `230`; crypto_major avg `-0.7695` n `8`; equity avg `1.8822` n `113`; fx avg `-0.0457` n `6`; index avg `0.3546` n `25`; metal avg `-0.2625` n `20`; unknown avg `0.9627` n `755`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
