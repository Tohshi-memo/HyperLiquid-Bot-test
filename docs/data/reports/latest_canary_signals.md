# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T17:37:28.205221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0442` n `13`; crypto_alt avg `0.1632` n `239`; crypto_major avg `0.0876` n `8`; equity avg `0.3355` n `162`; fx avg `0.0002` n `6`; index avg `0.0386` n `27`; metal avg `0.0187` n `20`; unknown avg `0.6508` n `1259`
- 1h: commodity avg `0.1687` n `13`; crypto_alt avg `-0.0913` n `239`; crypto_major avg `0.1424` n `8`; equity avg `-0.0038` n `162`; fx avg `-0.0187` n `6`; index avg `0.0016` n `27`; metal avg `0.0515` n `20`; unknown avg `45.1543` n `1239`
- 4h: commodity avg `0.119` n `13`; crypto_alt avg `0.0635` n `239`; crypto_major avg `-0.0989` n `8`; equity avg `1.2449` n `162`; fx avg `-0.0592` n `6`; index avg `0.1803` n `27`; metal avg `-0.1538` n `20`; unknown avg `49.8653` n `1227`
- 24h: commodity avg `0.298` n `13`; crypto_alt avg `-3.7246` n `239`; crypto_major avg `-3.6572` n `8`; equity avg `-3.1062` n `162`; fx avg `-0.1219` n `6`; index avg `-0.161` n `27`; metal avg `-0.89` n `20`; unknown avg `3.9175` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
