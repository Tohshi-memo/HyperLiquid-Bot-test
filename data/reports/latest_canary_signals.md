# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T09:07:26.473250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0303` n `12`; crypto_alt avg `-0.0937` n `230`; crypto_major avg `-0.1943` n `8`; equity avg `0.0844` n `100`; fx avg `-0.0045` n `6`; index avg `0.011` n `25`; metal avg `0.0389` n `20`; unknown avg `0.0052` n `773`
- 1h: commodity avg `-0.2234` n `12`; crypto_alt avg `-0.2009` n `230`; crypto_major avg `-0.2751` n `8`; equity avg `0.1521` n `100`; fx avg `-0.0357` n `6`; index avg `0.0466` n `25`; metal avg `0.1135` n `20`; unknown avg `0.0287` n `772`
- 4h: commodity avg `-0.4573` n `12`; crypto_alt avg `0.0284` n `230`; crypto_major avg `0.137` n `8`; equity avg `0.2583` n `100`; fx avg `-0.0196` n `6`; index avg `0.066` n `25`; metal avg `0.2678` n `20`; unknown avg `0.053` n `756`
- 24h: commodity avg `-0.1897` n `12`; crypto_alt avg `-1.1292` n `230`; crypto_major avg `-1.5954` n `8`; equity avg `-1.9897` n `99`; fx avg `-0.1411` n `6`; index avg `-0.4893` n `25`; metal avg `-0.4445` n `20`; unknown avg `0.0779` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0997`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
