# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T03:37:22.760895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.0118` n `230`; crypto_major avg `-0.0603` n `8`; equity avg `-0.0353` n `96`; fx avg `-0.0009` n `6`; index avg `0.0017` n `25`; metal avg `0.002` n `20`; unknown avg `0.0379` n `769`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `-0.1492` n `230`; crypto_major avg `-0.1313` n `8`; equity avg `0.0243` n `96`; fx avg `0.0003` n `6`; index avg `0.0179` n `25`; metal avg `0.0121` n `20`; unknown avg `0.0049` n `769`
- 4h: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.1454` n `230`; crypto_major avg `-0.0925` n `8`; equity avg `0.1785` n `96`; fx avg `-0.0118` n `6`; index avg `0.0664` n `25`; metal avg `0.043` n `20`; unknown avg `-0.3702` n `769`
- 24h: commodity avg `0.7534` n `12`; crypto_alt avg `-0.6285` n `230`; crypto_major avg `-0.3868` n `8`; equity avg `0.3997` n `96`; fx avg `0.0376` n `6`; index avg `-0.0022` n `25`; metal avg `0.1016` n `20`; unknown avg `0.1821` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
