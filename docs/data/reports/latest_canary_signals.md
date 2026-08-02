# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T10:37:30.734416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0488` n `12`; crypto_alt avg `-0.0407` n `230`; crypto_major avg `0.0064` n `8`; equity avg `-0.0218` n `102`; fx avg `-0.0102` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0257` n `782`
- 1h: commodity avg `0.206` n `12`; crypto_alt avg `-0.1813` n `230`; crypto_major avg `-0.2297` n `8`; equity avg `0.0309` n `102`; fx avg `-0.0077` n `6`; index avg `-0.008` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0861` n `782`
- 4h: commodity avg `0.1091` n `12`; crypto_alt avg `-0.1826` n `230`; crypto_major avg `-0.4618` n `8`; equity avg `0.0595` n `102`; fx avg `-0.0207` n `6`; index avg `-0.0068` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.1124` n `782`
- 24h: commodity avg `-1.023` n `12`; crypto_alt avg `0.4706` n `230`; crypto_major avg `0.2957` n `8`; equity avg `1.0083` n `102`; fx avg `-0.1564` n `6`; index avg `0.2145` n `25`; metal avg `0.2409` n `20`; unknown avg `0.2637` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
