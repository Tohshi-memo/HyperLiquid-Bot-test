# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T22:37:19.168092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.2541` n `228`; crypto_major avg `-0.1504` n `8`; equity avg `-0.067` n `67`; fx avg `0.0014` n `6`; index avg `0.0014` n `23`; metal avg `-0.0071` n `18`; unknown avg `-0.3586` n `386`
- 1h: commodity avg `0.1503` n `12`; crypto_alt avg `-0.6192` n `228`; crypto_major avg `-0.4097` n `8`; equity avg `-0.1402` n `67`; fx avg `0.0052` n `6`; index avg `-0.0568` n `23`; metal avg `0.0378` n `18`; unknown avg `-0.3999` n `386`
- 4h: commodity avg `0.4771` n `12`; crypto_alt avg `-1.8235` n `228`; crypto_major avg `-1.1613` n `8`; equity avg `-0.8174` n `67`; fx avg `0.0265` n `6`; index avg `-0.3199` n `23`; metal avg `-0.2254` n `18`; unknown avg `1.2761` n `386`
- 24h: commodity avg `-0.6051` n `12`; crypto_alt avg `-3.0325` n `228`; crypto_major avg `-2.159` n `8`; equity avg `-1.3719` n `67`; fx avg `0.144` n `6`; index avg `0.3993` n `23`; metal avg `-1.0377` n `18`; unknown avg `-1.4849` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0482`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
