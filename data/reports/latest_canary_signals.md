# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T12:07:19.573208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2355` n `12`; crypto_alt avg `0.0337` n `228`; crypto_major avg `0.0014` n `8`; equity avg `-0.0937` n `66`; fx avg `0.0047` n `6`; index avg `-0.0659` n `23`; metal avg `-0.1412` n `18`; unknown avg `-0.1559` n `383`
- 1h: commodity avg `-0.108` n `12`; crypto_alt avg `-0.2948` n `228`; crypto_major avg `-0.3574` n `8`; equity avg `-0.3222` n `66`; fx avg `0.0029` n `6`; index avg `-0.1445` n `23`; metal avg `-0.2829` n `18`; unknown avg `-0.3705` n `383`
- 4h: commodity avg `0.0948` n `12`; crypto_alt avg `-1.0121` n `228`; crypto_major avg `-0.7051` n `8`; equity avg `-0.9802` n `66`; fx avg `-0.0574` n `6`; index avg `-0.5531` n `23`; metal avg `-0.3553` n `18`; unknown avg `-0.7173` n `383`
- 24h: commodity avg `1.132` n `12`; crypto_alt avg `-0.0569` n `228`; crypto_major avg `-0.3378` n `8`; equity avg `-2.1628` n `66`; fx avg `0.2242` n `6`; index avg `-0.9596` n `23`; metal avg `-0.7548` n `18`; unknown avg `0.4345` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
