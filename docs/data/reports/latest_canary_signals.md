# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T17:52:29.069267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `0.0014` n `230`; crypto_major avg `-0.0221` n `8`; equity avg `0.0062` n `112`; fx avg `-0.0027` n `6`; index avg `-0.0023` n `25`; metal avg `0.0066` n `20`; unknown avg `0.0311` n `784`
- 1h: commodity avg `0.0747` n `12`; crypto_alt avg `0.0274` n `230`; crypto_major avg `0.0255` n `8`; equity avg `0.1077` n `112`; fx avg `-0.0029` n `6`; index avg `0.0014` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0601` n `784`
- 4h: commodity avg `0.0014` n `12`; crypto_alt avg `0.948` n `230`; crypto_major avg `0.6948` n `8`; equity avg `0.2309` n `112`; fx avg `-0.0049` n `6`; index avg `0.0174` n `25`; metal avg `0.014` n `20`; unknown avg `0.03` n `784`
- 24h: commodity avg `-0.1403` n `12`; crypto_alt avg `1.7548` n `230`; crypto_major avg `1.9512` n `8`; equity avg `1.0048` n `112`; fx avg `0.0088` n `6`; index avg `0.0774` n `25`; metal avg `0.0956` n `20`; unknown avg `0.1613` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
