# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T14:17:38.927037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.0357` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `-0.0265` n `98`; fx avg `0.0208` n `6`; index avg `0.0096` n `25`; metal avg `0.0693` n `20`; unknown avg `0.001` n `771`
- 1h: commodity avg `0.0527` n `12`; crypto_alt avg `0.0449` n `230`; crypto_major avg `-0.0033` n `8`; equity avg `0.3461` n `98`; fx avg `0.0452` n `6`; index avg `0.0108` n `25`; metal avg `0.0876` n `20`; unknown avg `0.0601` n `771`
- 4h: commodity avg `0.2044` n `12`; crypto_alt avg `-0.0494` n `230`; crypto_major avg `-0.0427` n `8`; equity avg `0.3077` n `98`; fx avg `0.0159` n `6`; index avg `-0.0046` n `25`; metal avg `-0.1129` n `20`; unknown avg `0.139` n `771`
- 24h: commodity avg `0.5175` n `12`; crypto_alt avg `2.4631` n `230`; crypto_major avg `2.9944` n `8`; equity avg `2.6456` n `98`; fx avg `-0.0254` n `6`; index avg `0.2752` n `25`; metal avg `0.6906` n `20`; unknown avg `0.342` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0557`, n `666`, weak_sample_signal
