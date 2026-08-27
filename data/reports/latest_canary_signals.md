# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T07:22:25.071645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0343` n `12`; crypto_alt avg `0.0259` n `231`; crypto_major avg `0.0961` n `8`; equity avg `0.0723` n `127`; fx avg `-0.007` n `6`; index avg `0.0051` n `26`; metal avg `-0.0403` n `20`; unknown avg `0.0179` n `791`
- 1h: commodity avg `-0.1442` n `12`; crypto_alt avg `0.3528` n `231`; crypto_major avg `0.2189` n `8`; equity avg `0.3339` n `127`; fx avg `-0.0093` n `6`; index avg `0.0523` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.0745` n `791`
- 4h: commodity avg `-0.2176` n `12`; crypto_alt avg `-0.1072` n `231`; crypto_major avg `0.005` n `8`; equity avg `-0.0463` n `127`; fx avg `-0.0097` n `6`; index avg `-0.0402` n `26`; metal avg `-0.3115` n `20`; unknown avg `0.0092` n `775`
- 24h: commodity avg `0.2179` n `12`; crypto_alt avg `0.2144` n `231`; crypto_major avg `0.4092` n `8`; equity avg `1.5825` n `127`; fx avg `-0.0967` n `6`; index avg `0.2515` n `26`; metal avg `-0.3776` n `20`; unknown avg `0.3616` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
