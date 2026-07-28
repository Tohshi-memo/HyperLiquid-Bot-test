# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T17:07:39.837865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6686` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.1527` n `230`; crypto_major avg `-0.185` n `8`; equity avg `-0.1704` n `102`; fx avg `-0.0061` n `6`; index avg `-0.0299` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0234` n `774`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.0775` n `230`; crypto_major avg `0.1493` n `8`; equity avg `0.0699` n `102`; fx avg `0.0047` n `6`; index avg `-0.009` n `25`; metal avg `-0.0534` n `20`; unknown avg `-0.1107` n `774`
- 4h: commodity avg `-0.6768` n `12`; crypto_alt avg `0.3985` n `230`; crypto_major avg `1.0678` n `8`; equity avg `-0.6008` n `102`; fx avg `-0.0125` n `6`; index avg `0.0836` n `25`; metal avg `0.0984` n `20`; unknown avg `-0.1834` n `774`
- 24h: commodity avg `-1.1174` n `12`; crypto_alt avg `-1.7464` n `230`; crypto_major avg `-1.554` n `8`; equity avg `-2.2866` n `102`; fx avg `-0.0628` n `6`; index avg `-0.1184` n `25`; metal avg `-0.2789` n `20`; unknown avg `17.7781` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
