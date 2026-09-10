# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T13:52:30.184375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0535` n `12`; crypto_alt avg `0.0918` n `233`; crypto_major avg `0.1189` n `8`; equity avg `0.0313` n `134`; fx avg `-0.0086` n `6`; index avg `-0.0197` n `26`; metal avg `0.082` n `20`; unknown avg `0.1392` n `797`
- 1h: commodity avg `-0.0893` n `12`; crypto_alt avg `0.4313` n `233`; crypto_major avg `0.2441` n `8`; equity avg `0.3463` n `134`; fx avg `0.0025` n `6`; index avg `-0.039` n `26`; metal avg `0.1423` n `20`; unknown avg `0.562` n `795`
- 4h: commodity avg `0.3197` n `12`; crypto_alt avg `-0.615` n `233`; crypto_major avg `-1.1725` n `8`; equity avg `-1.0531` n `134`; fx avg `0.0152` n `6`; index avg `-0.2972` n `26`; metal avg `-0.6577` n `20`; unknown avg `0.362` n `789`
- 24h: commodity avg `0.4069` n `12`; crypto_alt avg `-5.0279` n `233`; crypto_major avg `-4.24` n `8`; equity avg `-2.3286` n `134`; fx avg `0.0884` n `6`; index avg `-0.3861` n `26`; metal avg `-0.9344` n `20`; unknown avg `0.714` n `675`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
