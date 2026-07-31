# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T21:07:26.037198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.4237` n `12`; crypto_alt avg `-0.0198` n `230`; crypto_major avg `0.0114` n `8`; equity avg `-0.0923` n `102`; fx avg `-0.0207` n `6`; index avg `-0.0616` n `25`; metal avg `-0.0578` n `20`; unknown avg `-0.0316` n `781`
- 1h: commodity avg `0.4219` n `12`; crypto_alt avg `-0.0201` n `230`; crypto_major avg `0.1179` n `8`; equity avg `-0.1289` n `102`; fx avg `-0.1061` n `6`; index avg `-0.0737` n `25`; metal avg `-0.0352` n `20`; unknown avg `-0.1277` n `780`
- 4h: commodity avg `0.5522` n `12`; crypto_alt avg `-0.1094` n `230`; crypto_major avg `-0.1394` n `8`; equity avg `-0.3724` n `102`; fx avg `-0.0955` n `6`; index avg `-0.1019` n `25`; metal avg `0.0598` n `20`; unknown avg `7.1103` n `780`
- 24h: commodity avg `0.6218` n `12`; crypto_alt avg `-0.5095` n `230`; crypto_major avg `-2.0808` n `8`; equity avg `-0.9285` n `102`; fx avg `0.0829` n `6`; index avg `0.0872` n `25`; metal avg `-0.431` n `20`; unknown avg `0.2262` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
