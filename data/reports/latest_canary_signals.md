# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T20:52:29.700299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.2829` n `230`; crypto_major avg `-0.1987` n `8`; equity avg `-0.1902` n `102`; fx avg `0.0092` n `6`; index avg `-0.045` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.1006` n `778`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `-0.513` n `230`; crypto_major avg `-0.0335` n `8`; equity avg `-0.82` n `102`; fx avg `0.0077` n `6`; index avg `-0.1255` n `25`; metal avg `-0.0716` n `20`; unknown avg `-0.0112` n `778`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.9074` n `230`; crypto_major avg `-0.5235` n `8`; equity avg `-1.3577` n `102`; fx avg `0.084` n `6`; index avg `-0.2913` n `25`; metal avg `0.2945` n `20`; unknown avg `-0.564` n `778`
- 24h: commodity avg `1.3886` n `12`; crypto_alt avg `-3.2101` n `230`; crypto_major avg `-1.1213` n `8`; equity avg `-4.0699` n `102`; fx avg `0.0323` n `6`; index avg `-0.7108` n `25`; metal avg `0.1594` n `20`; unknown avg `-0.7602` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
