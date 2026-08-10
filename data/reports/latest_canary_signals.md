# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T06:37:27.826152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `-0.0068` n `8`; equity avg `-0.0089` n `112`; fx avg `0.0233` n `6`; index avg `0.0009` n `25`; metal avg `0.0147` n `20`; unknown avg `0.006` n `785`
- 1h: commodity avg `-0.0764` n `12`; crypto_alt avg `0.1751` n `230`; crypto_major avg `0.0942` n `8`; equity avg `0.1613` n `112`; fx avg `0.061` n `6`; index avg `0.0182` n `25`; metal avg `0.0044` n `20`; unknown avg `57.2049` n `753`
- 4h: commodity avg `-0.1344` n `12`; crypto_alt avg `0.3942` n `230`; crypto_major avg `0.275` n `8`; equity avg `0.1663` n `112`; fx avg `0.075` n `6`; index avg `0.0525` n `25`; metal avg `0.144` n `20`; unknown avg `57.1366` n `753`
- 24h: commodity avg `0.2484` n `12`; crypto_alt avg `0.7661` n `230`; crypto_major avg `0.0812` n `8`; equity avg `-0.2228` n `112`; fx avg `0.1931` n `6`; index avg `0.0509` n `25`; metal avg `-0.0237` n `20`; unknown avg `56.8945` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
