# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T06:52:28.156869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0821` n `12`; crypto_alt avg `0.4067` n `233`; crypto_major avg `0.3032` n `8`; equity avg `0.0491` n `134`; fx avg `0.0383` n `6`; index avg `0.0014` n `26`; metal avg `0.0428` n `20`; unknown avg `0.6293` n `795`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `0.011` n `233`; crypto_major avg `-0.0488` n `8`; equity avg `-0.0063` n `134`; fx avg `0.0201` n `6`; index avg `0.019` n `26`; metal avg `-0.0527` n `20`; unknown avg `0.8666` n `771`
- 4h: commodity avg `-0.0625` n `12`; crypto_alt avg `0.2693` n `233`; crypto_major avg `-0.008` n `8`; equity avg `0.1847` n `134`; fx avg `0.0553` n `6`; index avg `0.0908` n `26`; metal avg `-0.0007` n `20`; unknown avg `124.9422` n `765`
- 24h: commodity avg `-0.0855` n `12`; crypto_alt avg `-3.6264` n `233`; crypto_major avg `-2.5015` n `8`; equity avg `-1.0577` n `134`; fx avg `0.0789` n `6`; index avg `-0.1102` n `26`; metal avg `0.285` n `20`; unknown avg `0.9135` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
