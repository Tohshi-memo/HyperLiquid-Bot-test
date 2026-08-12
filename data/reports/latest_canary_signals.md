# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T03:07:32.730835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.0968` n `230`; crypto_major avg `-0.0522` n `8`; equity avg `0.056` n `113`; fx avg `0.0199` n `6`; index avg `0.013` n `25`; metal avg `0.0509` n `20`; unknown avg `0.0838` n `786`
- 1h: commodity avg `0.0515` n `12`; crypto_alt avg `0.1946` n `230`; crypto_major avg `-0.2548` n `8`; equity avg `0.4002` n `113`; fx avg `0.0266` n `6`; index avg `0.0993` n `25`; metal avg `0.1784` n `20`; unknown avg `-0.2393` n `786`
- 4h: commodity avg `0.1358` n `12`; crypto_alt avg `0.556` n `230`; crypto_major avg `0.1893` n `8`; equity avg `0.6999` n `113`; fx avg `0.0617` n `6`; index avg `0.1723` n `25`; metal avg `0.2727` n `20`; unknown avg `-0.2181` n `786`
- 24h: commodity avg `0.2589` n `12`; crypto_alt avg `-0.8303` n `230`; crypto_major avg `0.6005` n `8`; equity avg `1.7658` n `113`; fx avg `0.0378` n `6`; index avg `0.1639` n `25`; metal avg `-0.0312` n `20`; unknown avg `-0.103` n `753`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2254`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2164`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2067`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
