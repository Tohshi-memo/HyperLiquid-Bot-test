# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T13:07:26.984523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.0231` n `230`; crypto_major avg `0.0406` n `8`; equity avg `-0.0139` n `112`; fx avg `-0.0063` n `6`; index avg `-0.0014` n `25`; metal avg `0.002` n `20`; unknown avg `0.0069` n `784`
- 1h: commodity avg `0.0122` n `12`; crypto_alt avg `0.1115` n `230`; crypto_major avg `0.1701` n `8`; equity avg `0.0228` n `112`; fx avg `0.0032` n `6`; index avg `0.0184` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0383` n `784`
- 4h: commodity avg `0.0766` n `12`; crypto_alt avg `0.3392` n `230`; crypto_major avg `0.3054` n `8`; equity avg `0.1461` n `112`; fx avg `-0.0105` n `6`; index avg `0.0144` n `25`; metal avg `-0.0101` n `20`; unknown avg `0.5456` n `784`
- 24h: commodity avg `0.1411` n `12`; crypto_alt avg `0.2624` n `230`; crypto_major avg `-0.0685` n `8`; equity avg `-0.1127` n `112`; fx avg `0.0187` n `6`; index avg `-0.0932` n `25`; metal avg `-0.0422` n `20`; unknown avg `0.5028` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
