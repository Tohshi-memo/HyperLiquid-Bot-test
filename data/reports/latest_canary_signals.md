# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T15:22:28.668790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `-0.0876` n `230`; crypto_major avg `-0.0844` n `8`; equity avg `0.011` n `114`; fx avg `0.0064` n `6`; index avg `-0.0059` n `25`; metal avg `0.0062` n `20`; unknown avg `0.0301` n `792`
- 1h: commodity avg `-0.0457` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `0.2615` n `8`; equity avg `0.5282` n `114`; fx avg `-0.005` n `6`; index avg `0.0772` n `25`; metal avg `0.0696` n `20`; unknown avg `0.0009` n `792`
- 4h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.1145` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `0.4358` n `114`; fx avg `0.0152` n `6`; index avg `0.0782` n `25`; metal avg `0.1067` n `20`; unknown avg `0.0208` n `792`
- 24h: commodity avg `-0.0569` n `12`; crypto_alt avg `-0.1862` n `230`; crypto_major avg `0.8219` n `8`; equity avg `1.6728` n `114`; fx avg `-0.0021` n `6`; index avg `0.2306` n `25`; metal avg `0.3182` n `20`; unknown avg `0.1368` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
