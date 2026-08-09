# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T13:22:24.322198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0803` n `230`; crypto_major avg `0.1387` n `8`; equity avg `0.0401` n `112`; fx avg `-0.0027` n `6`; index avg `-0.0009` n `25`; metal avg `0.0098` n `20`; unknown avg `-0.0552` n `785`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `0.3059` n `230`; crypto_major avg `0.2642` n `8`; equity avg `0.0872` n `112`; fx avg `-0.0129` n `6`; index avg `0.0115` n `25`; metal avg `0.028` n `20`; unknown avg `0.0003` n `785`
- 4h: commodity avg `-0.0805` n `12`; crypto_alt avg `0.4157` n `230`; crypto_major avg `0.3602` n `8`; equity avg `0.1129` n `112`; fx avg `-0.0113` n `6`; index avg `0.0011` n `25`; metal avg `0.0137` n `20`; unknown avg `0.021` n `785`
- 24h: commodity avg `0.0948` n `12`; crypto_alt avg `1.3597` n `230`; crypto_major avg `0.4177` n `8`; equity avg `0.3257` n `112`; fx avg `-0.0185` n `6`; index avg `0.0123` n `25`; metal avg `0.0491` n `20`; unknown avg `0.3589` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
