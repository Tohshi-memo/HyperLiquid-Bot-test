# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T07:07:30.420833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `-0.1963` n `230`; crypto_major avg `-0.0732` n `8`; equity avg `0.0056` n `112`; fx avg `-0.004` n `6`; index avg `0.001` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.0076` n `785`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0394` n `230`; crypto_major avg `0.119` n `8`; equity avg `0.0214` n `112`; fx avg `-0.0107` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.0052` n `784`
- 4h: commodity avg `0.0225` n `12`; crypto_alt avg `0.1971` n `230`; crypto_major avg `0.203` n `8`; equity avg `-0.0008` n `112`; fx avg `-0.0203` n `6`; index avg `-0.0026` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0031` n `752`
- 24h: commodity avg `0.2483` n `12`; crypto_alt avg `1.433` n `230`; crypto_major avg `0.5587` n `8`; equity avg `0.6978` n `112`; fx avg `-0.0224` n `6`; index avg `0.0671` n `25`; metal avg `0.0215` n `20`; unknown avg `0.5753` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
