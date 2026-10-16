# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T20:52:27.770707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `0.0604` n `236`; crypto_major avg `0.0876` n `8`; equity avg `0.0464` n `151`; fx avg `0.0004` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0075` n `20`; unknown avg `-0.0455` n `1193`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `0.3007` n `236`; crypto_major avg `0.3049` n `8`; equity avg `0.219` n `151`; fx avg `0.0072` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0076` n `20`; unknown avg `0.2904` n `1115`
- 4h: commodity avg `0.039` n `13`; crypto_alt avg `-0.046` n `236`; crypto_major avg `0.1783` n `8`; equity avg `-0.8965` n `151`; fx avg `0.0109` n `6`; index avg `-0.2053` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.4726` n `1115`
- 24h: commodity avg `0.3253` n `13`; crypto_alt avg `-1.7324` n `236`; crypto_major avg `-1.4891` n `8`; equity avg `-3.9295` n `151`; fx avg `0.0198` n `6`; index avg `-0.6749` n `26`; metal avg `-0.1102` n `20`; unknown avg `0.6832` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.162`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0759`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
