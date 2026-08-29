# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T10:37:26.800150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0644` n `231`; crypto_major avg `-0.0438` n `8`; equity avg `-0.0038` n `127`; fx avg `-0.0015` n `6`; index avg `-0.001` n `26`; metal avg `-0.0166` n `20`; unknown avg `-0.0059` n `793`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `-0.0273` n `231`; crypto_major avg `0.0237` n `8`; equity avg `0.0244` n `127`; fx avg `-0.0131` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.0075` n `793`
- 4h: commodity avg `0.0577` n `12`; crypto_alt avg `-0.2229` n `231`; crypto_major avg `0.1138` n `8`; equity avg `0.0534` n `127`; fx avg `-0.0133` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0043` n `20`; unknown avg `0.0046` n `791`
- 24h: commodity avg `-0.0895` n `12`; crypto_alt avg `-2.0724` n `231`; crypto_major avg `-1.974` n `8`; equity avg `-1.3577` n `127`; fx avg `-0.0657` n `6`; index avg `-0.1374` n `26`; metal avg `-0.7252` n `20`; unknown avg `-0.402` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
