# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T01:07:27.651354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `0.0026` n `230`; crypto_major avg `0.0257` n `8`; equity avg `-0.0117` n `94`; fx avg `0.0217` n `6`; index avg `-0.0333` n `25`; metal avg `-0.1109` n `20`; unknown avg `-0.0554` n `768`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `-0.1408` n `230`; crypto_major avg `-0.2755` n `8`; equity avg `-0.0084` n `20`; fx avg `0.0` n `1`; index avg `-0.0133` n `19`; metal avg `-0.0178` n `14`; unknown avg `-0.1828` n `764`
- 4h: commodity avg `-0.037` n `12`; crypto_alt avg `-0.1159` n `230`; crypto_major avg `-0.2891` n `8`; equity avg `-0.4237` n `94`; fx avg `0.0018` n `6`; index avg `-0.1508` n `25`; metal avg `-0.1571` n `20`; unknown avg `0.1342` n `766`
- 24h: commodity avg `0.0242` n `12`; crypto_alt avg `0.1194` n `230`; crypto_major avg `0.4097` n `8`; equity avg `-1.2756` n `93`; fx avg `0.1984` n `6`; index avg `-0.3582` n `25`; metal avg `-0.073` n `20`; unknown avg `0.0628` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
