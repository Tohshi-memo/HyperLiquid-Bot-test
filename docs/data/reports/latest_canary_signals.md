# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T03:09:07.011382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `12`; crypto_alt avg `-0.2666` n `230`; crypto_major avg `-0.0031` n `8`; equity avg `-0.0542` n `114`; fx avg `-0.01` n `6`; index avg `-0.0107` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0326` n `793`
- 1h: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.7947` n `230`; crypto_major avg `-0.2165` n `8`; equity avg `-0.7732` n `114`; fx avg `-0.0426` n `6`; index avg `-0.1373` n `25`; metal avg `-0.0286` n `20`; unknown avg `0.1264` n `793`
- 4h: commodity avg `0.0053` n `12`; crypto_alt avg `-1.0446` n `230`; crypto_major avg `-0.3726` n `8`; equity avg `-1.6014` n `114`; fx avg `-0.0681` n `6`; index avg `-0.2602` n `25`; metal avg `-0.1602` n `20`; unknown avg `0.075` n `793`
- 24h: commodity avg `0.6051` n `12`; crypto_alt avg `-1.5004` n `230`; crypto_major avg `-0.1044` n `8`; equity avg `-1.076` n `114`; fx avg `-0.0407` n `6`; index avg `-0.2409` n `25`; metal avg `-0.1924` n `20`; unknown avg `-0.0174` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
