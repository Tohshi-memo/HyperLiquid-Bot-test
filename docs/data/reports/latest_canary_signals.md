# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T19:07:26.102969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.0133` n `231`; crypto_major avg `0.0204` n `8`; equity avg `0.0086` n `128`; fx avg `-0.0114` n `6`; index avg `0.0146` n `26`; metal avg `0.0054` n `20`; unknown avg `0.1438` n `792`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.3864` n `231`; crypto_major avg `0.2878` n `8`; equity avg `0.0374` n `128`; fx avg `-0.0204` n `6`; index avg `0.0183` n `26`; metal avg `0.0142` n `20`; unknown avg `0.0245` n `792`
- 4h: commodity avg `0.0005` n `12`; crypto_alt avg `0.0003` n `231`; crypto_major avg `0.2498` n `8`; equity avg `0.0548` n `128`; fx avg `-0.0179` n `6`; index avg `0.0134` n `26`; metal avg `0.0408` n `20`; unknown avg `-0.1026` n `786`
- 24h: commodity avg `0.0308` n `12`; crypto_alt avg `1.2651` n `231`; crypto_major avg `1.4287` n `8`; equity avg `0.3551` n `128`; fx avg `-0.0511` n `6`; index avg `0.0567` n `26`; metal avg `0.1438` n `20`; unknown avg `0.2056` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
