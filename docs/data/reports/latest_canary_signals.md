# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T12:22:24.401281+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `0.169` n `231`; crypto_major avg `0.1397` n `8`; equity avg `-0.0126` n `127`; fx avg `-0.0004` n `6`; index avg `0.0067` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.0011` n `791`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.1491` n `231`; crypto_major avg `0.0818` n `8`; equity avg `-0.0308` n `127`; fx avg `-0.0018` n `6`; index avg `0.0108` n `26`; metal avg `0.0092` n `20`; unknown avg `0.1455` n `777`
- 4h: commodity avg `0.0224` n `12`; crypto_alt avg `0.1` n `231`; crypto_major avg `0.1989` n `8`; equity avg `-0.0105` n `127`; fx avg `-0.0221` n `6`; index avg `0.0055` n `26`; metal avg `0.0054` n `20`; unknown avg `-0.0045` n `761`
- 24h: commodity avg `0.2034` n `12`; crypto_alt avg `-2.1633` n `231`; crypto_major avg `-2.0309` n `8`; equity avg `-1.3986` n `127`; fx avg `-0.0702` n `6`; index avg `-0.141` n `26`; metal avg `-0.7719` n `20`; unknown avg `-0.6487` n `744`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1979`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
