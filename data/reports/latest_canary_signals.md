# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:54:54.074250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `-0.2499` n `230`; crypto_major avg `-0.08` n `8`; equity avg `0.0378` n `112`; fx avg `0.005` n `6`; index avg `0.0048` n `25`; metal avg `0.0128` n `20`; unknown avg `0.0896` n `785`
- 1h: commodity avg `0.2018` n `12`; crypto_alt avg `-0.4416` n `230`; crypto_major avg `-0.4688` n `8`; equity avg `-0.2368` n `112`; fx avg `0.0117` n `6`; index avg `-0.0508` n `25`; metal avg `-0.0793` n `20`; unknown avg `0.3431` n `785`
- 4h: commodity avg `0.3249` n `12`; crypto_alt avg `-0.2173` n `230`; crypto_major avg `-0.41` n `8`; equity avg `-0.164` n `112`; fx avg `0.0015` n `6`; index avg `-0.0593` n `25`; metal avg `-0.1349` n `20`; unknown avg `-0.1122` n `785`
- 24h: commodity avg `0.423` n `12`; crypto_alt avg `1.0558` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `-0.0293` n `112`; fx avg `0.002` n `6`; index avg `-0.0178` n `25`; metal avg `-0.058` n `20`; unknown avg `-0.3385` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
