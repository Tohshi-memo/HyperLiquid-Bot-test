# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T03:22:30.100982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `13`; crypto_alt avg `0.2526` n `237`; crypto_major avg `0.0882` n `8`; equity avg `0.0915` n `152`; fx avg `-0.015` n `6`; index avg `0.011` n `26`; metal avg `0.0088` n `20`; unknown avg `0.71` n `1231`
- 1h: commodity avg `-0.0219` n `13`; crypto_alt avg `0.2431` n `237`; crypto_major avg `0.2092` n `8`; equity avg `0.0451` n `152`; fx avg `-0.0087` n `6`; index avg `0.0097` n `26`; metal avg `-0.0021` n `20`; unknown avg `0.4839` n `1225`
- 4h: commodity avg `-0.0215` n `13`; crypto_alt avg `0.1003` n `237`; crypto_major avg `0.7892` n `8`; equity avg `0.1519` n `152`; fx avg `-0.0098` n `6`; index avg `0.023` n `26`; metal avg `0.0145` n `20`; unknown avg `0.2995` n `1211`
- 24h: commodity avg `0.1482` n `13`; crypto_alt avg `-1.2506` n `237`; crypto_major avg `-0.1107` n `8`; equity avg `-0.0449` n `152`; fx avg `-0.0437` n `6`; index avg `0.006` n `26`; metal avg `-0.0779` n `20`; unknown avg `30.041` n `1066`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.16`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
