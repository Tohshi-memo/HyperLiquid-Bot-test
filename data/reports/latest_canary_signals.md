# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T11:20:57.073849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `0.0509` n `230`; crypto_major avg `0.0104` n `8`; equity avg `0.0145` n `112`; fx avg `0.0052` n `6`; index avg `0.0016` n `25`; metal avg `0.0001` n `20`; unknown avg `-0.0067` n `785`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.047` n `230`; crypto_major avg `-0.0623` n `8`; equity avg `-0.0001` n `112`; fx avg `0.0049` n `6`; index avg `-0.0072` n `25`; metal avg `-0.0053` n `20`; unknown avg `0.0104` n `785`
- 4h: commodity avg `0.0592` n `12`; crypto_alt avg `0.1798` n `230`; crypto_major avg `0.0889` n `8`; equity avg `-0.0571` n `112`; fx avg `0.0059` n `6`; index avg `-0.0126` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.0227` n `785`
- 24h: commodity avg `0.23` n `12`; crypto_alt avg `1.213` n `230`; crypto_major avg `0.3299` n `8`; equity avg `0.3823` n `112`; fx avg `-0.0059` n `6`; index avg `0.0348` n `25`; metal avg `0.0275` n `20`; unknown avg `0.2558` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
