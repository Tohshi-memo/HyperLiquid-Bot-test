# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T07:52:25.540604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `12`; crypto_alt avg `-0.0792` n `230`; crypto_major avg `-0.0135` n `8`; equity avg `-0.0349` n `112`; fx avg `-0.002` n `6`; index avg `0.0006` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0205` n `785`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `-0.3546` n `230`; crypto_major avg `-0.116` n `8`; equity avg `-0.0284` n `112`; fx avg `-0.0055` n `6`; index avg `0.0027` n `25`; metal avg `0.0224` n `20`; unknown avg `-0.0183` n `785`
- 4h: commodity avg `0.0274` n `12`; crypto_alt avg `-0.0197` n `230`; crypto_major avg `0.1369` n `8`; equity avg `0.0516` n `112`; fx avg `-0.016` n `6`; index avg `0.0011` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0394` n `752`
- 24h: commodity avg `0.2404` n `12`; crypto_alt avg `1.3219` n `230`; crypto_major avg `0.5514` n `8`; equity avg `0.6412` n `112`; fx avg `-0.015` n `6`; index avg `0.0796` n `25`; metal avg `0.0338` n `20`; unknown avg `0.4783` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
