# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T14:49:26.547214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `0.0737` n `230`; crypto_major avg `0.0049` n `8`; equity avg `0.0327` n `112`; fx avg `0.0` n `6`; index avg `0.0011` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.0399` n `785`
- 1h: commodity avg `-0.0062` n `12`; crypto_alt avg `0.1259` n `230`; crypto_major avg `0.0836` n `8`; equity avg `0.0717` n `112`; fx avg `0.0059` n `6`; index avg `0.0005` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0189` n `785`
- 4h: commodity avg `-0.1406` n `12`; crypto_alt avg `0.464` n `230`; crypto_major avg `0.2763` n `8`; equity avg `0.1532` n `112`; fx avg `-0.0029` n `6`; index avg `0.0182` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0063` n `785`
- 24h: commodity avg `0.1828` n `12`; crypto_alt avg `1.0739` n `230`; crypto_major avg `-0.2236` n `8`; equity avg `0.4064` n `112`; fx avg `-0.0083` n `6`; index avg `0.0268` n `25`; metal avg `0.0552` n `20`; unknown avg `0.3646` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
