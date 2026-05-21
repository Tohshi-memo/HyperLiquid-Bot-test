# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T10:22:20.879953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1572` n `12`; crypto_alt avg `0.1326` n `228`; crypto_major avg `0.0703` n `8`; equity avg `-0.0205` n `66`; fx avg `-0.0039` n `6`; index avg `0.0223` n `23`; metal avg `0.0875` n `18`; unknown avg `0.0604` n `386`
- 1h: commodity avg `-0.0618` n `12`; crypto_alt avg `-0.3462` n `228`; crypto_major avg `-0.4431` n `8`; equity avg `-0.1236` n `66`; fx avg `0.0092` n `6`; index avg `-0.0462` n `23`; metal avg `-0.0977` n `18`; unknown avg `0.29` n `386`
- 4h: commodity avg `-0.4105` n `12`; crypto_alt avg `0.2048` n `228`; crypto_major avg `0.247` n `8`; equity avg `0.0531` n `66`; fx avg `-0.0284` n `6`; index avg `0.0374` n `23`; metal avg `0.0563` n `18`; unknown avg `0.9097` n `385`
- 24h: commodity avg `-2.1586` n `12`; crypto_alt avg `2.3999` n `228`; crypto_major avg `2.822` n `8`; equity avg `1.5516` n `66`; fx avg `0.0879` n `6`; index avg `1.2756` n `23`; metal avg `0.3633` n `18`; unknown avg `6.8063` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
