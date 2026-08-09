# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T20:52:28.778883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0055` n `230`; crypto_major avg `-0.007` n `8`; equity avg `0.0375` n `112`; fx avg `-0.0025` n `6`; index avg `-0.0002` n `25`; metal avg `-0.0121` n `20`; unknown avg `-0.0497` n `785`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `0.017` n `230`; crypto_major avg `-0.0456` n `8`; equity avg `0.0437` n `112`; fx avg `0.0105` n `6`; index avg `-0.005` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.078` n `785`
- 4h: commodity avg `0.1332` n `12`; crypto_alt avg `0.2689` n `230`; crypto_major avg `-0.1831` n `8`; equity avg `0.1354` n `112`; fx avg `0.0041` n `6`; index avg `0.0164` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.3258` n `785`
- 24h: commodity avg `0.1146` n `12`; crypto_alt avg `1.4353` n `230`; crypto_major avg `0.1051` n `8`; equity avg `0.2555` n `112`; fx avg `0.0062` n `6`; index avg `0.0269` n `25`; metal avg `0.0955` n `20`; unknown avg `-0.3035` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
