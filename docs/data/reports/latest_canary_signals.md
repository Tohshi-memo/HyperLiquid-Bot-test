# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T09:00:29.304382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `0.0544` n `8`; equity avg `-0.0423` n `112`; fx avg `0.0006` n `6`; index avg `-0.0057` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.016` n `785`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.2262` n `230`; crypto_major avg `-0.2469` n `8`; equity avg `-0.081` n `112`; fx avg `-0.0021` n `6`; index avg `-0.0224` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.0104` n `785`
- 4h: commodity avg `-0.0219` n `12`; crypto_alt avg `-0.2655` n `230`; crypto_major avg `-0.0107` n `8`; equity avg `-0.024` n `112`; fx avg `-0.0209` n `6`; index avg `-0.0271` n `25`; metal avg `0.024` n `20`; unknown avg `-0.065` n `752`
- 24h: commodity avg `0.2608` n `12`; crypto_alt avg `1.1617` n `230`; crypto_major avg `0.2825` n `8`; equity avg `0.4996` n `112`; fx avg `-0.0206` n `6`; index avg `0.0419` n `25`; metal avg `0.0325` n `20`; unknown avg `0.3179` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0452`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
