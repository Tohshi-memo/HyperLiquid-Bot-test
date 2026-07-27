# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T18:51:26.622401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0918` n `12`; crypto_alt avg `-0.1219` n `230`; crypto_major avg `-0.056` n `8`; equity avg `0.2166` n `102`; fx avg `0.0026` n `6`; index avg `0.0299` n `25`; metal avg `-0.0001` n `20`; unknown avg `-0.0388` n `774`
- 1h: commodity avg `-0.0617` n `12`; crypto_alt avg `-0.3756` n `230`; crypto_major avg `-0.4189` n `8`; equity avg `0.0691` n `102`; fx avg `0.0239` n `6`; index avg `0.0384` n `25`; metal avg `-0.0395` n `20`; unknown avg `-0.0814` n `774`
- 4h: commodity avg `-0.2617` n `12`; crypto_alt avg `-0.198` n `230`; crypto_major avg `-0.0994` n `8`; equity avg `-0.037` n `102`; fx avg `-0.0481` n `6`; index avg `-0.0504` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.4587` n `774`
- 24h: commodity avg `-0.8425` n `12`; crypto_alt avg `-1.4343` n `230`; crypto_major avg `-0.7767` n `8`; equity avg `-1.7959` n `102`; fx avg `-0.0011` n `6`; index avg `-0.4651` n `25`; metal avg `0.1282` n `20`; unknown avg `-0.3919` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
