# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T09:07:18.374135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.1185` n `228`; crypto_major avg `0.0224` n `8`; equity avg `-0.0189` n `65`; fx avg `0.0` n `5`; index avg `0.0281` n `23`; metal avg `0.0109` n `18`; unknown avg `-0.0778` n `376`
- 1h: commodity avg `0.0455` n `12`; crypto_alt avg `-0.1038` n `228`; crypto_major avg `0.0017` n `8`; equity avg `-0.0316` n `65`; fx avg `-0.0008` n `5`; index avg `0.0825` n `23`; metal avg `0.0076` n `18`; unknown avg `-0.036` n `376`
- 4h: commodity avg `0.0614` n `12`; crypto_alt avg `-0.2728` n `228`; crypto_major avg `0.0726` n `8`; equity avg `0.0895` n `65`; fx avg `0.0202` n `5`; index avg `0.0835` n `23`; metal avg `0.0255` n `18`; unknown avg `0.0356` n `356`
- 24h: commodity avg `0.0909` n `12`; crypto_alt avg `3.7645` n `228`; crypto_major avg `2.3833` n `8`; equity avg `2.6572` n `65`; fx avg `-0.0201` n `5`; index avg `1.1705` n `23`; metal avg `-0.1124` n `18`; unknown avg `0.8957` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
