# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T08:52:29.592709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `13`; crypto_alt avg `-0.0052` n `236`; crypto_major avg `0.0693` n `8`; equity avg `0.0325` n `151`; fx avg `0.0213` n `6`; index avg `0.0119` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0362` n `1136`
- 1h: commodity avg `-0.1585` n `13`; crypto_alt avg `0.1334` n `236`; crypto_major avg `0.2443` n `8`; equity avg `0.1378` n `151`; fx avg `0.0031` n `6`; index avg `0.0362` n `26`; metal avg `-0.0119` n `20`; unknown avg `-0.0271` n `1066`
- 4h: commodity avg `-0.1084` n `13`; crypto_alt avg `0.6585` n `236`; crypto_major avg `0.6537` n `8`; equity avg `-0.4902` n `151`; fx avg `-0.078` n `6`; index avg `-0.0751` n `26`; metal avg `0.0063` n `20`; unknown avg `0.1973` n `1048`
- 24h: commodity avg `-0.1721` n `13`; crypto_alt avg `3.9006` n `236`; crypto_major avg `2.0416` n `8`; equity avg `2.5458` n `151`; fx avg `-0.0136` n `6`; index avg `0.328` n `26`; metal avg `0.3959` n `20`; unknown avg `27.3561` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0967`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
