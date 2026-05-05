# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T23:15:19.369924+00:00`
- Correlation status: `ready`
- Asset price records: `401`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.267` n `7`; crypto_alt avg `0.043` n `223`; crypto_major avg `-0.0041` n `7`; equity avg `-0.0771` n `47`; fx avg `0.0133` n `4`; index avg `-0.0154` n `6`; metal avg `0.354` n `7`; unknown avg `-0.0691` n `313`
- 1h: commodity avg `-0.746` n `7`; crypto_alt avg `-0.2294` n `223`; crypto_major avg `-0.2142` n `7`; equity avg `0.4981` n `47`; fx avg `0.0166` n `4`; index avg `0.1962` n `6`; metal avg `0.8559` n `7`; unknown avg `0.163` n `313`
- 4h: commodity avg `-0.7252` n `7`; crypto_alt avg `0.6622` n `223`; crypto_major avg `0.3742` n `7`; equity avg `0.9216` n `47`; fx avg `0.1226` n `4`; index avg `0.2989` n `6`; metal avg `0.6979` n `7`; unknown avg `0.1883` n `313`
- 24h: commodity avg `-1.8726` n `7`; crypto_alt avg `2.4098` n `223`; crypto_major avg `2.5855` n `7`; equity avg `3.1706` n `47`; fx avg `0.0808` n `4`; index avg `1.8884` n `6`; metal avg `1.4869` n `7`; unknown avg `2.4516` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2007`, n `397`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1941`, n `397`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `397`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `397`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1086`, n `393`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `397`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1066`, n `397`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `397`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1008`, n `393`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `397`, weak_sample_signal
