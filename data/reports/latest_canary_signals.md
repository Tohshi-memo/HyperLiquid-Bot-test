# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T19:52:26.578459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0266` n `12`; crypto_alt avg `-0.4476` n `233`; crypto_major avg `-0.4337` n `8`; equity avg `-0.1244` n `134`; fx avg `0.0015` n `6`; index avg `-0.0251` n `26`; metal avg `0.0039` n `20`; unknown avg `12.6913` n `797`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `-1.0945` n `233`; crypto_major avg `-0.8533` n `8`; equity avg `-0.1858` n `134`; fx avg `-0.0096` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0684` n `20`; unknown avg `14.0739` n `795`
- 4h: commodity avg `-0.0919` n `12`; crypto_alt avg `-0.7597` n `233`; crypto_major avg `-0.7374` n `8`; equity avg `-0.3229` n `134`; fx avg `0.0105` n `6`; index avg `-0.0249` n `26`; metal avg `-0.0813` n `20`; unknown avg `0.5571` n `789`
- 24h: commodity avg `0.135` n `12`; crypto_alt avg `-1.2507` n `233`; crypto_major avg `-0.6445` n `8`; equity avg `-0.2614` n `134`; fx avg `-0.0373` n `6`; index avg `-0.1457` n `26`; metal avg `0.496` n `20`; unknown avg `7.3396` n `699`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
