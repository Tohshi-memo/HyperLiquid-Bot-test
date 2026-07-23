# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T17:07:26.936734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `-0.1132` n `230`; crypto_major avg `-0.0638` n `8`; equity avg `-0.1237` n `100`; fx avg `-0.002` n `6`; index avg `-0.026` n `25`; metal avg `0.0155` n `20`; unknown avg `0.0238` n `772`
- 1h: commodity avg `0.0858` n `12`; crypto_alt avg `-0.1675` n `230`; crypto_major avg `-0.217` n `8`; equity avg `0.1445` n `100`; fx avg `0.0015` n `6`; index avg `-0.0285` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.0033` n `772`
- 4h: commodity avg `0.157` n `12`; crypto_alt avg `-0.4332` n `230`; crypto_major avg `-0.9209` n `8`; equity avg `0.1452` n `100`; fx avg `-0.024` n `6`; index avg `-0.0641` n `25`; metal avg `0.0123` n `20`; unknown avg `-0.2172` n `772`
- 24h: commodity avg `1.047` n `12`; crypto_alt avg `-1.7742` n `230`; crypto_major avg `-2.3525` n `8`; equity avg `-1.5871` n `99`; fx avg `-0.0819` n `6`; index avg `-0.4147` n `25`; metal avg `-0.8131` n `20`; unknown avg `-0.1404` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0691`, n `666`, weak_sample_signal
