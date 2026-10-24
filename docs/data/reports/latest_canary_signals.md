# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T21:52:28.698488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.0954` n `237`; crypto_major avg `-0.0742` n `8`; equity avg `0.0343` n `152`; fx avg `-0.0005` n `6`; index avg `0.0022` n `26`; metal avg `-0.0019` n `20`; unknown avg `0.4129` n `1211`
- 1h: commodity avg `0.0261` n `13`; crypto_alt avg `-0.2354` n `237`; crypto_major avg `-0.2373` n `8`; equity avg `-0.0569` n `152`; fx avg `0.003` n `6`; index avg `0.0007` n `26`; metal avg `-0.0165` n `20`; unknown avg `0.1903` n `1179`
- 4h: commodity avg `-0.0097` n `13`; crypto_alt avg `0.8243` n `237`; crypto_major avg `0.5728` n `8`; equity avg `0.2861` n `152`; fx avg `-0.0015` n `6`; index avg `0.0447` n `26`; metal avg `0.0136` n `20`; unknown avg `0.9075` n `1147`
- 24h: commodity avg `0.0054` n `13`; crypto_alt avg `-2.1133` n `237`; crypto_major avg `-1.6143` n `8`; equity avg `-0.271` n `152`; fx avg `-0.037` n `6`; index avg `-0.0425` n `26`; metal avg `-0.1591` n `20`; unknown avg `0.4886` n `1076`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
