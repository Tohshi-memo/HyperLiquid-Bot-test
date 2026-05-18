# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T20:07:18.915597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0545` n `12`; crypto_alt avg `-0.0704` n `228`; crypto_major avg `-0.0735` n `8`; equity avg `-0.1051` n `66`; fx avg `0.0093` n `6`; index avg `-0.0193` n `23`; metal avg `0.0224` n `18`; unknown avg `0.1032` n `383`
- 1h: commodity avg `-0.321` n `12`; crypto_alt avg `0.8493` n `228`; crypto_major avg `0.8096` n `8`; equity avg `0.5757` n `66`; fx avg `-0.0279` n `6`; index avg `0.3064` n `23`; metal avg `0.0485` n `18`; unknown avg `0.0158` n `383`
- 4h: commodity avg `-0.3966` n `12`; crypto_alt avg `1.106` n `228`; crypto_major avg `1.2255` n `8`; equity avg `0.1981` n `66`; fx avg `-0.0285` n `6`; index avg `0.119` n `23`; metal avg `0.4048` n `18`; unknown avg `0.6311` n `383`
- 24h: commodity avg `0.6382` n `12`; crypto_alt avg `-1.8571` n `228`; crypto_major avg `-2.1587` n `8`; equity avg `-1.0045` n `66`; fx avg `0.1728` n `6`; index avg `-0.4033` n `23`; metal avg `0.9661` n `18`; unknown avg `-0.4689` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
