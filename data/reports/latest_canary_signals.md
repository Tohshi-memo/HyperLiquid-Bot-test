# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T18:37:26.796157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.0723` n `230`; crypto_major avg `0.0655` n `8`; equity avg `-0.027` n `96`; fx avg `0.0016` n `6`; index avg `0.0051` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0166` n `769`
- 1h: commodity avg `0.0303` n `12`; crypto_alt avg `-0.2069` n `230`; crypto_major avg `-0.2332` n `8`; equity avg `-0.7912` n `96`; fx avg `-0.0015` n `6`; index avg `-0.0945` n `25`; metal avg `-0.0142` n `20`; unknown avg `-0.0597` n `769`
- 4h: commodity avg `0.2407` n `12`; crypto_alt avg `0.3342` n `230`; crypto_major avg `0.4675` n `8`; equity avg `0.406` n `96`; fx avg `0.0857` n `6`; index avg `0.0622` n `25`; metal avg `0.1868` n `20`; unknown avg `0.2163` n `769`
- 24h: commodity avg `0.8095` n `12`; crypto_alt avg `-1.0264` n `230`; crypto_major avg `-1.1947` n `8`; equity avg `-1.1243` n `94`; fx avg `0.1048` n `6`; index avg `-0.2173` n `25`; metal avg `0.0312` n `20`; unknown avg `0.0107` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
