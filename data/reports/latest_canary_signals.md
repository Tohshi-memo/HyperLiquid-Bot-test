# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T06:07:20.167282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.4494` n `228`; crypto_major avg `-0.267` n `8`; equity avg `0.0081` n `69`; fx avg `0.0197` n `6`; index avg `0.0382` n `23`; metal avg `-0.0832` n `18`; unknown avg `-0.1191` n `412`
- 1h: commodity avg `0.2517` n `12`; crypto_alt avg `-0.5024` n `228`; crypto_major avg `-0.3352` n `8`; equity avg `0.0046` n `69`; fx avg `-0.0597` n `6`; index avg `-0.2874` n `23`; metal avg `0.0743` n `18`; unknown avg `-0.0842` n `412`
- 4h: commodity avg `0.0298` n `12`; crypto_alt avg `-0.2788` n `228`; crypto_major avg `-0.1593` n `8`; equity avg `0.1755` n `69`; fx avg `-0.0655` n `6`; index avg `0.2196` n `23`; metal avg `-0.11` n `18`; unknown avg `-0.1266` n `412`
- 24h: commodity avg `1.0635` n `12`; crypto_alt avg `0.0669` n `228`; crypto_major avg `-0.9152` n `8`; equity avg `0.5355` n `69`; fx avg `-0.0412` n `6`; index avg `0.4714` n `23`; metal avg `0.3337` n `18`; unknown avg `1.5693` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2863`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2264`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
