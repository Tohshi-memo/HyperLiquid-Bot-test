# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T12:22:24.232227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0611` n `230`; crypto_major avg `0.0315` n `8`; equity avg `-0.0254` n `102`; fx avg `-0.0115` n `6`; index avg `0.0062` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0086` n `782`
- 1h: commodity avg `-0.0045` n `12`; crypto_alt avg `0.2429` n `230`; crypto_major avg `0.0879` n `8`; equity avg `-0.0784` n `102`; fx avg `-0.027` n `6`; index avg `-0.0603` n `25`; metal avg `0.0052` n `20`; unknown avg `-0.0014` n `781`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `0.0557` n `230`; crypto_major avg `-0.1608` n `8`; equity avg `-0.1057` n `102`; fx avg `-0.0918` n `6`; index avg `-0.0129` n `25`; metal avg `-0.018` n `20`; unknown avg `-0.0541` n `781`
- 24h: commodity avg `0.3196` n `12`; crypto_alt avg `0.5941` n `230`; crypto_major avg `-1.1903` n `8`; equity avg `-2.246` n `102`; fx avg `-0.1617` n `6`; index avg `-0.2413` n `25`; metal avg `-0.0085` n `20`; unknown avg `4.5939` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
