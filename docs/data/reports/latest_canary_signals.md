# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T14:54:20.874199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `-0.0306` n `230`; crypto_major avg `0.1188` n `8`; equity avg `-0.0435` n `112`; fx avg `0.0041` n `6`; index avg `-0.0035` n `25`; metal avg `0.0014` n `20`; unknown avg `0.121` n `784`
- 1h: commodity avg `-0.1138` n `12`; crypto_alt avg `0.3659` n `230`; crypto_major avg `0.7076` n `8`; equity avg `0.0122` n `112`; fx avg `0.0008` n `6`; index avg `0.0068` n `25`; metal avg `0.0042` n `20`; unknown avg `0.0293` n `784`
- 4h: commodity avg `-0.0493` n `12`; crypto_alt avg `0.5091` n `230`; crypto_major avg `0.8477` n `8`; equity avg `0.1726` n `112`; fx avg `0.0075` n `6`; index avg `0.0368` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.2108` n `784`
- 24h: commodity avg `-0.1887` n `12`; crypto_alt avg `1.1158` n `230`; crypto_major avg `1.1704` n `8`; equity avg `1.3036` n `112`; fx avg `-0.009` n `6`; index avg `0.1095` n `25`; metal avg `0.0754` n `20`; unknown avg `0.0016` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
