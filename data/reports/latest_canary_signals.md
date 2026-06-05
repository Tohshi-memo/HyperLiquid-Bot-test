# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T09:52:24.748163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `0.2969` n `228`; crypto_major avg `0.1907` n `8`; equity avg `0.1689` n `74`; fx avg `0.006` n `6`; index avg `0.0054` n `23`; metal avg `0.1104` n `18`; unknown avg `0.6291` n `424`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `1.5919` n `228`; crypto_major avg `1.0817` n `8`; equity avg `0.3787` n `74`; fx avg `-0.0053` n `6`; index avg `0.0866` n `23`; metal avg `0.2232` n `18`; unknown avg `0.4537` n `424`
- 4h: commodity avg `-0.241` n `12`; crypto_alt avg `-1.1129` n `228`; crypto_major avg `0.0019` n `8`; equity avg `0.2876` n `74`; fx avg `0.0452` n `6`; index avg `0.1272` n `23`; metal avg `0.3032` n `18`; unknown avg `0.7864` n `404`
- 24h: commodity avg `-0.0853` n `12`; crypto_alt avg `-3.2677` n `228`; crypto_major avg `-2.4031` n `8`; equity avg `-0.2783` n `73`; fx avg `0.0831` n `6`; index avg `-0.0479` n `23`; metal avg `-0.5263` n `18`; unknown avg `0.3499` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
