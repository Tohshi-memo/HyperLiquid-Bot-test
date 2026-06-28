# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T13:37:28.176805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `0.1494` n `228`; crypto_major avg `0.1128` n `8`; equity avg `0.0398` n `88`; fx avg `-0.0033` n `6`; index avg `-0.0035` n `23`; metal avg `-0.0089` n `20`; unknown avg `0.0018` n `764`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `-0.2249` n `228`; crypto_major avg `-0.0667` n `8`; equity avg `0.0202` n `88`; fx avg `-0.005` n `6`; index avg `0.0085` n `23`; metal avg `-0.0299` n `20`; unknown avg `-0.018` n `764`
- 4h: commodity avg `0.086` n `12`; crypto_alt avg `-0.2173` n `228`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0361` n `88`; fx avg `0.0029` n `6`; index avg `0.0092` n `23`; metal avg `-0.0316` n `20`; unknown avg `1.4579` n `750`
- 24h: commodity avg `0.1661` n `12`; crypto_alt avg `-0.3716` n `228`; crypto_major avg `-0.9763` n `8`; equity avg `0.0518` n `88`; fx avg `-0.003` n `6`; index avg `-0.0544` n `23`; metal avg `-0.0418` n `20`; unknown avg `15.4576` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
