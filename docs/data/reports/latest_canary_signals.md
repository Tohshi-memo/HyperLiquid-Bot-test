# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T06:52:28.186189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `-0.0443` n `230`; crypto_major avg `-0.0337` n `8`; equity avg `-0.068` n `102`; fx avg `0.0015` n `6`; index avg `-0.0063` n `25`; metal avg `0.0048` n `20`; unknown avg `0.0234` n `782`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.1093` n `230`; crypto_major avg `-0.1182` n `8`; equity avg `0.042` n `102`; fx avg `-0.0071` n `6`; index avg `0.015` n `25`; metal avg `0.0061` n `20`; unknown avg `0.0069` n `766`
- 4h: commodity avg `-0.2092` n `12`; crypto_alt avg `0.1342` n `230`; crypto_major avg `0.134` n `8`; equity avg `-0.0524` n `102`; fx avg `-0.0664` n `6`; index avg `0.0442` n `25`; metal avg `0.066` n `20`; unknown avg `0.391` n `766`
- 24h: commodity avg `-1.0612` n `12`; crypto_alt avg `0.1519` n `230`; crypto_major avg `0.3754` n `8`; equity avg `0.8147` n `102`; fx avg `-0.1309` n `6`; index avg `0.2302` n `25`; metal avg `0.2681` n `20`; unknown avg `0.3554` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
