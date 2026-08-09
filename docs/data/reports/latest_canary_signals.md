# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T09:22:28.550747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.0361` n `230`; crypto_major avg `-0.055` n `8`; equity avg `-0.0509` n `112`; fx avg `0.0007` n `6`; index avg `0.0094` n `25`; metal avg `0.0006` n `20`; unknown avg `0.0062` n `785`
- 1h: commodity avg `0.0367` n `12`; crypto_alt avg `-0.1371` n `230`; crypto_major avg `-0.1644` n `8`; equity avg `-0.0641` n `112`; fx avg `-0.0011` n `6`; index avg `-0.0058` n `25`; metal avg `0.0029` n `20`; unknown avg `0.0002` n `785`
- 4h: commodity avg `0.0227` n `12`; crypto_alt avg `0.0118` n `230`; crypto_major avg `0.0066` n `8`; equity avg `-0.0016` n `112`; fx avg `-0.0146` n `6`; index avg `-0.0135` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.0428` n `752`
- 24h: commodity avg `0.274` n `12`; crypto_alt avg `1.1816` n `230`; crypto_major avg `0.2132` n `8`; equity avg `0.5004` n `112`; fx avg `-0.0228` n `6`; index avg `0.0482` n `25`; metal avg `0.0162` n `20`; unknown avg `0.3325` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
