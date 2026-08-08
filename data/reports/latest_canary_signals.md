# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:37:27.117258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0155` n `230`; crypto_major avg `0.06` n `8`; equity avg `-0.0078` n `112`; fx avg `-0.0052` n `6`; index avg `-0.0002` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.0187` n `784`
- 1h: commodity avg `-0.0393` n `12`; crypto_alt avg `-0.0369` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `-0.0285` n `112`; fx avg `-0.0035` n `6`; index avg `0.0109` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.1106` n `784`
- 4h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.0085` n `230`; crypto_major avg `-0.1403` n `8`; equity avg `-0.043` n `112`; fx avg `-0.009` n `6`; index avg `0.0096` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.2017` n `784`
- 24h: commodity avg `0.1519` n `12`; crypto_alt avg `1.8411` n `230`; crypto_major avg `1.241` n `8`; equity avg `0.6116` n `112`; fx avg `-0.0116` n `6`; index avg `0.0507` n `25`; metal avg `0.0398` n `20`; unknown avg `0.1941` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
