# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T15:37:39.753290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.1185` n `233`; crypto_major avg `0.3313` n `8`; equity avg `0.0129` n `134`; fx avg `0.0033` n `6`; index avg `0.0117` n `26`; metal avg `0.1655` n `20`; unknown avg `2.5621` n `797`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `-1.2819` n `233`; crypto_major avg `-0.9071` n `8`; equity avg `-0.4387` n `134`; fx avg `0.0254` n `6`; index avg `-0.0849` n `26`; metal avg `-0.1586` n `20`; unknown avg `3.4043` n `795`
- 4h: commodity avg `0.0018` n `12`; crypto_alt avg `-1.2364` n `233`; crypto_major avg `-0.7067` n `8`; equity avg `0.1073` n `134`; fx avg `0.0216` n `6`; index avg `-0.0148` n `26`; metal avg `0.3336` n `20`; unknown avg `10.2026` n `766`
- 24h: commodity avg `0.5006` n `12`; crypto_alt avg `-1.7232` n `232`; crypto_major avg `-0.2293` n `8`; equity avg `-0.6768` n `134`; fx avg `-0.078` n `6`; index avg `-0.2215` n `26`; metal avg `0.2912` n `20`; unknown avg `10.0735` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
