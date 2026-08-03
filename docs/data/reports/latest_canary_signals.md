# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T23:37:27.082110+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0472` n `230`; crypto_major avg `-0.0665` n `8`; equity avg `0.0245` n `107`; fx avg `0.0121` n `6`; index avg `0.0124` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.0358` n `780`
- 1h: commodity avg `-0.0295` n `12`; crypto_alt avg `-0.0654` n `230`; crypto_major avg `0.0156` n `8`; equity avg `0.1029` n `107`; fx avg `0.0177` n `6`; index avg `0.0363` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1184` n `780`
- 4h: commodity avg `-0.0799` n `12`; crypto_alt avg `-0.3609` n `230`; crypto_major avg `-0.5225` n `8`; equity avg `0.4938` n `107`; fx avg `0.0649` n `6`; index avg `0.1069` n `25`; metal avg `0.0128` n `20`; unknown avg `0.2306` n `780`
- 24h: commodity avg `-0.0797` n `12`; crypto_alt avg `0.1445` n `230`; crypto_major avg `-0.1099` n `8`; equity avg `2.0739` n `107`; fx avg `-0.272` n `6`; index avg `0.1331` n `25`; metal avg `-0.2805` n `20`; unknown avg `0.0355` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
