# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T09:00:51.208059+00:00`
- Correlation status: `ready`
- Asset price records: `440`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9213` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-1.0913` n `7`; crypto_alt avg `0.1996` n `223`; crypto_major avg `0.2312` n `7`; equity avg `0.4467` n `47`; fx avg `-0.0116` n `4`; index avg `0.8545` n `6`; metal avg `0.8044` n `7`; unknown avg `0.1102` n `313`
- 1h: commodity avg `-0.9551` n `7`; crypto_alt avg `0.9277` n `223`; crypto_major avg `0.7898` n `7`; equity avg `0.7287` n `47`; fx avg `-0.0033` n `4`; index avg `0.9338` n `6`; metal avg `0.6313` n `7`; unknown avg `0.2056` n `313`
- 4h: commodity avg `-1.5429` n `7`; crypto_alt avg `1.8555` n `223`; crypto_major avg `1.3784` n `7`; equity avg `0.9627` n `47`; fx avg `-0.0634` n `4`; index avg `0.7857` n `6`; metal avg `1.0853` n `7`; unknown avg `1.2212` n `311`
- 24h: commodity avg `-2.7752` n `7`; crypto_alt avg `3.8629` n `223`; crypto_major avg `2.8565` n `7`; equity avg `3.3993` n `47`; fx avg `-0.5172` n `4`; index avg `2.9245` n `6`; metal avg `2.7288` n `7`; unknown avg `2.2076` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1763`, n `436`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1701`, n `436`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1366`, n `436`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1231`, n `436`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `436`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `436`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0962`, n `432`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `436`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0903`, n `432`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `432`, weak_sample_signal
