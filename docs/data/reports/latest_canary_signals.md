# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T17:52:27.547672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0511` n `12`; crypto_alt avg `0.1533` n `228`; crypto_major avg `0.1468` n `8`; equity avg `0.0176` n `88`; fx avg `-0.0031` n `6`; index avg `0.0031` n `23`; metal avg `0.0033` n `20`; unknown avg `0.0005` n `764`
- 1h: commodity avg `-0.169` n `12`; crypto_alt avg `-0.1217` n `228`; crypto_major avg `0.0691` n `8`; equity avg `-0.0474` n `88`; fx avg `-0.0243` n `6`; index avg `0.0023` n `23`; metal avg `0.0009` n `20`; unknown avg `0.1733` n `764`
- 4h: commodity avg `-0.0191` n `12`; crypto_alt avg `-0.3042` n `228`; crypto_major avg `-0.5259` n `8`; equity avg `-0.1026` n `88`; fx avg `-0.0175` n `6`; index avg `-0.0213` n `23`; metal avg `-0.0373` n `20`; unknown avg `0.4956` n `764`
- 24h: commodity avg `0.2928` n `12`; crypto_alt avg `-0.859` n `228`; crypto_major avg `-1.5496` n `8`; equity avg `0.0713` n `88`; fx avg `-0.0254` n `6`; index avg `-0.0423` n `23`; metal avg `-0.0395` n `20`; unknown avg `14.7331` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
