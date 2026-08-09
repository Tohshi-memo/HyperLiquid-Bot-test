# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T07:37:28.447356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.1384` n `230`; crypto_major avg `0.0261` n `8`; equity avg `0.0253` n `112`; fx avg `0.0037` n `6`; index avg `0.0028` n `25`; metal avg `0.0236` n `20`; unknown avg `-0.0212` n `785`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.1286` n `230`; crypto_major avg `0.0102` n `8`; equity avg `-0.0157` n `112`; fx avg `-0.0036` n `6`; index avg `0.0063` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0195` n `785`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `0.0911` n `230`; crypto_major avg `0.1218` n `8`; equity avg `0.1082` n `112`; fx avg `-0.0192` n `6`; index avg `0.0035` n `25`; metal avg `0.0107` n `20`; unknown avg `-0.0382` n `752`
- 24h: commodity avg `0.2339` n `12`; crypto_alt avg `1.4274` n `230`; crypto_major avg `0.5331` n `8`; equity avg `0.6957` n `112`; fx avg `-0.0139` n `6`; index avg `0.0753` n `25`; metal avg `0.0361` n `20`; unknown avg `0.4162` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
