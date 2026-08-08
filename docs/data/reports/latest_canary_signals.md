# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T21:22:30.534248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.0419` n `230`; crypto_major avg `0.0222` n `8`; equity avg `-0.0165` n `112`; fx avg `0.0025` n `6`; index avg `-0.0032` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0492` n `784`
- 1h: commodity avg `0.0044` n `12`; crypto_alt avg `0.0323` n `230`; crypto_major avg `0.0348` n `8`; equity avg `0.0399` n `112`; fx avg `0.0034` n `6`; index avg `0.0081` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0391` n `784`
- 4h: commodity avg `0.0321` n `12`; crypto_alt avg `0.0251` n `230`; crypto_major avg `-0.1219` n `8`; equity avg `0.1506` n `112`; fx avg `0.0013` n `6`; index avg `0.0266` n `25`; metal avg `0.0044` n `20`; unknown avg `0.2681` n `784`
- 24h: commodity avg `0.1439` n `12`; crypto_alt avg `1.7591` n `230`; crypto_major avg `1.4421` n `8`; equity avg `0.6513` n `112`; fx avg `-0.0006` n `6`; index avg `0.0349` n `25`; metal avg `0.0527` n `20`; unknown avg `0.2042` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
