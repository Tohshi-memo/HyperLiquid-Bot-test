# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T00:22:27.519894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0082` n `230`; crypto_major avg `0.0627` n `8`; equity avg `0.1179` n `114`; fx avg `-0.0121` n `6`; index avg `0.0347` n `25`; metal avg `0.0532` n `20`; unknown avg `-0.0841` n `793`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.0237` n `230`; crypto_major avg `0.1316` n `8`; equity avg `0.2041` n `114`; fx avg `-0.0196` n `6`; index avg `-0.0084` n `25`; metal avg `0.0883` n `20`; unknown avg `-0.1461` n `793`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `-0.1001` n `230`; crypto_major avg `0.384` n `8`; equity avg `0.2926` n `114`; fx avg `-0.0416` n `6`; index avg `-0.0055` n `25`; metal avg `0.074` n `20`; unknown avg `-0.1543` n `792`
- 24h: commodity avg `0.6156` n `12`; crypto_alt avg `0.5054` n `230`; crypto_major avg `1.7515` n `8`; equity avg `1.3113` n `114`; fx avg `-0.0036` n `6`; index avg `0.0297` n `25`; metal avg `0.2213` n `20`; unknown avg `0.3199` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
