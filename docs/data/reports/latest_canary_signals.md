# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:22:34.031761+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.0198` n `230`; crypto_major avg `-0.0237` n `8`; equity avg `0.0175` n `112`; fx avg `-0.002` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0487` n `785`
- 1h: commodity avg `-0.0106` n `12`; crypto_alt avg `0.075` n `230`; crypto_major avg `0.1318` n `8`; equity avg `0.0163` n `112`; fx avg `0.0082` n `6`; index avg `0.0087` n `25`; metal avg `-0.006` n `20`; unknown avg `0.046` n `785`
- 4h: commodity avg `-0.1063` n `12`; crypto_alt avg `0.4421` n `230`; crypto_major avg `0.2275` n `8`; equity avg `0.1175` n `112`; fx avg `-0.0015` n `6`; index avg `0.011` n `25`; metal avg `0.002` n `20`; unknown avg `0.0574` n `785`
- 24h: commodity avg `0.0857` n `12`; crypto_alt avg `1.2235` n `230`; crypto_major avg `0.2847` n `8`; equity avg `0.3575` n `112`; fx avg `-0.0109` n `6`; index avg `0.0271` n `25`; metal avg `0.0527` n `20`; unknown avg `0.3931` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
