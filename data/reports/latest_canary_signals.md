# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T10:46:12.057029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `0.0662` n `230`; crypto_major avg `0.1104` n `8`; equity avg `0.0207` n `114`; fx avg `-0.0075` n `6`; index avg `0.0026` n `25`; metal avg `0.0073` n `20`; unknown avg `1.0776` n `792`
- 1h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.3189` n `230`; crypto_major avg `0.4406` n `8`; equity avg `0.1333` n `114`; fx avg `-0.0124` n `6`; index avg `0.0216` n `25`; metal avg `0.065` n `20`; unknown avg `1.9817` n `792`
- 4h: commodity avg `0.2081` n `12`; crypto_alt avg `-0.2524` n `230`; crypto_major avg `-0.0086` n `8`; equity avg `0.1296` n `114`; fx avg `0.0038` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0671` n `20`; unknown avg `-0.0439` n `792`
- 24h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.0038` n `230`; crypto_major avg `1.0108` n `8`; equity avg `1.3029` n `114`; fx avg `-0.0188` n `6`; index avg `0.1546` n `25`; metal avg `0.1989` n `20`; unknown avg `-0.0141` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
