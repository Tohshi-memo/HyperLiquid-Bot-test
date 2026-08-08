# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T20:07:28.165997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0514` n `230`; crypto_major avg `0.0145` n `8`; equity avg `-0.0154` n `112`; fx avg `-0.0049` n `6`; index avg `0.0034` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.0023` n `784`
- 1h: commodity avg `0.0188` n `12`; crypto_alt avg `0.0262` n `230`; crypto_major avg `0.1083` n `8`; equity avg `0.1199` n `112`; fx avg `-0.0012` n `6`; index avg `0.0114` n `25`; metal avg `-0.0065` n `20`; unknown avg `-0.071` n `784`
- 4h: commodity avg `0.1469` n `12`; crypto_alt avg `0.0955` n `230`; crypto_major avg `-0.1755` n `8`; equity avg `0.262` n `112`; fx avg `0.0036` n `6`; index avg `0.008` n `25`; metal avg `0.0076` n `20`; unknown avg `0.4275` n `784`
- 24h: commodity avg `0.1627` n `12`; crypto_alt avg `1.4923` n `230`; crypto_major avg `1.1961` n `8`; equity avg `0.6911` n `112`; fx avg `0.0172` n `6`; index avg `0.0355` n `25`; metal avg `0.0997` n `20`; unknown avg `0.2255` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
