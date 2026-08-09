# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T23:43:27.358156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `-0.26` n `230`; crypto_major avg `-0.1346` n `8`; equity avg `-0.036` n `112`; fx avg `-0.0021` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0417` n `20`; unknown avg `0.0096` n `785`
- 1h: commodity avg `0.0673` n `12`; crypto_alt avg `-0.9167` n `230`; crypto_major avg `-0.5061` n `8`; equity avg `0.0305` n `112`; fx avg `-0.0015` n `6`; index avg `0.0079` n `25`; metal avg `0.0007` n `20`; unknown avg `0.2484` n `785`
- 4h: commodity avg `0.3757` n `12`; crypto_alt avg `-0.9838` n `230`; crypto_major avg `-0.8821` n `8`; equity avg `-0.1846` n `112`; fx avg `-0.0007` n `6`; index avg `-0.0557` n `25`; metal avg `-0.1592` n `20`; unknown avg `0.4092` n `785`
- 24h: commodity avg `0.493` n `12`; crypto_alt avg `0.3754` n `230`; crypto_major avg `-0.5041` n `8`; equity avg `-0.0082` n `112`; fx avg `0.0` n `6`; index avg `-0.023` n `25`; metal avg `-0.096` n `20`; unknown avg `-0.3961` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
