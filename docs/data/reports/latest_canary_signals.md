# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T03:07:17.992574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-0.0918` n `228`; crypto_major avg `-0.0567` n `8`; equity avg `-0.0561` n `66`; fx avg `-0.0022` n `6`; index avg `-0.0779` n `23`; metal avg `-0.1477` n `18`; unknown avg `-0.0864` n `384`
- 1h: commodity avg `0.1745` n `12`; crypto_alt avg `-0.3367` n `228`; crypto_major avg `-0.2488` n `8`; equity avg `-0.3285` n `66`; fx avg `0.0036` n `6`; index avg `-0.2813` n `23`; metal avg `-0.5586` n `18`; unknown avg `-0.5749` n `384`
- 4h: commodity avg `-0.152` n `12`; crypto_alt avg `0.1105` n `228`; crypto_major avg `-0.292` n `8`; equity avg `-0.2217` n `66`; fx avg `-0.0509` n `6`; index avg `-0.3353` n `23`; metal avg `-0.6689` n `18`; unknown avg `-0.7202` n `383`
- 24h: commodity avg `0.6622` n `12`; crypto_alt avg `-0.942` n `228`; crypto_major avg `-0.6945` n `8`; equity avg `0.0348` n `66`; fx avg `-0.1434` n `6`; index avg `-0.6656` n `23`; metal avg `-2.4751` n `18`; unknown avg `0.9196` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
