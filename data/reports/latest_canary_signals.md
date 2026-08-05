# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T06:37:32.870542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0583` n `12`; crypto_alt avg `0.1155` n `230`; crypto_major avg `0.1378` n `8`; equity avg `-0.0192` n `108`; fx avg `-0.0053` n `6`; index avg `-0.0099` n `25`; metal avg `0.0792` n `20`; unknown avg `0.026` n `781`
- 1h: commodity avg `0.1436` n `12`; crypto_alt avg `0.0964` n `230`; crypto_major avg `0.0959` n `8`; equity avg `-0.0789` n `108`; fx avg `-0.0012` n `6`; index avg `-0.0082` n `25`; metal avg `0.211` n `20`; unknown avg `0.014` n `749`
- 4h: commodity avg `0.2438` n `12`; crypto_alt avg `0.2627` n `230`; crypto_major avg `0.0604` n `8`; equity avg `0.5476` n `108`; fx avg `0.0259` n `6`; index avg `0.0544` n `25`; metal avg `0.3796` n `20`; unknown avg `0.062` n `749`
- 24h: commodity avg `-1.3606` n `12`; crypto_alt avg `0.7792` n `230`; crypto_major avg `1.0871` n `8`; equity avg `3.6569` n `108`; fx avg `-0.0253` n `6`; index avg `0.7523` n `25`; metal avg `1.397` n `20`; unknown avg `0.5163` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
