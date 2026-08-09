# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T13:37:30.266340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `0.0218` n `230`; crypto_major avg `0.0343` n `8`; equity avg `-0.0221` n `112`; fx avg `0.0044` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0445` n `785`
- 1h: commodity avg `0.0091` n `10`; crypto_alt avg `0.3097` n `228`; crypto_major avg `0.382` n `7`; equity avg `0.0673` n `108`; fx avg `-0.0173` n `6`; index avg `0.0031` n `24`; metal avg `0.0288` n `13`; unknown avg `0.0002` n `769`
- 4h: commodity avg `-0.1252` n `12`; crypto_alt avg `0.4555` n `230`; crypto_major avg `0.3746` n `8`; equity avg `0.0921` n `112`; fx avg `-0.0062` n `6`; index avg `-0.0005` n `25`; metal avg `0.0158` n `20`; unknown avg `0.1049` n `785`
- 24h: commodity avg `0.0891` n `12`; crypto_alt avg `1.3558` n `230`; crypto_major avg `0.446` n `8`; equity avg `0.3438` n `112`; fx avg `-0.0148` n `6`; index avg `0.0109` n `25`; metal avg `0.0556` n `20`; unknown avg `0.3825` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
