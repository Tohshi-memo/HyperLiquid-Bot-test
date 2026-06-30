# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T23:07:31.343180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.0255` n `228`; crypto_major avg `0.0543` n `8`; equity avg `0.0613` n `88`; fx avg `0.0046` n `6`; index avg `-0.0023` n `23`; metal avg `0.0536` n `20`; unknown avg `1.1097` n `765`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.3255` n `228`; crypto_major avg `-0.2488` n `8`; equity avg `0.0179` n `88`; fx avg `-0.0122` n `6`; index avg `0.0008` n `23`; metal avg `-0.003` n `20`; unknown avg `0.6151` n `765`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.5713` n `228`; crypto_major avg `-0.3966` n `8`; equity avg `0.3938` n `88`; fx avg `-0.008` n `6`; index avg `-0.0427` n `23`; metal avg `-0.195` n `20`; unknown avg `2.291` n `763`
- 24h: commodity avg `0.1722` n `12`; crypto_alt avg `-2.1912` n `228`; crypto_major avg `-2.3115` n `8`; equity avg `1.2014` n `88`; fx avg `0.1024` n `6`; index avg `0.2517` n `23`; metal avg `-0.0479` n `20`; unknown avg `8.6783` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
