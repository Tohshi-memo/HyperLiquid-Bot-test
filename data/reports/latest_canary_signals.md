# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T04:52:21.018022+00:00`
- Correlation status: `ready`
- Asset price records: `615`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.175` n `12`; crypto_alt avg `0.0329` n `228`; crypto_major avg `0.0827` n `8`; equity avg `0.0839` n `65`; fx avg `0.0097` n `5`; index avg `0.024` n `23`; metal avg `0.1482` n `18`; unknown avg `-0.0922` n `365`
- 1h: commodity avg `0.0969` n `12`; crypto_alt avg `-0.0607` n `228`; crypto_major avg `-0.0909` n `8`; equity avg `0.2157` n `65`; fx avg `0.0445` n `5`; index avg `0.0151` n `23`; metal avg `-0.086` n `18`; unknown avg `-0.3255` n `365`
- 4h: commodity avg `-0.4557` n `12`; crypto_alt avg `0.3327` n `228`; crypto_major avg `-0.2196` n `8`; equity avg `0.3394` n `65`; fx avg `0.0699` n `5`; index avg `0.157` n `23`; metal avg `0.6487` n `18`; unknown avg `-0.3436` n `365`
- 24h: commodity avg `0.4684` n `12`; crypto_alt avg `1.796` n `228`; crypto_major avg `-1.3943` n `8`; equity avg `-0.8613` n `65`; fx avg `0.2365` n `5`; index avg `-0.5976` n `23`; metal avg `0.443` n `18`; unknown avg `-0.1354` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.132`, n `611`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1197`, n `607`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `607`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `611`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `611`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `611`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `607`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `607`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0788`, n `607`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `611`, weak_sample_signal
