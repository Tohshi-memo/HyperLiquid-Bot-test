# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T11:52:41.958213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.0748` n `230`; crypto_major avg `-0.074` n `8`; equity avg `-0.0791` n `108`; fx avg `-0.0008` n `6`; index avg `-0.0166` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.076` n `782`
- 1h: commodity avg `-0.1302` n `12`; crypto_alt avg `-0.0403` n `230`; crypto_major avg `0.001` n `8`; equity avg `0.175` n `108`; fx avg `0.0007` n `6`; index avg `0.0723` n `25`; metal avg `0.2566` n `20`; unknown avg `-0.056` n `782`
- 4h: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.2375` n `230`; crypto_major avg `-0.0829` n `8`; equity avg `-0.3975` n `108`; fx avg `0.0082` n `6`; index avg `-0.0058` n `25`; metal avg `0.007` n `20`; unknown avg `0.589` n `781`
- 24h: commodity avg `-0.2923` n `12`; crypto_alt avg `0.3889` n `230`; crypto_major avg `0.0958` n `8`; equity avg `1.6542` n `108`; fx avg `0.0419` n `6`; index avg `0.5005` n `25`; metal avg `0.8994` n `20`; unknown avg `-0.001` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
