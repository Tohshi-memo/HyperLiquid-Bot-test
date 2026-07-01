# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T08:07:32.097757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `0.0286` n `228`; crypto_major avg `-0.0345` n `8`; equity avg `0.0224` n `88`; fx avg `-0.0019` n `6`; index avg `0.0047` n `23`; metal avg `-0.0332` n `20`; unknown avg `0.0381` n `765`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.2771` n `228`; crypto_major avg `0.2472` n `8`; equity avg `0.1066` n `88`; fx avg `0.0095` n `6`; index avg `0.0173` n `23`; metal avg `0.1148` n `20`; unknown avg `0.0402` n `765`
- 4h: commodity avg `-0.1649` n `12`; crypto_alt avg `-0.8186` n `228`; crypto_major avg `-0.9215` n `8`; equity avg `-0.3061` n `88`; fx avg `-0.0083` n `6`; index avg `-0.059` n `23`; metal avg `-0.12` n `20`; unknown avg `0.3554` n `743`
- 24h: commodity avg `-0.1194` n `12`; crypto_alt avg `-0.858` n `228`; crypto_major avg `-0.7522` n `8`; equity avg `0.3121` n `88`; fx avg `0.0787` n `6`; index avg `-0.0394` n `23`; metal avg `-0.8667` n `20`; unknown avg `-0.3322` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
