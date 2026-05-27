# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T04:37:19.661461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.2983` n `228`; crypto_major avg `-0.1187` n `8`; equity avg `-0.1645` n `67`; fx avg `0.007` n `6`; index avg `-0.0625` n `23`; metal avg `-0.0295` n `18`; unknown avg `1.6077` n `418`
- 1h: commodity avg `-0.1816` n `12`; crypto_alt avg `-0.9511` n `228`; crypto_major avg `-0.5655` n `8`; equity avg `-0.3036` n `67`; fx avg `-0.0106` n `6`; index avg `-0.0949` n `23`; metal avg `0.0166` n `18`; unknown avg `3.7423` n `418`
- 4h: commodity avg `-0.5465` n `12`; crypto_alt avg `-1.6866` n `228`; crypto_major avg `-0.6647` n `8`; equity avg `-0.3201` n `67`; fx avg `-0.0581` n `6`; index avg `-0.1599` n `23`; metal avg `-0.5927` n `18`; unknown avg `0.6289` n `418`
- 24h: commodity avg `-0.2899` n `12`; crypto_alt avg `-1.9092` n `228`; crypto_major avg `-1.0421` n `8`; equity avg `0.3333` n `67`; fx avg `-0.0648` n `6`; index avg `0.8258` n `23`; metal avg `-0.0857` n `18`; unknown avg `1.2408` n `397`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1715`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
