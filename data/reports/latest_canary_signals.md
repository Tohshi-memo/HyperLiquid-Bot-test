# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-29T00:37:32.136431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.124` n `239`; crypto_major avg `-0.1294` n `8`; equity avg `-0.0031` n `168`; fx avg `0.0058` n `6`; index avg `-0.0001` n `27`; metal avg `0.0051` n `20`; unknown avg `-0.0718` n `1264`
- 1h: commodity avg `0.0958` n `13`; crypto_alt avg `-0.4798` n `239`; crypto_major avg `-0.4464` n `8`; equity avg `-0.053` n `168`; fx avg `-0.0013` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0162` n `20`; unknown avg `359.4918` n `1254`
- 4h: commodity avg `0.2256` n `13`; crypto_alt avg `-0.0515` n `239`; crypto_major avg `-0.0478` n `8`; equity avg `0.1018` n `168`; fx avg `0.0086` n `6`; index avg `0.0154` n `27`; metal avg `0.0126` n `20`; unknown avg `43.6413` n `1188`
- 24h: commodity avg `0.4122` n `13`; crypto_alt avg `-3.5808` n `239`; crypto_major avg `-1.431` n `8`; equity avg `-0.0177` n `168`; fx avg `0.008` n `6`; index avg `-0.019` n `27`; metal avg `0.0215` n `20`; unknown avg `0.6271` n `1067`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
