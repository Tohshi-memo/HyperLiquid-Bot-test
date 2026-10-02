# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T09:07:36.366700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `13`; crypto_alt avg `-0.1327` n `234`; crypto_major avg `-0.1461` n `8`; equity avg `-0.0684` n `142`; fx avg `0.0062` n `6`; index avg `-0.019` n `26`; metal avg `-0.0287` n `20`; unknown avg `0.6871` n `983`
- 1h: commodity avg `-0.0351` n `13`; crypto_alt avg `0.092` n `234`; crypto_major avg `0.0919` n `8`; equity avg `0.0313` n `142`; fx avg `-0.0102` n `6`; index avg `-0.0043` n `26`; metal avg `-0.1153` n `20`; unknown avg `0.1021` n `971`
- 4h: commodity avg `-0.552` n `13`; crypto_alt avg `0.2033` n `234`; crypto_major avg `0.0584` n `8`; equity avg `0.3647` n `142`; fx avg `-0.1321` n `6`; index avg `0.0912` n `26`; metal avg `-0.0706` n `20`; unknown avg `-0.3245` n `891`
- 24h: commodity avg `-0.7311` n `13`; crypto_alt avg `1.4541` n `234`; crypto_major avg `2.0978` n `8`; equity avg `1.2102` n `142`; fx avg `-0.3355` n `6`; index avg `0.2254` n `26`; metal avg `0.2299` n `20`; unknown avg `-0.0311` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
