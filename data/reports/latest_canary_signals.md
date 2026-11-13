# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T13:52:26.717597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.125` n `13`; crypto_alt avg `-0.0464` n `239`; crypto_major avg `-0.281` n `8`; equity avg `-0.5097` n `162`; fx avg `-0.0147` n `6`; index avg `-0.0536` n `27`; metal avg `-0.1539` n `20`; unknown avg `2.3782` n `1262`
- 1h: commodity avg `0.0461` n `13`; crypto_alt avg `0.9663` n `239`; crypto_major avg `0.7348` n `8`; equity avg `0.3477` n `162`; fx avg `0.0186` n `6`; index avg `0.0194` n `27`; metal avg `-0.0523` n `20`; unknown avg `1.1727` n `1260`
- 4h: commodity avg `0.1533` n `13`; crypto_alt avg `1.4889` n `239`; crypto_major avg `1.3696` n `8`; equity avg `0.4433` n `162`; fx avg `0.0192` n `6`; index avg `0.0373` n `27`; metal avg `-0.0218` n `20`; unknown avg `42.5715` n `1200`
- 24h: commodity avg `0.6032` n `13`; crypto_alt avg `1.6755` n `239`; crypto_major avg `-0.109` n `8`; equity avg `0.5991` n `162`; fx avg `-0.008` n `6`; index avg `0.1115` n `27`; metal avg `-0.1025` n `20`; unknown avg `1.817` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
