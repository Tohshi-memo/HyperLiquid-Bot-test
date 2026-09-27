# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T23:26:11.936146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0372` n `12`; crypto_alt avg `0.2728` n `234`; crypto_major avg `0.3173` n `8`; equity avg `-0.0073` n `141`; fx avg `0.0008` n `6`; index avg `0.0219` n `26`; metal avg `0.0161` n `20`; unknown avg `2.9049` n `962`
- 1h: commodity avg `0.0251` n `12`; crypto_alt avg `0.2612` n `234`; crypto_major avg `0.0806` n `8`; equity avg `-0.1086` n `141`; fx avg `-0.0065` n `6`; index avg `0.0131` n `26`; metal avg `-0.0294` n `20`; unknown avg `2.4079` n `936`
- 4h: commodity avg `-0.2643` n `12`; crypto_alt avg `-0.4971` n `234`; crypto_major avg `-0.5652` n `8`; equity avg `-0.378` n `141`; fx avg `-0.0188` n `6`; index avg `-0.074` n `26`; metal avg `-0.1679` n `20`; unknown avg `2.2488` n `886`
- 24h: commodity avg `-0.4645` n `12`; crypto_alt avg `0.513` n `234`; crypto_major avg `-0.1511` n `8`; equity avg `-0.0455` n `141`; fx avg `-0.0208` n `6`; index avg `-0.0351` n `26`; metal avg `-0.1759` n `20`; unknown avg `4.854` n `827`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
