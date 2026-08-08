# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T19:52:23.467365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.0722` n `230`; crypto_major avg `0.0765` n `8`; equity avg `-0.0326` n `112`; fx avg `-0.0036` n `6`; index avg `-0.0028` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0465` n `784`
- 1h: commodity avg `0.0392` n `12`; crypto_alt avg `0.0579` n `230`; crypto_major avg `0.0575` n `8`; equity avg `0.1393` n `112`; fx avg `0.0023` n `6`; index avg `0.0106` n `25`; metal avg `0.0055` n `20`; unknown avg `0.3413` n `784`
- 4h: commodity avg `0.1457` n `12`; crypto_alt avg `0.2673` n `230`; crypto_major avg `-0.0822` n `8`; equity avg `0.2576` n `112`; fx avg `0.0106` n `6`; index avg `0.0042` n `25`; metal avg `0.0057` n `20`; unknown avg `0.4465` n `784`
- 24h: commodity avg `0.1716` n `12`; crypto_alt avg `1.4824` n `230`; crypto_major avg `1.1889` n `8`; equity avg `0.8195` n `112`; fx avg `0.034` n `6`; index avg `0.0255` n `25`; metal avg `0.0608` n `20`; unknown avg `0.1743` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
