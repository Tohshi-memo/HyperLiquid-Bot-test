# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T14:37:28.711309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0886` n `12`; crypto_alt avg `0.0392` n `232`; crypto_major avg `-0.052` n `8`; equity avg `-0.0327` n `134`; fx avg `0.0011` n `6`; index avg `-0.0024` n `26`; metal avg `0.0096` n `20`; unknown avg `-0.0159` n `797`
- 1h: commodity avg `-0.1906` n `12`; crypto_alt avg `0.934` n `232`; crypto_major avg `0.7576` n `8`; equity avg `0.1209` n `134`; fx avg `0.0283` n `6`; index avg `-0.0573` n `26`; metal avg `0.0201` n `20`; unknown avg `0.1267` n `781`
- 4h: commodity avg `-0.3066` n `12`; crypto_alt avg `-0.6716` n `232`; crypto_major avg `-0.4573` n `8`; equity avg `0.4391` n `134`; fx avg `0.0169` n `6`; index avg `-0.0372` n `26`; metal avg `-0.0207` n `20`; unknown avg `-0.0948` n `775`
- 24h: commodity avg `-0.1952` n `12`; crypto_alt avg `-0.1844` n `232`; crypto_major avg `-0.5696` n `8`; equity avg `0.3894` n `134`; fx avg `-0.0806` n `6`; index avg `-0.0761` n `26`; metal avg `0.0254` n `20`; unknown avg `7061.6104` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
