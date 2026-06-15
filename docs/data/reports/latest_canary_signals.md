# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T21:37:39.331780+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.2243` n `8`; equity avg `0.0793` n `77`; fx avg `-0.0072` n `6`; index avg `0.0258` n `23`; metal avg `-0.0008` n `18`; unknown avg `-0.0521` n `687`
- 1h: commodity avg `-0.1037` n `12`; crypto_alt avg `-0.0888` n `228`; crypto_major avg `-0.3279` n `8`; equity avg `-0.0015` n `77`; fx avg `0.0203` n `6`; index avg `0.0188` n `23`; metal avg `0.0115` n `18`; unknown avg `-0.0196` n `679`
- 4h: commodity avg `0.2978` n `12`; crypto_alt avg `-1.1079` n `228`; crypto_major avg `-0.8403` n `8`; equity avg `-0.0947` n `77`; fx avg `-0.0248` n `6`; index avg `-0.0548` n `23`; metal avg `-0.1672` n `18`; unknown avg `-0.1038` n `679`
- 24h: commodity avg `0.3057` n `12`; crypto_alt avg `2.593` n `228`; crypto_major avg `4.3388` n `8`; equity avg `2.1439` n `76`; fx avg `-0.033` n `6`; index avg `1.1684` n `23`; metal avg `1.5567` n `18`; unknown avg `2.6589` n `519`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
