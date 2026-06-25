# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T23:07:27.011385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.0216` n `228`; crypto_major avg `-0.0107` n `8`; equity avg `0.0763` n `86`; fx avg `-0.0011` n `6`; index avg `0.0028` n `23`; metal avg `0.0304` n `20`; unknown avg `-0.3523` n `765`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.1876` n `228`; crypto_major avg `-0.0847` n `8`; equity avg `0.0331` n `86`; fx avg `-0.0036` n `6`; index avg `0.014` n `23`; metal avg `0.0237` n `20`; unknown avg `0.3611` n `765`
- 4h: commodity avg `-0.1209` n `12`; crypto_alt avg `0.9088` n `228`; crypto_major avg `0.9342` n `8`; equity avg `0.1195` n `86`; fx avg `-0.0223` n `6`; index avg `-0.0008` n `23`; metal avg `-0.1231` n `20`; unknown avg `0.3291` n `765`
- 24h: commodity avg `0.376` n `12`; crypto_alt avg `-1.3536` n `228`; crypto_major avg `-1.3366` n `8`; equity avg `-2.4509` n `86`; fx avg `0.1022` n `6`; index avg `-0.2728` n `23`; metal avg `0.3461` n `20`; unknown avg `0.65` n `716`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
