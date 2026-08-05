# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T19:37:25.424947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.022` n `230`; crypto_major avg `0.0105` n `8`; equity avg `-0.1366` n `108`; fx avg `0.0005` n `6`; index avg `-0.0204` n `25`; metal avg `-0.045` n `20`; unknown avg `0.0008` n `782`
- 1h: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.0287` n `230`; crypto_major avg `0.0229` n `8`; equity avg `0.0405` n `108`; fx avg `-0.0125` n `6`; index avg `0.0005` n `25`; metal avg `-0.0294` n `20`; unknown avg `-0.1153` n `782`
- 4h: commodity avg `0.0532` n `12`; crypto_alt avg `0.1519` n `230`; crypto_major avg `0.4312` n `8`; equity avg `-0.2352` n `108`; fx avg `-0.0065` n `6`; index avg `-0.0451` n `25`; metal avg `-0.056` n `20`; unknown avg `-0.1281` n `782`
- 24h: commodity avg `-0.069` n `12`; crypto_alt avg `0.5801` n `230`; crypto_major avg `0.9113` n `8`; equity avg `-0.3823` n `108`; fx avg `-0.061` n `6`; index avg `-0.0984` n `25`; metal avg `0.7854` n `20`; unknown avg `0.7786` n `749`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
