# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T15:52:33.808512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.0766` n `8`; equity avg `0.0089` n `112`; fx avg `-0.0057` n `6`; index avg `-0.0108` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.0415` n `784`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.2607` n `230`; crypto_major avg `-0.1436` n `8`; equity avg `0.0594` n `112`; fx avg `-0.0081` n `6`; index avg `0.0158` n `25`; metal avg `0.0097` n `20`; unknown avg `0.06` n `784`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.7791` n `230`; crypto_major avg `0.644` n `8`; equity avg `0.199` n `112`; fx avg `-0.0117` n `6`; index avg `0.0324` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.2492` n `784`
- 24h: commodity avg `-0.2762` n `12`; crypto_alt avg `1.0864` n `230`; crypto_major avg `0.9507` n `8`; equity avg `0.4817` n `112`; fx avg `-0.0024` n `6`; index avg `0.0282` n `25`; metal avg `0.1436` n `20`; unknown avg `-0.1211` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0483`, n `668`, weak_sample_signal
