# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:07:27.671511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.3437` n `230`; crypto_major avg `0.0739` n `8`; equity avg `0.0139` n `121`; fx avg `0.0007` n `6`; index avg `-0.0138` n `25`; metal avg `-0.025` n `20`; unknown avg `0.1628` n `793`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.4918` n `230`; crypto_major avg `0.3037` n `8`; equity avg `0.0543` n `121`; fx avg `-0.0013` n `6`; index avg `-0.0095` n `25`; metal avg `0.0121` n `20`; unknown avg `0.077` n `793`
- 4h: commodity avg `-0.0911` n `12`; crypto_alt avg `-0.3563` n `230`; crypto_major avg `-0.0849` n `8`; equity avg `-0.0285` n `121`; fx avg `0.0079` n `6`; index avg `-0.0499` n `25`; metal avg `0.0223` n `20`; unknown avg `0.1733` n `793`
- 24h: commodity avg `0.0632` n `12`; crypto_alt avg `6.9994` n `230`; crypto_major avg `4.8546` n `8`; equity avg `0.8982` n `121`; fx avg `-0.0788` n `6`; index avg `0.1122` n `25`; metal avg `0.5251` n `20`; unknown avg `1.0697` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
