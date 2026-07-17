# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T11:52:32.642753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.0149` n `230`; crypto_major avg `0.0612` n `8`; equity avg `-0.095` n `96`; fx avg `-0.0196` n `6`; index avg `-0.0163` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0425` n `769`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `0.0806` n `8`; equity avg `-0.3395` n `96`; fx avg `0.0129` n `6`; index avg `-0.0616` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.1499` n `769`
- 4h: commodity avg `0.3185` n `12`; crypto_alt avg `0.3271` n `230`; crypto_major avg `0.5255` n `8`; equity avg `0.6634` n `96`; fx avg `0.0069` n `6`; index avg `0.0583` n `25`; metal avg `-0.0381` n `20`; unknown avg `0.1455` n `768`
- 24h: commodity avg `0.0028` n `12`; crypto_alt avg `-1.3727` n `230`; crypto_major avg `-2.4391` n `8`; equity avg `-4.1956` n `94`; fx avg `-0.0237` n `6`; index avg `-0.5338` n `25`; metal avg `-0.6828` n `20`; unknown avg `-0.2548` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
