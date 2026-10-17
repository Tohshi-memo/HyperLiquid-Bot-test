# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T07:52:27.260406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `-0.0577` n `236`; crypto_major avg `-0.0711` n `8`; equity avg `-0.0404` n `151`; fx avg `-0.0024` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0` n `20`; unknown avg `-0.0148` n `1193`
- 1h: commodity avg `-0.0289` n `13`; crypto_alt avg `-0.2557` n `236`; crypto_major avg `0.0459` n `8`; equity avg `-0.0464` n `151`; fx avg `0.0008` n `6`; index avg `0.0039` n `26`; metal avg `-0.002` n `20`; unknown avg `0.0993` n `1191`
- 4h: commodity avg `-0.239` n `13`; crypto_alt avg `-0.4079` n `236`; crypto_major avg `0.0954` n `8`; equity avg `0.0439` n `151`; fx avg `-0.0017` n `6`; index avg `0.0322` n `26`; metal avg `-0.008` n `20`; unknown avg `0.6935` n `1167`
- 24h: commodity avg `0.2892` n `13`; crypto_alt avg `-1.9987` n `236`; crypto_major avg `-1.1829` n `8`; equity avg `-3.7687` n `151`; fx avg `0.0306` n `6`; index avg `-0.5616` n `26`; metal avg `-0.2699` n `20`; unknown avg `40.361` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1803`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1459`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.127`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
