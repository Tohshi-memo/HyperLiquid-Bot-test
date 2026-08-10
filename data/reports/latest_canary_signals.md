# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T01:07:26.982590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `12`; crypto_alt avg `-0.065` n `230`; crypto_major avg `-0.0827` n `8`; equity avg `-0.2319` n `112`; fx avg `0.022` n `6`; index avg `-0.0222` n `25`; metal avg `-0.1078` n `20`; unknown avg `-0.0721` n `785`
- 1h: commodity avg `0.1121` n `12`; crypto_alt avg `0.2748` n `230`; crypto_major avg `0.0484` n `8`; equity avg `-0.4453` n `112`; fx avg `0.0611` n `6`; index avg `-0.0374` n `25`; metal avg `-0.1844` n `20`; unknown avg `-0.0034` n `785`
- 4h: commodity avg `0.3764` n `12`; crypto_alt avg `-0.68` n `230`; crypto_major avg `-0.7019` n `8`; equity avg `-0.5353` n `112`; fx avg `0.0729` n `6`; index avg `-0.0585` n `25`; metal avg `-0.3387` n `20`; unknown avg `0.3293` n `785`
- 24h: commodity avg `0.5032` n `12`; crypto_alt avg `0.6436` n `230`; crypto_major avg `-0.4568` n `8`; equity avg `-0.3807` n `112`; fx avg `0.0812` n `6`; index avg `-0.0358` n `25`; metal avg `-0.2725` n `20`; unknown avg `-0.387` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
