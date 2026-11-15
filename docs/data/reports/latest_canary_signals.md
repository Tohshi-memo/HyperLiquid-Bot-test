# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T06:52:27.340619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `13`; crypto_alt avg `0.1045` n `239`; crypto_major avg `0.1242` n `8`; equity avg `0.0538` n `162`; fx avg `-0.001` n `6`; index avg `0.0012` n `27`; metal avg `0.0147` n `20`; unknown avg `0.8803` n `1263`
- 1h: commodity avg `0.002` n `13`; crypto_alt avg `-0.1205` n `239`; crypto_major avg `-0.5259` n `8`; equity avg `-0.0953` n `162`; fx avg `-0.0009` n `6`; index avg `-0.0088` n `27`; metal avg `-0.0141` n `20`; unknown avg `161.7606` n `1241`
- 4h: commodity avg `0.0453` n `13`; crypto_alt avg `0.0811` n `239`; crypto_major avg `-0.479` n `8`; equity avg `-0.1222` n `162`; fx avg `0.0017` n `6`; index avg `-0.0213` n `27`; metal avg `-0.0399` n `20`; unknown avg `0.7029` n `1225`
- 24h: commodity avg `0.0512` n `13`; crypto_alt avg `-5.2386` n `239`; crypto_major avg `-4.8941` n `8`; equity avg `-1.0108` n `162`; fx avg `0.0629` n `6`; index avg `-0.092` n `27`; metal avg `-0.4714` n `20`; unknown avg `46.9621` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
