# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T07:22:25.141050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.1536` n `236`; crypto_major avg `0.0017` n `8`; equity avg `-0.0704` n `151`; fx avg `0.0` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.0321` n `1193`
- 1h: commodity avg `-0.1945` n `13`; crypto_alt avg `-0.2896` n `236`; crypto_major avg `0.0452` n `8`; equity avg `-0.0707` n `151`; fx avg `-0.0045` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.0658` n `1189`
- 4h: commodity avg `-0.2548` n `13`; crypto_alt avg `-0.0456` n `236`; crypto_major avg `0.2353` n `8`; equity avg `0.0603` n `151`; fx avg `-0.002` n `6`; index avg `0.0254` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.6236` n `1167`
- 24h: commodity avg `0.2891` n `13`; crypto_alt avg `-2.3306` n `236`; crypto_major avg `-1.3489` n `8`; equity avg `-3.9929` n `151`; fx avg `0.0478` n `6`; index avg `-0.6139` n `26`; metal avg `-0.2889` n `20`; unknown avg `40.4643` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1797`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1391`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1204`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
