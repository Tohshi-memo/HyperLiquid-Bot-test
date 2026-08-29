# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T01:22:25.061010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0592` n `231`; crypto_major avg `0.0831` n `8`; equity avg `0.0117` n `127`; fx avg `-0.0034` n `6`; index avg `0.0043` n `26`; metal avg `0.0067` n `20`; unknown avg `-0.055` n `793`
- 1h: commodity avg `0.0567` n `12`; crypto_alt avg `-0.3134` n `231`; crypto_major avg `-0.3326` n `8`; equity avg `0.0064` n `127`; fx avg `-0.008` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0326` n `20`; unknown avg `-0.1137` n `793`
- 4h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.4613` n `231`; crypto_major avg `0.2835` n `8`; equity avg `0.0784` n `127`; fx avg `0.0019` n `6`; index avg `-0.0069` n `26`; metal avg `0.0431` n `20`; unknown avg `0.0669` n `793`
- 24h: commodity avg `-0.101` n `12`; crypto_alt avg `-3.8219` n `231`; crypto_major avg `-4.0471` n `8`; equity avg `-2.1803` n `127`; fx avg `-0.1143` n `6`; index avg `-0.2297` n `26`; metal avg `-0.3502` n `20`; unknown avg `-0.6225` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
