# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T05:07:25.842492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `-0.055` n `228`; crypto_major avg `0.0055` n `8`; equity avg `0.0211` n `74`; fx avg `0.0074` n `6`; index avg `-0.0112` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.2142` n `645`
- 1h: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.4982` n `228`; crypto_major avg `-0.337` n `8`; equity avg `-0.0629` n `74`; fx avg `-0.0033` n `6`; index avg `-0.0237` n `23`; metal avg `0.0092` n `18`; unknown avg `-0.1367` n `645`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `-0.4151` n `228`; crypto_major avg `-0.3451` n `8`; equity avg `0.0394` n `74`; fx avg `0.0026` n `6`; index avg `-0.0553` n `23`; metal avg `-0.0018` n `18`; unknown avg `-1.4391` n `629`
- 24h: commodity avg `-0.7719` n `12`; crypto_alt avg `1.3627` n `228`; crypto_major avg `1.7485` n `8`; equity avg `0.7318` n `74`; fx avg `-0.0277` n `6`; index avg `0.2992` n `23`; metal avg `0.3264` n `18`; unknown avg `-1.2148` n `603`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
