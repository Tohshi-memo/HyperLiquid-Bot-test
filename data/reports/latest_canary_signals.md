# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T01:24:40.379951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0683` n `12`; crypto_alt avg `-0.1714` n `230`; crypto_major avg `-0.1925` n `8`; equity avg `-0.0179` n `98`; fx avg `-0.0056` n `6`; index avg `-0.0171` n `25`; metal avg `0.1023` n `20`; unknown avg `0.1981` n `773`
- 1h: commodity avg `0.0916` n `12`; crypto_alt avg `-0.1924` n `230`; crypto_major avg `-0.3579` n `8`; equity avg `0.1269` n `98`; fx avg `-0.0552` n `6`; index avg `0.0322` n `25`; metal avg `0.1294` n `20`; unknown avg `0.2906` n `773`
- 4h: commodity avg `0.2841` n `12`; crypto_alt avg `-0.199` n `230`; crypto_major avg `0.0902` n `8`; equity avg `0.2076` n `98`; fx avg `-0.0658` n `6`; index avg `0.098` n `25`; metal avg `0.0994` n `20`; unknown avg `-0.0201` n `773`
- 24h: commodity avg `0.7117` n `11`; crypto_alt avg `-0.5544` n `230`; crypto_major avg `-0.6887` n `8`; equity avg `-0.9221` n `87`; fx avg `-0.1283` n `5`; index avg `-0.0883` n `19`; metal avg `0.0312` n `16`; unknown avg `1.8112` n `722`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0741`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0691`, n `666`, weak_sample_signal
