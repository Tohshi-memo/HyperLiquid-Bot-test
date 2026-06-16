# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T15:22:40.977411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `12`; crypto_alt avg `-0.1338` n `228`; crypto_major avg `-0.1988` n `8`; equity avg `-0.1337` n `77`; fx avg `-0.0036` n `6`; index avg `-0.1082` n `23`; metal avg `-0.0267` n `18`; unknown avg `0.6172` n `687`
- 1h: commodity avg `-0.1373` n `12`; crypto_alt avg `-0.4262` n `228`; crypto_major avg `-0.3339` n `8`; equity avg `-0.1515` n `77`; fx avg `0.0373` n `6`; index avg `-0.3402` n `23`; metal avg `-0.1413` n `18`; unknown avg `0.3937` n `687`
- 4h: commodity avg `-0.0616` n `12`; crypto_alt avg `-1.8696` n `228`; crypto_major avg `-1.566` n `8`; equity avg `-1.5727` n `77`; fx avg `0.0064` n `6`; index avg `-0.7404` n `23`; metal avg `-0.2404` n `18`; unknown avg `0.7401` n `687`
- 24h: commodity avg `-0.51` n `12`; crypto_alt avg `-2.1949` n `228`; crypto_major avg `-0.6579` n `8`; equity avg `-0.3942` n `77`; fx avg `-0.0422` n `6`; index avg `-0.5139` n `23`; metal avg `-0.4025` n `18`; unknown avg `0.5089` n `623`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0463`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
