# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T03:52:13.031110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `0.0415` n `228`; crypto_major avg `0.0514` n `8`; equity avg `0.0417` n `67`; fx avg `0.0074` n `6`; index avg `0.0427` n `23`; metal avg `0.0367` n `18`; unknown avg `-0.0073` n `386`
- 1h: commodity avg `0.0263` n `12`; crypto_alt avg `0.1153` n `228`; crypto_major avg `-0.0028` n `8`; equity avg `0.1116` n `67`; fx avg `0.0351` n `6`; index avg `0.0355` n `23`; metal avg `0.042` n `18`; unknown avg `-0.0003` n `386`
- 4h: commodity avg `-0.1024` n `12`; crypto_alt avg `0.1897` n `228`; crypto_major avg `-0.2629` n `8`; equity avg `-0.0158` n `67`; fx avg `0.1241` n `6`; index avg `0.1168` n `23`; metal avg `-0.2645` n `18`; unknown avg `-0.272` n `386`
- 24h: commodity avg `-0.8253` n `12`; crypto_alt avg `1.4641` n `228`; crypto_major avg `0.2067` n `8`; equity avg `1.3649` n `66`; fx avg `0.1031` n `6`; index avg `0.6104` n `23`; metal avg `0.5129` n `18`; unknown avg `2.6791` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
