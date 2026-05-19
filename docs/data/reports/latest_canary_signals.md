# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T07:52:21.514098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1191` n `12`; crypto_alt avg `0.1118` n `228`; crypto_major avg `0.0522` n `8`; equity avg `0.194` n `66`; fx avg `-0.0053` n `6`; index avg `0.1314` n `23`; metal avg `0.2135` n `18`; unknown avg `0.0422` n `383`
- 1h: commodity avg `-0.1626` n `12`; crypto_alt avg `0.1773` n `228`; crypto_major avg `0.3055` n `8`; equity avg `0.3895` n `66`; fx avg `0.0214` n `6`; index avg `0.15` n `23`; metal avg `0.0637` n `18`; unknown avg `0.0567` n `383`
- 4h: commodity avg `0.1922` n `12`; crypto_alt avg `0.4125` n `228`; crypto_major avg `0.2976` n `8`; equity avg `0.4212` n `66`; fx avg `0.0149` n `6`; index avg `0.1793` n `23`; metal avg `0.0303` n `18`; unknown avg `0.3094` n `363`
- 24h: commodity avg `0.594` n `12`; crypto_alt avg `2.2516` n `228`; crypto_major avg `1.2524` n `8`; equity avg `-0.4764` n `66`; fx avg `0.3149` n `6`; index avg `-0.1381` n `23`; metal avg `0.2419` n `18`; unknown avg `1.0307` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
