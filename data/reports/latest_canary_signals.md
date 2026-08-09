# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T06:52:31.014914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.1481` n `230`; crypto_major avg `0.1129` n `8`; equity avg `-0.0219` n `112`; fx avg `0.0` n `6`; index avg `0.0042` n `25`; metal avg `-0.0069` n `20`; unknown avg `0.0197` n `785`
- 1h: commodity avg `-0.0389` n `12`; crypto_alt avg `0.3623` n `230`; crypto_major avg `0.2992` n `8`; equity avg `0.0767` n `112`; fx avg `-0.0068` n `6`; index avg `-0.0031` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0482` n `752`
- 4h: commodity avg `0.025` n `12`; crypto_alt avg `0.4425` n `230`; crypto_major avg `0.2734` n `8`; equity avg `0.0377` n `112`; fx avg `-0.0098` n `6`; index avg `-0.0013` n `25`; metal avg `0.0053` n `20`; unknown avg `0.0074` n `752`
- 24h: commodity avg `0.2423` n `12`; crypto_alt avg `1.6824` n `230`; crypto_major avg `0.5917` n `8`; equity avg `0.7123` n `112`; fx avg `-0.017` n `6`; index avg `0.0784` n `25`; metal avg `0.0388` n `20`; unknown avg `0.0262` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
