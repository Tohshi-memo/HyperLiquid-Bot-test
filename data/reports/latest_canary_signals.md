# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T07:37:15.508867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1474` n `12`; crypto_alt avg `0.2651` n `228`; crypto_major avg `0.1624` n `8`; equity avg `0.1573` n `66`; fx avg `0.0134` n `6`; index avg `0.0132` n `23`; metal avg `-0.0504` n `18`; unknown avg `0.5946` n `385`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.2687` n `228`; crypto_major avg `0.258` n `8`; equity avg `-0.309` n `66`; fx avg `-0.0474` n `6`; index avg `-0.1673` n `23`; metal avg `-0.1815` n `18`; unknown avg `0.2622` n `385`
- 4h: commodity avg `0.1204` n `12`; crypto_alt avg `-0.2994` n `228`; crypto_major avg `-0.1174` n `8`; equity avg `-0.2532` n `66`; fx avg `-0.0121` n `6`; index avg `-0.1722` n `23`; metal avg `-0.4915` n `18`; unknown avg `0.63` n `374`
- 24h: commodity avg `-1.8049` n `12`; crypto_alt avg `2.3586` n `228`; crypto_major avg `2.9796` n `8`; equity avg `1.525` n `66`; fx avg `0.0406` n `6`; index avg `1.2851` n `23`; metal avg `0.0676` n `18`; unknown avg `5.2514` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
