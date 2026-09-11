# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T09:07:30.805492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `-0.0451` n `233`; crypto_major avg `-0.08` n `8`; equity avg `0.0972` n `136`; fx avg `-0.0163` n `6`; index avg `0.0076` n `26`; metal avg `-0.0238` n `20`; unknown avg `-0.0631` n `794`
- 1h: commodity avg `-0.1935` n `12`; crypto_alt avg `0.1678` n `233`; crypto_major avg `0.2478` n `8`; equity avg `0.4999` n `136`; fx avg `-0.0704` n `6`; index avg `0.0893` n `26`; metal avg `0.0399` n `20`; unknown avg `-0.12` n `788`
- 4h: commodity avg `-0.3967` n `12`; crypto_alt avg `-0.094` n `233`; crypto_major avg `0.2251` n `8`; equity avg `0.9284` n `136`; fx avg `-0.065` n `6`; index avg `0.1679` n `26`; metal avg `0.1952` n `20`; unknown avg `0.8021` n `762`
- 24h: commodity avg `0.4623` n `12`; crypto_alt avg `-1.1158` n `233`; crypto_major avg `-1.3452` n `8`; equity avg `-0.8109` n `136`; fx avg `-0.0436` n `6`; index avg `-0.1201` n `26`; metal avg `-0.8232` n `20`; unknown avg `1.478` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
