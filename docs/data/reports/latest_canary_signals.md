# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T02:22:16.466073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `0.0853` n `228`; crypto_major avg `0.0254` n `8`; equity avg `0.1628` n `66`; fx avg `-0.0229` n `6`; index avg `0.0552` n `23`; metal avg `0.074` n `18`; unknown avg `-0.4124` n `384`
- 1h: commodity avg `-0.1932` n `12`; crypto_alt avg `0.2184` n `228`; crypto_major avg `-0.0081` n `8`; equity avg `0.155` n `66`; fx avg `-0.087` n `6`; index avg `0.066` n `23`; metal avg `-0.202` n `18`; unknown avg `-0.32` n `384`
- 4h: commodity avg `-0.343` n `12`; crypto_alt avg `0.4071` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `0.1381` n `66`; fx avg `-0.0791` n `6`; index avg `-0.0054` n `23`; metal avg `0.1224` n `18`; unknown avg `-0.5895` n `383`
- 24h: commodity avg `0.6783` n `12`; crypto_alt avg `-0.879` n `228`; crypto_major avg `-0.5713` n `8`; equity avg `0.6858` n `66`; fx avg `-0.1591` n `6`; index avg `-0.2682` n `23`; metal avg `-2.0077` n `18`; unknown avg `1.0625` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
