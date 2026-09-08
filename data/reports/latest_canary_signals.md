# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T14:22:27.014637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `0.496` n `232`; crypto_major avg `0.4536` n `8`; equity avg `0.2681` n `134`; fx avg `0.0117` n `6`; index avg `0.0133` n `26`; metal avg `-0.0242` n `20`; unknown avg `0.7073` n `797`
- 1h: commodity avg `-0.0745` n `12`; crypto_alt avg `0.1306` n `232`; crypto_major avg `0.2971` n `8`; equity avg `0.1385` n `134`; fx avg `-0.0017` n `6`; index avg `-0.1009` n `26`; metal avg `-0.1089` n `20`; unknown avg `0.5685` n `781`
- 4h: commodity avg `-0.2202` n `12`; crypto_alt avg `-0.8932` n `232`; crypto_major avg `-0.6179` n `8`; equity avg `0.3487` n `134`; fx avg `0.0171` n `6`; index avg `-0.0592` n `26`; metal avg `-0.076` n `20`; unknown avg `0.023` n `775`
- 24h: commodity avg `-0.078` n `12`; crypto_alt avg `-0.5304` n `232`; crypto_major avg `-0.8009` n `8`; equity avg `0.4229` n `134`; fx avg `-0.0934` n `6`; index avg `-0.0727` n `26`; metal avg `0.014` n `20`; unknown avg `7062.1096` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
