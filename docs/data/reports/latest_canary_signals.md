# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T06:52:27.249344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.2224` n `231`; crypto_major avg `0.0874` n `8`; equity avg `0.0963` n `127`; fx avg `0.0113` n `6`; index avg `0.0103` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.0186` n `791`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.2357` n `231`; crypto_major avg `-0.1894` n `8`; equity avg `0.1614` n `127`; fx avg `0.0053` n `6`; index avg `0.0282` n `26`; metal avg `0.0509` n `20`; unknown avg `0.0836` n `775`
- 4h: commodity avg `-0.0585` n `12`; crypto_alt avg `0.2171` n `231`; crypto_major avg `0.1365` n `8`; equity avg `-0.1117` n `127`; fx avg `0.0104` n `6`; index avg `-0.0747` n `26`; metal avg `-0.1829` n `20`; unknown avg `0.1056` n `775`
- 24h: commodity avg `0.2837` n `12`; crypto_alt avg `0.4164` n `231`; crypto_major avg `0.6126` n `8`; equity avg `1.2679` n `127`; fx avg `-0.0642` n `6`; index avg `0.2063` n `26`; metal avg `-0.2789` n `20`; unknown avg `0.3575` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
