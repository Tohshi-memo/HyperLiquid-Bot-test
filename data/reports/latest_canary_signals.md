# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T01:29:33.579440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.0151` n `228`; crypto_major avg `0.1238` n `8`; equity avg `0.0461` n `74`; fx avg `0.0097` n `6`; index avg `0.0602` n `23`; metal avg `0.47` n `18`; unknown avg `-0.2028` n `547`
- 1h: commodity avg `-0.3716` n `12`; crypto_alt avg `0.0268` n `228`; crypto_major avg `-0.144` n `8`; equity avg `-0.1559` n `74`; fx avg `0.0422` n `6`; index avg `-0.0592` n `23`; metal avg `-0.4792` n `18`; unknown avg `-0.1624` n `547`
- 4h: commodity avg `-0.0984` n `12`; crypto_alt avg `-0.1484` n `228`; crypto_major avg `-0.6439` n `8`; equity avg `-0.0207` n `74`; fx avg `-0.1012` n `6`; index avg `-0.0071` n `23`; metal avg `-1.014` n `18`; unknown avg `-0.4447` n `547`
- 24h: commodity avg `-0.6598` n `12`; crypto_alt avg `-0.0622` n `228`; crypto_major avg `-2.026` n `8`; equity avg `-1.6429` n `74`; fx avg `0.047` n `6`; index avg `-0.7002` n `23`; metal avg `-2.2766` n `18`; unknown avg `-0.4018` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.034`, n `668`, weak_sample_signal
