# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T06:07:25.631239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.002` n `12`; crypto_alt avg `-0.1866` n `231`; crypto_major avg `-0.2109` n `8`; equity avg `-0.1023` n `127`; fx avg `-0.0062` n `6`; index avg `-0.0157` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.0441` n `775`
- 1h: commodity avg `-0.0649` n `12`; crypto_alt avg `0.0377` n `231`; crypto_major avg `0.3698` n `8`; equity avg `-0.18` n `127`; fx avg `-0.0042` n `6`; index avg `-0.0486` n `26`; metal avg `-0.1337` n `20`; unknown avg `0.0513` n `775`
- 4h: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.7483` n `231`; crypto_major avg `-0.3902` n `8`; equity avg `-0.1663` n `127`; fx avg `0.0172` n `6`; index avg `-0.0934` n `26`; metal avg `-0.2741` n `20`; unknown avg `0.0086` n `775`
- 24h: commodity avg `0.2758` n `12`; crypto_alt avg `-0.3011` n `231`; crypto_major avg `0.218` n `8`; equity avg `1.0855` n `127`; fx avg `-0.093` n `6`; index avg `0.1794` n `26`; metal avg `-0.4021` n `20`; unknown avg `0.2704` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
