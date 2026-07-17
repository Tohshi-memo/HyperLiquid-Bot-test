# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T11:07:24.138439+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `-0.0604` n `230`; crypto_major avg `-0.0408` n `8`; equity avg `-0.1144` n `96`; fx avg `0.0071` n `6`; index avg `-0.0109` n `25`; metal avg `-0.019` n `20`; unknown avg `-0.0631` n `769`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.1401` n `230`; crypto_major avg `-0.0757` n `8`; equity avg `0.2983` n `96`; fx avg `-0.0114` n `6`; index avg `0.0808` n `25`; metal avg `-0.1109` n `20`; unknown avg `-0.0918` n `769`
- 4h: commodity avg `0.256` n `12`; crypto_alt avg `0.0569` n `230`; crypto_major avg `0.2146` n `8`; equity avg `0.7342` n `96`; fx avg `0.0123` n `6`; index avg `0.1013` n `25`; metal avg `-0.0187` n `20`; unknown avg `0.0135` n `768`
- 24h: commodity avg `0.0919` n `12`; crypto_alt avg `-1.4103` n `230`; crypto_major avg `-2.4937` n `8`; equity avg `-4.2277` n `94`; fx avg `-0.0171` n `6`; index avg `-0.5628` n `25`; metal avg `-0.7106` n `20`; unknown avg `-0.4341` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
