# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T03:45:19.663436+00:00`
- Correlation status: `ready`
- Asset price records: `419`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1259` n `7`; crypto_alt avg `0.0087` n `223`; crypto_major avg `-0.0241` n `7`; equity avg `0.1152` n `47`; fx avg `-0.0161` n `4`; index avg `0.1378` n `6`; metal avg `0.0119` n `7`; unknown avg `0.1066` n `313`
- 1h: commodity avg `-0.0606` n `7`; crypto_alt avg `0.4388` n `223`; crypto_major avg `0.5191` n `7`; equity avg `0.4164` n `47`; fx avg `0.0019` n `4`; index avg `0.1766` n `6`; metal avg `0.3563` n `7`; unknown avg `0.0303` n `313`
- 4h: commodity avg `0.109` n `7`; crypto_alt avg `1.3887` n `223`; crypto_major avg `0.7573` n `7`; equity avg `0.5889` n `47`; fx avg `-0.2732` n `4`; index avg `0.5539` n `6`; metal avg `1.1967` n `7`; unknown avg `0.4229` n `313`
- 24h: commodity avg `-1.5583` n `7`; crypto_alt avg `2.5766` n `223`; crypto_major avg `1.8085` n `7`; equity avg `2.9839` n `47`; fx avg `-0.1683` n `4`; index avg `2.2781` n `6`; metal avg `2.2205` n `7`; unknown avg `1.4105` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1814`, n `415`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1751`, n `415`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `415`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `415`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `415`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `415`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `411`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `415`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `415`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0942`, n `411`, weak_sample_signal
