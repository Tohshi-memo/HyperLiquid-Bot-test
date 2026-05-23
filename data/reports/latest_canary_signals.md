# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T13:07:16.714929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0208` n `12`; crypto_alt avg `0.7295` n `228`; crypto_major avg `0.4454` n `8`; equity avg `0.1232` n `67`; fx avg `0.005` n `6`; index avg `0.0202` n `23`; metal avg `0.0047` n `18`; unknown avg `-0.1973` n `396`
- 1h: commodity avg `0.1669` n `12`; crypto_alt avg `0.9805` n `228`; crypto_major avg `0.5175` n `8`; equity avg `0.1585` n `67`; fx avg `0.0014` n `6`; index avg `0.1186` n `23`; metal avg `-0.0112` n `18`; unknown avg `-0.1707` n `396`
- 4h: commodity avg `0.1111` n `12`; crypto_alt avg `0.8001` n `228`; crypto_major avg `0.3991` n `8`; equity avg `0.2459` n `67`; fx avg `0.005` n `6`; index avg `0.1783` n `23`; metal avg `-0.0449` n `18`; unknown avg `-0.3963` n `396`
- 24h: commodity avg `0.6026` n `12`; crypto_alt avg `-5.8223` n `228`; crypto_major avg `-4.2856` n `8`; equity avg `-1.7808` n `67`; fx avg `0.076` n `6`; index avg `-0.1243` n `23`; metal avg `-0.6269` n `18`; unknown avg `-2.9597` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0648`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.062`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0582`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0558`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0552`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0528`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0504`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0473`, n `669`, weak_sample_signal
