# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T11:22:26.957421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `0.0461` n `229`; crypto_major avg `0.0373` n `8`; equity avg `0.0325` n `91`; fx avg `0.0088` n `6`; index avg `0.0117` n `25`; metal avg `0.1172` n `20`; unknown avg `0.0435` n `763`
- 1h: commodity avg `0.0818` n `12`; crypto_alt avg `-0.1606` n `229`; crypto_major avg `-0.3047` n `8`; equity avg `-0.2041` n `91`; fx avg `-0.023` n `6`; index avg `-0.0802` n `25`; metal avg `0.0143` n `20`; unknown avg `-0.0213` n `763`
- 4h: commodity avg `0.0317` n `12`; crypto_alt avg `-0.0585` n `229`; crypto_major avg `-0.4298` n `8`; equity avg `-0.4619` n `91`; fx avg `-0.1135` n `6`; index avg `-0.1065` n `25`; metal avg `0.2215` n `20`; unknown avg `-0.4432` n `757`
- 24h: commodity avg `0.4435` n `12`; crypto_alt avg `0.3949` n `229`; crypto_major avg `-0.445` n `8`; equity avg `-1.6118` n `90`; fx avg `-0.1447` n `6`; index avg `-0.4242` n `25`; metal avg `-0.2299` n `20`; unknown avg `-0.408` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
