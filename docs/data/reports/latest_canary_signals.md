# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T06:37:28.105700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0285` n `12`; crypto_alt avg `0.0738` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.0264` n `112`; fx avg `0.0138` n `6`; index avg `0.0069` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0064` n `785`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.3074` n `230`; crypto_major avg `0.2015` n `8`; equity avg `0.0931` n `112`; fx avg `-0.0091` n `6`; index avg `-0.0073` n `25`; metal avg `0.0125` n `20`; unknown avg `0.0107` n `752`
- 4h: commodity avg `0.0383` n `12`; crypto_alt avg `0.2477` n `230`; crypto_major avg `0.0722` n `8`; equity avg `0.0734` n `112`; fx avg `-0.0087` n `6`; index avg `-0.0051` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0118` n `752`
- 24h: commodity avg `0.2412` n `12`; crypto_alt avg `1.5723` n `230`; crypto_major avg `0.5053` n `8`; equity avg `0.7528` n `112`; fx avg `-0.0175` n `6`; index avg `0.0731` n `25`; metal avg `0.0402` n `20`; unknown avg `-0.0102` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
