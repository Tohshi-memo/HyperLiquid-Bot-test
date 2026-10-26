# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T08:07:32.467419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `13`; crypto_alt avg `-0.1994` n `237`; crypto_major avg `-0.3168` n `8`; equity avg `-0.2134` n `152`; fx avg `0.0104` n `6`; index avg `-0.0135` n `26`; metal avg `0.0488` n `20`; unknown avg `-0.0895` n `1184`
- 1h: commodity avg `0.0518` n `13`; crypto_alt avg `-0.5052` n `237`; crypto_major avg `-0.5437` n `8`; equity avg `-0.343` n `152`; fx avg `0.0003` n `6`; index avg `-0.0187` n `26`; metal avg `0.0723` n `20`; unknown avg `4.1029` n `1178`
- 4h: commodity avg `0.1462` n `13`; crypto_alt avg `-0.0145` n `237`; crypto_major avg `0.0557` n `8`; equity avg `-0.3188` n `152`; fx avg `0.0086` n `6`; index avg `-0.0725` n `26`; metal avg `0.0011` n `20`; unknown avg `4.4058` n `1150`
- 24h: commodity avg `-0.5203` n `13`; crypto_alt avg `-1.1446` n `237`; crypto_major avg `-0.9178` n `8`; equity avg `-0.844` n `152`; fx avg `0.0452` n `6`; index avg `-0.0545` n `26`; metal avg `0.1556` n `20`; unknown avg `-0.3636` n `953`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2526`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
