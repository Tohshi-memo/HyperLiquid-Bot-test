# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T14:52:26.399032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.069` n `232`; crypto_major avg `-0.0816` n `8`; equity avg `0.0606` n `131`; fx avg `-0.0019` n `6`; index avg `0.0221` n `26`; metal avg `-0.0515` n `20`; unknown avg `-0.0862` n `792`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.3652` n `232`; crypto_major avg `0.2148` n `8`; equity avg `0.4034` n `131`; fx avg `-0.0049` n `6`; index avg `0.0925` n `26`; metal avg `0.0116` n `20`; unknown avg `-0.0276` n `790`
- 4h: commodity avg `-0.0962` n `12`; crypto_alt avg `0.4284` n `232`; crypto_major avg `0.0697` n `8`; equity avg `-0.4426` n `130`; fx avg `-0.0187` n `6`; index avg `0.0446` n `26`; metal avg `-0.0365` n `20`; unknown avg `-0.2349` n `790`
- 24h: commodity avg `0.3116` n `12`; crypto_alt avg `1.2262` n `232`; crypto_major avg `0.0874` n `8`; equity avg `-0.921` n `130`; fx avg `0.0325` n `6`; index avg `-0.1418` n `26`; metal avg `-0.5548` n `20`; unknown avg `-0.1085` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0403`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.035`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0309`, n `668`, weak_sample_signal
