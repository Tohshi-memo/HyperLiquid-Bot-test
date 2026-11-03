# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T14:07:27.122669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3088` n `13`; crypto_alt avg `-0.3033` n `239`; crypto_major avg `-0.232` n `8`; equity avg `-0.2191` n `157`; fx avg `0.0196` n `6`; index avg `-0.0425` n `27`; metal avg `-0.14` n `20`; unknown avg `497.3101` n `1258`
- 1h: commodity avg `-0.3962` n `13`; crypto_alt avg `-0.2235` n `239`; crypto_major avg `-0.0491` n `8`; equity avg `0.3572` n `157`; fx avg `-0.0075` n `6`; index avg `0.0767` n `27`; metal avg `0.091` n `20`; unknown avg `14.3711` n `1258`
- 4h: commodity avg `-0.3391` n `13`; crypto_alt avg `1.015` n `239`; crypto_major avg `0.6746` n `8`; equity avg `0.6108` n `157`; fx avg `0.0007` n `6`; index avg `0.0991` n `27`; metal avg `0.3572` n `20`; unknown avg `259.2984` n `1222`
- 24h: commodity avg `-0.4443` n `13`; crypto_alt avg `-1.0119` n `239`; crypto_major avg `-0.4716` n `8`; equity avg `-2.4792` n `157`; fx avg `0.0115` n `6`; index avg `-0.1339` n `27`; metal avg `-0.2868` n `20`; unknown avg `0.1269` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
