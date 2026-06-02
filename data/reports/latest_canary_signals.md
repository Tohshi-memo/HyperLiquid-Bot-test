# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T19:07:28.561132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.09` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2025` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0952` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0592` n `12`; crypto_alt avg `-0.0757` n `228`; crypto_major avg `0.051` n `8`; equity avg `-0.0551` n `69`; fx avg `0.0105` n `6`; index avg `0.0777` n `23`; metal avg `0.0404` n `18`; unknown avg `0.1988` n `422`
- 1h: commodity avg `0.1005` n `12`; crypto_alt avg `-1.3897` n `228`; crypto_major avg `-0.9368` n `8`; equity avg `-0.0504` n `69`; fx avg `0.0066` n `6`; index avg `0.1584` n `23`; metal avg `0.0547` n `18`; unknown avg `-0.1174` n `422`
- 4h: commodity avg `0.667` n `12`; crypto_alt avg `-0.9128` n `228`; crypto_major avg `-1.0855` n `8`; equity avg `0.1916` n `69`; fx avg `-0.0176` n `6`; index avg `0.117` n `23`; metal avg `-0.3692` n `18`; unknown avg `-0.0442` n `422`
- 24h: commodity avg `-0.0296` n `12`; crypto_alt avg `-3.91` n `228`; crypto_major avg `-4.3897` n `8`; equity avg `0.1182` n `69`; fx avg `0.0802` n `6`; index avg `0.2487` n `23`; metal avg `0.2454` n `18`; unknown avg `-0.3698` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
