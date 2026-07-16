# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T17:07:31.316982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0634` n `12`; crypto_alt avg `-0.1747` n `230`; crypto_major avg `-0.3432` n `8`; equity avg `-0.022` n `94`; fx avg `-0.0158` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0775` n `20`; unknown avg `-0.1679` n `768`
- 1h: commodity avg `-0.1619` n `12`; crypto_alt avg `-0.1898` n `230`; crypto_major avg `-0.5017` n `8`; equity avg `-0.2246` n `94`; fx avg `-0.0071` n `6`; index avg `-0.0787` n `25`; metal avg `-0.1193` n `20`; unknown avg `0.1591` n `768`
- 4h: commodity avg `-0.4971` n `12`; crypto_alt avg `0.3048` n `230`; crypto_major avg `-0.1888` n `8`; equity avg `-1.59` n `94`; fx avg `-0.0682` n `6`; index avg `-0.0767` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.1441` n `768`
- 24h: commodity avg `-0.2374` n `12`; crypto_alt avg `-0.5876` n `230`; crypto_major avg `-1.762` n `8`; equity avg `-2.7868` n `94`; fx avg `-0.1464` n `6`; index avg `-0.2714` n `25`; metal avg `-0.297` n `20`; unknown avg `-0.2462` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
