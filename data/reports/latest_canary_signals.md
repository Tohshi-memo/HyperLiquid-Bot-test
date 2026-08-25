# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T18:37:30.568879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0481` n `12`; crypto_alt avg `-0.132` n `231`; crypto_major avg `-0.2362` n `8`; equity avg `0.0802` n `122`; fx avg `0.0016` n `6`; index avg `0.0192` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0745` n `795`
- 1h: commodity avg `0.0172` n `12`; crypto_alt avg `0.2548` n `231`; crypto_major avg `0.1891` n `8`; equity avg `0.15` n `122`; fx avg `0.0033` n `6`; index avg `0.0195` n `25`; metal avg `0.0129` n `20`; unknown avg `0.0158` n `795`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `-0.2057` n `231`; crypto_major avg `0.0701` n `8`; equity avg `0.1604` n `122`; fx avg `-0.0008` n `6`; index avg `0.0273` n `25`; metal avg `0.1168` n `20`; unknown avg `-0.0761` n `795`
- 24h: commodity avg `-0.5746` n `12`; crypto_alt avg `-0.3446` n `231`; crypto_major avg `1.0263` n `8`; equity avg `1.5214` n `122`; fx avg `0.0553` n `6`; index avg `0.134` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.6045` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
