# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:04:44.068234+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `-0.0177` n `230`; crypto_major avg `-0.0346` n `8`; equity avg `-0.0061` n `112`; fx avg `-0.0014` n `6`; index avg `0.0015` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.3942` n `784`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.0331` n `230`; crypto_major avg `-0.1962` n `8`; equity avg `-0.0205` n `112`; fx avg `0.0048` n `6`; index avg `-0.001` n `25`; metal avg `-0.0047` n `20`; unknown avg `0.4339` n `784`
- 4h: commodity avg `0.1253` n `12`; crypto_alt avg `0.4014` n `230`; crypto_major avg `-0.1843` n `8`; equity avg `0.1608` n `112`; fx avg `0.0007` n `6`; index avg `0.0141` n `25`; metal avg `0.0215` n `20`; unknown avg `0.5326` n `784`
- 24h: commodity avg `0.0564` n `12`; crypto_alt avg `1.4328` n `230`; crypto_major avg `1.3372` n `8`; equity avg `0.683` n `112`; fx avg `0.0119` n `6`; index avg `0.0105` n `25`; metal avg `0.0293` n `20`; unknown avg `0.1752` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0467`, n `668`, weak_sample_signal
