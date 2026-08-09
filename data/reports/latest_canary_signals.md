# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T21:52:24.534417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `12`; crypto_alt avg `-0.0389` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `-0.0063` n `112`; fx avg `-0.0038` n `6`; index avg `0.0044` n `25`; metal avg `-0.0086` n `20`; unknown avg `0.1659` n `785`
- 1h: commodity avg `0.077` n `12`; crypto_alt avg `0.0026` n `230`; crypto_major avg `0.0359` n `8`; equity avg `-0.0003` n `112`; fx avg `-0.015` n `6`; index avg `0.0008` n `25`; metal avg `-0.0815` n `20`; unknown avg `0.0691` n `785`
- 4h: commodity avg `0.2329` n `12`; crypto_alt avg `0.2151` n `230`; crypto_major avg `-0.0042` n `8`; equity avg `0.0773` n `112`; fx avg `-0.0099` n `6`; index avg `0.0122` n `25`; metal avg `-0.0539` n `20`; unknown avg `-0.4011` n `785`
- 24h: commodity avg `0.235` n `12`; crypto_alt avg `1.3691` n `230`; crypto_major avg `0.1626` n `8`; equity avg `0.2151` n `112`; fx avg `-0.0051` n `6`; index avg `0.0357` n `25`; metal avg `0.0156` n `20`; unknown avg `-0.2796` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
