# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T12:37:28.889450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1524` n `12`; crypto_alt avg `0.3301` n `232`; crypto_major avg `0.1836` n `8`; equity avg `0.191` n `134`; fx avg `-0.0022` n `6`; index avg `0.0452` n `26`; metal avg `0.1137` n `20`; unknown avg `0.7266` n `791`
- 1h: commodity avg `-0.1865` n `12`; crypto_alt avg `-0.1119` n `232`; crypto_major avg `-0.0819` n `8`; equity avg `0.1783` n `134`; fx avg `-0.0028` n `6`; index avg `0.0389` n `26`; metal avg `-0.0611` n `20`; unknown avg `0.6739` n `789`
- 4h: commodity avg `-0.1893` n `12`; crypto_alt avg `-0.0323` n `232`; crypto_major avg `-0.2365` n `8`; equity avg `0.7696` n `134`; fx avg `0.0026` n `6`; index avg `0.1286` n `26`; metal avg `0.0512` n `20`; unknown avg `0.4845` n `789`
- 24h: commodity avg `0.0955` n `12`; crypto_alt avg `-0.3718` n `232`; crypto_major avg `-1.3897` n `8`; equity avg `0.2099` n `134`; fx avg `-0.1099` n `6`; index avg `0.0043` n `26`; metal avg `0.1369` n `20`; unknown avg `0.3448` n `710`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
