# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T06:37:22.999772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `13`; crypto_alt avg `-0.5438` n `239`; crypto_major avg `-0.2865` n `8`; equity avg `-0.0397` n `162`; fx avg `0.0052` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0019` n `20`; unknown avg `0.2195` n `1258`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `0.0617` n `239`; crypto_major avg `0.3563` n `8`; equity avg `0.0935` n `162`; fx avg `0.0085` n `6`; index avg `0.0048` n `27`; metal avg `0.0145` n `20`; unknown avg `0.4329` n `1232`
- 4h: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.0289` n `239`; crypto_major avg `-0.2164` n `8`; equity avg `0.107` n `162`; fx avg `0.0054` n `6`; index avg `0.0017` n `27`; metal avg `0.0168` n `20`; unknown avg `0.7928` n `1214`
- 24h: commodity avg `-0.1623` n `13`; crypto_alt avg `-1.6334` n `239`; crypto_major avg `-2.3849` n `8`; equity avg `-2.3977` n `162`; fx avg `-0.1181` n `6`; index avg `-0.1773` n `27`; metal avg `-0.3906` n `20`; unknown avg `60.652` n `1020`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
