# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T20:37:25.256235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2073` n `12`; crypto_alt avg `0.0301` n `228`; crypto_major avg `-0.0356` n `8`; equity avg `0.0412` n `88`; fx avg `-0.0298` n `6`; index avg `0.0495` n `23`; metal avg `0.0161` n `20`; unknown avg `1.923` n `764`
- 1h: commodity avg `-0.2515` n `12`; crypto_alt avg `0.143` n `228`; crypto_major avg `0.1738` n `8`; equity avg `0.1543` n `88`; fx avg `-0.0375` n `6`; index avg `0.0566` n `23`; metal avg `0.0222` n `20`; unknown avg `4.7607` n `764`
- 4h: commodity avg `-0.3045` n `12`; crypto_alt avg `-0.1113` n `228`; crypto_major avg `-0.1302` n `8`; equity avg `0.1196` n `88`; fx avg `-0.0693` n `6`; index avg `0.0351` n `23`; metal avg `0.0464` n `20`; unknown avg `5.3331` n `764`
- 24h: commodity avg `0.0515` n `12`; crypto_alt avg `-0.4079` n `228`; crypto_major avg `-0.8816` n `8`; equity avg `0.2128` n `88`; fx avg `-0.0695` n `6`; index avg `-0.0067` n `23`; metal avg `0.0217` n `20`; unknown avg `16.3887` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
