# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T05:52:28.594610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0435` n `228`; crypto_major avg `0.0237` n `8`; equity avg `0.02` n `88`; fx avg `0.0125` n `6`; index avg `-0.0028` n `23`; metal avg `0.0138` n `20`; unknown avg `10.4151` n `764`
- 1h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.3874` n `228`; crypto_major avg `-0.3566` n `8`; equity avg `-0.0341` n `88`; fx avg `-0.0069` n `6`; index avg `-0.0067` n `23`; metal avg `-0.0255` n `20`; unknown avg `1.2317` n `764`
- 4h: commodity avg `-0.2524` n `12`; crypto_alt avg `-0.0167` n `228`; crypto_major avg `-0.4124` n `8`; equity avg `-0.0156` n `88`; fx avg `-0.0053` n `6`; index avg `0.0061` n `23`; metal avg `-0.0216` n `20`; unknown avg `15.9636` n `714`
- 24h: commodity avg `0.2118` n `12`; crypto_alt avg `-0.6993` n `228`; crypto_major avg `-1.4918` n `8`; equity avg `0.027` n `88`; fx avg `-0.0174` n `6`; index avg `-0.1027` n `23`; metal avg `-0.0588` n `20`; unknown avg `15.9972` n `682`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2192`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
