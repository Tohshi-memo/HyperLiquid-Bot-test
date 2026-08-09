# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:03:21.205951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `-0.0248` n `8`; equity avg `0.0118` n `112`; fx avg `0.0033` n `6`; index avg `0.0009` n `25`; metal avg `0.0122` n `20`; unknown avg `-0.026` n `785`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0598` n `230`; crypto_major avg `0.1382` n `8`; equity avg `0.0209` n `112`; fx avg `0.0063` n `6`; index avg `0.0083` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0098` n `785`
- 4h: commodity avg `-0.1305` n `12`; crypto_alt avg `0.3423` n `230`; crypto_major avg `0.2292` n `8`; equity avg `0.122` n `112`; fx avg `-0.0007` n `6`; index avg `0.022` n `25`; metal avg `0.0242` n `20`; unknown avg `0.0082` n `785`
- 24h: commodity avg `0.0673` n `12`; crypto_alt avg `1.2948` n `230`; crypto_major avg `0.2998` n `8`; equity avg `0.3123` n `112`; fx avg `-0.0115` n `6`; index avg `0.0377` n `25`; metal avg `0.0606` n `20`; unknown avg `0.3827` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
