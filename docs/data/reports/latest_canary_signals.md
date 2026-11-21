# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T21:52:26.030020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.1317` n `239`; crypto_major avg `0.0408` n `8`; equity avg `0.0567` n `166`; fx avg `0.0184` n `6`; index avg `0.0053` n `27`; metal avg `-0.0071` n `20`; unknown avg `0.4334` n `1262`
- 1h: commodity avg `-0.0054` n `13`; crypto_alt avg `-0.1338` n `239`; crypto_major avg `-0.0547` n `8`; equity avg `0.0983` n `166`; fx avg `0.0049` n `6`; index avg `0.0103` n `27`; metal avg `-0.0197` n `20`; unknown avg `-0.3223` n `1242`
- 4h: commodity avg `0.0558` n `13`; crypto_alt avg `-0.1874` n `239`; crypto_major avg `0.2705` n `8`; equity avg `0.299` n `166`; fx avg `0.0243` n `6`; index avg `0.0737` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.6433` n `1176`
- 24h: commodity avg `0.0327` n `13`; crypto_alt avg `0.3155` n `239`; crypto_major avg `1.8665` n `8`; equity avg `0.9888` n `166`; fx avg `-0.0684` n `6`; index avg `0.2042` n `27`; metal avg `0.1586` n `20`; unknown avg `368.2218` n `1084`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
