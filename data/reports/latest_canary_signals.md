# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T05:37:19.290317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.58` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0702` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `-0.47` n `228`; crypto_major avg `-0.3678` n `8`; equity avg `0.0927` n `69`; fx avg `-0.0017` n `6`; index avg `0.0949` n `23`; metal avg `0.4659` n `18`; unknown avg `0.7565` n `422`
- 1h: commodity avg `-0.1868` n `12`; crypto_alt avg `-0.8423` n `228`; crypto_major avg `-0.8189` n `8`; equity avg `0.3698` n `69`; fx avg `-0.0326` n `6`; index avg `0.2513` n `23`; metal avg `0.6732` n `18`; unknown avg `2.0297` n `422`
- 4h: commodity avg `-0.3362` n `12`; crypto_alt avg `0.1318` n `228`; crypto_major avg `-0.229` n `8`; equity avg `0.9296` n `69`; fx avg `0.0183` n `6`; index avg `0.1934` n `23`; metal avg `0.8879` n `18`; unknown avg `0.7674` n `422`
- 24h: commodity avg `-0.8583` n `12`; crypto_alt avg `-0.5798` n `228`; crypto_major avg `-1.4548` n `8`; equity avg `0.0909` n `69`; fx avg `0.0218` n `6`; index avg `-0.2135` n `23`; metal avg `0.8521` n `18`; unknown avg `3.1773` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
