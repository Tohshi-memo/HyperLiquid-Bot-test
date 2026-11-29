# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-29T00:07:27.642125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.028` n `13`; crypto_alt avg `0.0526` n `239`; crypto_major avg `-0.003` n `8`; equity avg `0.0284` n `168`; fx avg `0.0089` n `6`; index avg `-0.0005` n `27`; metal avg `0.0009` n `20`; unknown avg `7.5637` n `1244`
- 1h: commodity avg `0.0407` n `13`; crypto_alt avg `0.0697` n `239`; crypto_major avg `-0.0941` n `8`; equity avg `0.0491` n `168`; fx avg `0.0077` n `6`; index avg `0.001` n `27`; metal avg `0.0061` n `20`; unknown avg `7.9795` n `1250`
- 4h: commodity avg `0.1835` n `13`; crypto_alt avg `0.0722` n `239`; crypto_major avg `0.1773` n `8`; equity avg `0.0819` n `168`; fx avg `0.013` n `6`; index avg `0.0112` n `27`; metal avg `0.0122` n `20`; unknown avg `5.4019` n `1170`
- 24h: commodity avg `0.1319` n `13`; crypto_alt avg `-3.3951` n `239`; crypto_major avg `-1.1146` n `8`; equity avg `-0.0479` n `168`; fx avg `0.0156` n `6`; index avg `-0.0249` n `27`; metal avg `0.0178` n `20`; unknown avg `3.3568` n `1063`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
