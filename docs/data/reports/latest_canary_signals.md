# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:07:30.198286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0312` n `12`; crypto_alt avg `-0.1258` n `230`; crypto_major avg `-0.1305` n `8`; equity avg `-0.1049` n `114`; fx avg `0.0047` n `6`; index avg `-0.0232` n `25`; metal avg `-0.0316` n `20`; unknown avg `0.0522` n `792`
- 1h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0127` n `230`; crypto_major avg `-0.0572` n `8`; equity avg `-0.0721` n `114`; fx avg `-0.0055` n `6`; index avg `-0.0375` n `25`; metal avg `-0.0948` n `20`; unknown avg `-0.0826` n `792`
- 4h: commodity avg `0.4424` n `12`; crypto_alt avg `-0.1117` n `230`; crypto_major avg `-0.067` n `8`; equity avg `-0.3082` n `114`; fx avg `0.0257` n `6`; index avg `-0.1463` n `25`; metal avg `-0.1628` n `20`; unknown avg `0.0557` n `792`
- 24h: commodity avg `0.3149` n `12`; crypto_alt avg `-0.0669` n `230`; crypto_major avg `0.8177` n `8`; equity avg `1.2606` n `114`; fx avg `0.0169` n `6`; index avg `0.0798` n `25`; metal avg `0.125` n `20`; unknown avg `0.1864` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
