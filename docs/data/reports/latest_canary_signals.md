# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T20:22:24.149372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0174` n `230`; crypto_major avg `-0.0072` n `8`; equity avg `-0.0325` n `112`; fx avg `-0.0019` n `6`; index avg `-0.0` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.0371` n `784`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.0813` n `230`; crypto_major avg `0.1066` n `8`; equity avg `0.0169` n `112`; fx avg `-0.0003` n `6`; index avg `0.0105` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.073` n `784`
- 4h: commodity avg `0.14` n `12`; crypto_alt avg `0.109` n `230`; crypto_major avg `-0.1329` n `8`; equity avg `0.1843` n `112`; fx avg `0.0084` n `6`; index avg `0.0188` n `25`; metal avg `0.011` n `20`; unknown avg `3.5325` n `784`
- 24h: commodity avg `0.1358` n `12`; crypto_alt avg `1.665` n `230`; crypto_major avg `1.2097` n `8`; equity avg `0.6586` n `112`; fx avg `0.0212` n `6`; index avg `0.0391` n `25`; metal avg `0.1254` n `20`; unknown avg `0.1895` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0452`, n `668`, weak_sample_signal
