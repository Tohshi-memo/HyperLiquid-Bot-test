# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T06:22:35.122172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `0.0141` n `230`; crypto_major avg `0.051` n `8`; equity avg `0.0115` n `112`; fx avg `-0.0206` n `6`; index avg `-0.0146` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.0016` n `784`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.1257` n `230`; crypto_major avg `0.1069` n `8`; equity avg `0.0817` n `112`; fx avg `-0.0238` n `6`; index avg `-0.0197` n `25`; metal avg `0.0132` n `20`; unknown avg `0.0011` n `752`
- 4h: commodity avg `0.0611` n `12`; crypto_alt avg `0.1202` n `230`; crypto_major avg `-0.004` n `8`; equity avg `0.0407` n `112`; fx avg `-0.0224` n `6`; index avg `-0.0129` n `25`; metal avg `0.0208` n `20`; unknown avg `-0.0214` n `752`
- 24h: commodity avg `0.2779` n `12`; crypto_alt avg `1.5127` n `230`; crypto_major avg `0.5174` n `8`; equity avg `0.7157` n `112`; fx avg `-0.0318` n `6`; index avg `0.0638` n `25`; metal avg `0.0318` n `20`; unknown avg `0.0077` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
