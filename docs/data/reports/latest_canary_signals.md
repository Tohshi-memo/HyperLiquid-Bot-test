# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T19:22:28.392804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0296` n `12`; crypto_alt avg `0.0531` n `230`; crypto_major avg `0.0174` n `8`; equity avg `-0.012` n `92`; fx avg `-0.0056` n `6`; index avg `0.0078` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0249` n `765`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.005` n `230`; crypto_major avg `0.068` n `8`; equity avg `-0.03` n `92`; fx avg `-0.0121` n `6`; index avg `-0.0088` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0509` n `765`
- 4h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.0797` n `230`; crypto_major avg `-0.051` n `8`; equity avg `0.1029` n `92`; fx avg `-0.0002` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0059` n `20`; unknown avg `0.1924` n `765`
- 24h: commodity avg `-0.0398` n `12`; crypto_alt avg `1.4399` n `229`; crypto_major avg `1.1838` n `8`; equity avg `0.2872` n `92`; fx avg `-0.0082` n `6`; index avg `0.0374` n `25`; metal avg `0.077` n `20`; unknown avg `2.3898` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
