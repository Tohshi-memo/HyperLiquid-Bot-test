# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T00:52:30.141977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `12`; crypto_alt avg `0.0538` n `230`; crypto_major avg `0.0888` n `8`; equity avg `-0.0373` n `113`; fx avg `-0.0045` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0295` n `20`; unknown avg `0.1212` n `786`
- 1h: commodity avg `0.1187` n `12`; crypto_alt avg `0.1685` n `230`; crypto_major avg `0.0958` n `8`; equity avg `0.1079` n `113`; fx avg `0.0078` n `6`; index avg `0.0102` n `25`; metal avg `0.0563` n `20`; unknown avg `0.0327` n `786`
- 4h: commodity avg `0.13` n `12`; crypto_alt avg `0.235` n `230`; crypto_major avg `0.4029` n `8`; equity avg `0.2989` n `113`; fx avg `0.0168` n `6`; index avg `0.0126` n `25`; metal avg `0.0617` n `20`; unknown avg `0.0454` n `785`
- 24h: commodity avg `0.2183` n `12`; crypto_alt avg `-1.195` n `230`; crypto_major avg `0.9426` n `8`; equity avg `1.3293` n `113`; fx avg `-0.0086` n `6`; index avg `0.1065` n `25`; metal avg `-0.2629` n `20`; unknown avg `-0.0492` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2255`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2193`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2034`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
