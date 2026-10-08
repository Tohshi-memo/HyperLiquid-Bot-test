# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T10:07:29.650034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `-0.0827` n `235`; crypto_major avg `-0.0177` n `8`; equity avg `-0.0493` n `150`; fx avg `0.004` n `6`; index avg `0.0043` n `26`; metal avg `0.0373` n `20`; unknown avg `-0.0834` n `1075`
- 1h: commodity avg `0.0455` n `13`; crypto_alt avg `0.36` n `235`; crypto_major avg `0.1076` n `8`; equity avg `-0.0458` n `150`; fx avg `0.0026` n `6`; index avg `-0.0062` n `26`; metal avg `-0.055` n `20`; unknown avg `-0.0988` n `1075`
- 4h: commodity avg `0.4454` n `13`; crypto_alt avg `0.8564` n `235`; crypto_major avg `0.1857` n `8`; equity avg `-0.5274` n `150`; fx avg `0.0562` n `6`; index avg `-0.1074` n `26`; metal avg `-0.0551` n `20`; unknown avg `0.7519` n `1053`
- 24h: commodity avg `0.7887` n `13`; crypto_alt avg `0.9179` n `235`; crypto_major avg `-1.0957` n `8`; equity avg `-1.391` n `150`; fx avg `0.0175` n `6`; index avg `-0.27` n `26`; metal avg `-0.063` n `20`; unknown avg `416.4414` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
