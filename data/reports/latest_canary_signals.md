# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T02:22:27.535247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `12`; crypto_alt avg `0.0036` n `230`; crypto_major avg `-0.0036` n `8`; equity avg `0.1551` n `100`; fx avg `0.0212` n `6`; index avg `0.0247` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.0349` n `775`
- 1h: commodity avg `0.0408` n `12`; crypto_alt avg `0.1455` n `230`; crypto_major avg `0.0861` n `8`; equity avg `0.2404` n `100`; fx avg `0.0505` n `6`; index avg `0.0632` n `25`; metal avg `0.0268` n `20`; unknown avg `0.1034` n `775`
- 4h: commodity avg `0.2426` n `12`; crypto_alt avg `0.1063` n `230`; crypto_major avg `0.0058` n `8`; equity avg `-0.1883` n `100`; fx avg `0.1165` n `6`; index avg `-0.1151` n `25`; metal avg `0.0717` n `20`; unknown avg `-0.4186` n `775`
- 24h: commodity avg `-0.4614` n `12`; crypto_alt avg `1.4574` n `230`; crypto_major avg `1.2921` n `8`; equity avg `0.639` n `100`; fx avg `0.1669` n `6`; index avg `0.0549` n `25`; metal avg `0.451` n `20`; unknown avg `-0.009` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
