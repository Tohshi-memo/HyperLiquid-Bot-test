# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T23:52:28.397139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `0.0729` n `229`; crypto_major avg `-0.0515` n `8`; equity avg `-0.0487` n `88`; fx avg `0.0044` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0785` n `765`
- 1h: commodity avg `0.0034` n `12`; crypto_alt avg `0.1081` n `229`; crypto_major avg `0.0838` n `8`; equity avg `-0.0235` n `88`; fx avg `0.0169` n `6`; index avg `-0.0131` n `25`; metal avg `0.0209` n `20`; unknown avg `1.1287` n `765`
- 4h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.4685` n `229`; crypto_major avg `0.3515` n `8`; equity avg `-0.0483` n `88`; fx avg `-0.0175` n `6`; index avg `-0.0513` n `25`; metal avg `0.0258` n `20`; unknown avg `0.26` n `765`
- 24h: commodity avg `0.1539` n `12`; crypto_alt avg `3.1348` n `229`; crypto_major avg `3.0591` n `8`; equity avg `1.6837` n `88`; fx avg `-0.088` n `6`; index avg `0.3436` n `25`; metal avg `0.5055` n `20`; unknown avg `6.0988` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
