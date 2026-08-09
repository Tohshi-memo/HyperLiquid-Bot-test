# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T12:07:27.866251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.0944` n `230`; crypto_major avg `-0.1083` n `8`; equity avg `-0.0395` n `112`; fx avg `0.0101` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0092` n `785`
- 1h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.0111` n `230`; crypto_major avg `-0.1554` n `8`; equity avg `-0.009` n `112`; fx avg `0.0077` n `6`; index avg `-0.0024` n `25`; metal avg `-0.0152` n `20`; unknown avg `-0.0247` n `785`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `-0.1358` n `230`; crypto_major avg `-0.2358` n `8`; equity avg `-0.073` n `112`; fx avg `0.0045` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.015` n `785`
- 24h: commodity avg `0.1295` n `12`; crypto_alt avg `1.0102` n `230`; crypto_major avg `0.1565` n `8`; equity avg `0.383` n `112`; fx avg `-0.0002` n `6`; index avg `0.0428` n `25`; metal avg `0.0276` n `20`; unknown avg `0.229` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0495`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
