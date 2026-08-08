# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T10:22:39.426036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0264` n `12`; crypto_alt avg `0.0275` n `230`; crypto_major avg `0.0334` n `8`; equity avg `0.0163` n `112`; fx avg `-0.0006` n `6`; index avg `0.0009` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0151` n `784`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `0.0671` n `230`; crypto_major avg `0.0431` n `8`; equity avg `0.0494` n `112`; fx avg `-0.0033` n `6`; index avg `-0.0105` n `25`; metal avg `0.0156` n `20`; unknown avg `1.2014` n `784`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `0.2719` n `230`; crypto_major avg `0.2465` n `8`; equity avg `0.1782` n `112`; fx avg `-0.0031` n `6`; index avg `0.0113` n `25`; metal avg `0.0386` n `20`; unknown avg `1.4181` n `784`
- 24h: commodity avg `0.0821` n `12`; crypto_alt avg `0.0209` n `230`; crypto_major avg `0.1789` n `8`; equity avg `0.9329` n `112`; fx avg `-0.0146` n `6`; index avg `0.0704` n `25`; metal avg `-0.0195` n `20`; unknown avg `1.2563` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
