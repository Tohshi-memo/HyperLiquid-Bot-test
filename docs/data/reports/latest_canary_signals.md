# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T09:22:33.059139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0316` n `12`; crypto_alt avg `0.0179` n `230`; crypto_major avg `-0.1044` n `8`; equity avg `-0.1018` n `114`; fx avg `-0.0032` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.0085` n `795`
- 1h: commodity avg `-0.0695` n `12`; crypto_alt avg `0.1115` n `230`; crypto_major avg `0.0468` n `8`; equity avg `-0.1385` n `114`; fx avg `-0.0108` n `6`; index avg `-0.0335` n `25`; metal avg `-0.0332` n `20`; unknown avg `-0.0144` n `795`
- 4h: commodity avg `-0.0931` n `12`; crypto_alt avg `0.3702` n `230`; crypto_major avg `-0.0092` n `8`; equity avg `-1.0336` n `114`; fx avg `0.0184` n `6`; index avg `-0.1745` n `25`; metal avg `-0.1235` n `20`; unknown avg `-0.0198` n `761`
- 24h: commodity avg `0.5766` n `12`; crypto_alt avg `-0.668` n `230`; crypto_major avg `0.2072` n `8`; equity avg `-2.6161` n `114`; fx avg `0.008` n `6`; index avg `-0.5427` n `25`; metal avg `-0.2856` n `20`; unknown avg `0.0211` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
