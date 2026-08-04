# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T07:37:29.052792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.3059` n `230`; crypto_major avg `0.2773` n `8`; equity avg `0.0275` n `107`; fx avg `0.0091` n `6`; index avg `0.0053` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0686` n `781`
- 1h: commodity avg `-0.0467` n `12`; crypto_alt avg `-0.06` n `230`; crypto_major avg `0.101` n `8`; equity avg `0.2676` n `107`; fx avg `0.0104` n `6`; index avg `0.0367` n `25`; metal avg `0.1286` n `20`; unknown avg `0.4161` n `781`
- 4h: commodity avg `0.001` n `12`; crypto_alt avg `-0.1782` n `230`; crypto_major avg `-0.0318` n `8`; equity avg `0.8778` n `107`; fx avg `0.0453` n `6`; index avg `0.1421` n `25`; metal avg `0.1352` n `20`; unknown avg `0.4135` n `765`
- 24h: commodity avg `0.2041` n `12`; crypto_alt avg `1.1973` n `230`; crypto_major avg `1.446` n `8`; equity avg `2.833` n `107`; fx avg `0.0854` n `6`; index avg `0.2829` n `25`; metal avg `0.1788` n `20`; unknown avg `0.646` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
