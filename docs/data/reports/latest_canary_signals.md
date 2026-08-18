# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T05:07:27.022815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `0.0519` n `230`; crypto_major avg `0.0602` n `8`; equity avg `-0.1118` n `114`; fx avg `-0.0116` n `6`; index avg `-0.0168` n `25`; metal avg `-0.0218` n `20`; unknown avg `-0.219` n `793`
- 1h: commodity avg `0.0144` n `12`; crypto_alt avg `0.1776` n `230`; crypto_major avg `0.1898` n `8`; equity avg `-0.0215` n `114`; fx avg `0.017` n `6`; index avg `-0.012` n `25`; metal avg `0.0144` n `20`; unknown avg `0.001` n `793`
- 4h: commodity avg `0.092` n `12`; crypto_alt avg `-0.9209` n `230`; crypto_major avg `-0.2768` n `8`; equity avg `-1.5738` n `114`; fx avg `0.0239` n `6`; index avg `-0.2837` n `25`; metal avg `-0.3442` n `20`; unknown avg `-0.0392` n `793`
- 24h: commodity avg `0.6825` n `12`; crypto_alt avg `-1.347` n `230`; crypto_major avg `0.1393` n `8`; equity avg `-1.1641` n `114`; fx avg `0.0022` n `6`; index avg `-0.3046` n `25`; metal avg `-0.1817` n `20`; unknown avg `0.0916` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
