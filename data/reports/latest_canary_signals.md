# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T12:52:30.965619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0514` n `12`; crypto_alt avg `-0.023` n `229`; crypto_major avg `-0.2217` n `8`; equity avg `-0.1113` n `91`; fx avg `-0.0154` n `6`; index avg `-0.0132` n `25`; metal avg `0.0188` n `20`; unknown avg `0.0461` n `766`
- 1h: commodity avg `-0.1982` n `12`; crypto_alt avg `-0.0618` n `229`; crypto_major avg `-0.3583` n `8`; equity avg `-0.1123` n `91`; fx avg `-0.0252` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0474` n `20`; unknown avg `-0.0289` n `766`
- 4h: commodity avg `-0.0195` n `12`; crypto_alt avg `0.1472` n `229`; crypto_major avg `-0.092` n `8`; equity avg `0.3954` n `91`; fx avg `0.0136` n `6`; index avg `0.0575` n `25`; metal avg `0.0417` n `20`; unknown avg `-0.0447` n `765`
- 24h: commodity avg `-1.0493` n `12`; crypto_alt avg `1.1671` n `229`; crypto_major avg `1.713` n `8`; equity avg `0.2123` n `91`; fx avg `-0.1081` n `6`; index avg `0.0894` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.0239` n `733`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
