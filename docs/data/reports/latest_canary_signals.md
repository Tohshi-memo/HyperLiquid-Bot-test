# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T23:22:36.245067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.048` n `12`; crypto_alt avg `0.1595` n `231`; crypto_major avg `-0.0501` n `8`; equity avg `-0.0133` n `127`; fx avg `-0.0038` n `6`; index avg `0.0006` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.0872` n `793`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `0.4726` n `231`; crypto_major avg `0.3239` n `8`; equity avg `0.0115` n `127`; fx avg `-0.0125` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.2569` n `793`
- 4h: commodity avg `0.0398` n `12`; crypto_alt avg `0.5504` n `231`; crypto_major avg `0.3186` n `8`; equity avg `0.0329` n `127`; fx avg `-0.0255` n `6`; index avg `-0.0242` n `26`; metal avg `0.0251` n `20`; unknown avg `0.2855` n `793`
- 24h: commodity avg `-0.1475` n `12`; crypto_alt avg `-3.1192` n `231`; crypto_major avg `-3.685` n `8`; equity avg `-1.976` n `127`; fx avg `-0.144` n `6`; index avg `-0.1799` n `26`; metal avg `-0.3537` n `20`; unknown avg `-0.6131` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
