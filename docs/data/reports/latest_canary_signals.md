# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T23:52:23.795083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0166` n `230`; crypto_major avg `0.0004` n `8`; equity avg `-0.0281` n `112`; fx avg `0.0069` n `6`; index avg `0.0022` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0098` n `784`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.0172` n `8`; equity avg `-0.0562` n `112`; fx avg `0.0024` n `6`; index avg `0.0104` n `25`; metal avg `0.0268` n `20`; unknown avg `-0.0006` n `784`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.0632` n `230`; crypto_major avg `-0.2164` n `8`; equity avg `-0.0384` n `112`; fx avg `0.0016` n `6`; index avg `0.0146` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.1462` n `784`
- 24h: commodity avg `0.1771` n `12`; crypto_alt avg `1.8154` n `230`; crypto_major avg `1.2161` n `8`; equity avg `0.5066` n `112`; fx avg `-0.0026` n `6`; index avg `0.051` n `25`; metal avg `0.0329` n `20`; unknown avg `0.2392` n `751`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
