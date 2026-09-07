# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T15:52:24.719714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0657` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0948` n `12`; crypto_alt avg `-0.111` n `232`; crypto_major avg `-0.0193` n `8`; equity avg `-0.0345` n `134`; fx avg `-0.0061` n `6`; index avg `0.0064` n `26`; metal avg `0.0231` n `20`; unknown avg `0.5467` n `796`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `-1.3798` n `232`; crypto_major avg `-0.9664` n `8`; equity avg `-0.1691` n `134`; fx avg `-0.0033` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0165` n `20`; unknown avg `-0.3448` n `794`
- 4h: commodity avg `-0.0375` n `12`; crypto_alt avg `-0.8163` n `232`; crypto_major avg `-1.0365` n `8`; equity avg `-0.0987` n `134`; fx avg `-0.0439` n `6`; index avg `0.0292` n `26`; metal avg `0.1704` n `20`; unknown avg `6683.8902` n `748`
- 24h: commodity avg `0.133` n `12`; crypto_alt avg `-0.2551` n `232`; crypto_major avg `-1.3051` n `8`; equity avg `0.3283` n `134`; fx avg `-0.1143` n `6`; index avg `0.0543` n `26`; metal avg `0.0229` n `20`; unknown avg `-0.0477` n `681`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
