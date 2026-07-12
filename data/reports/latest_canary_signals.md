# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T15:52:28.542924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `0.0479` n `230`; crypto_major avg `0.1145` n `8`; equity avg `0.0117` n `92`; fx avg `-0.0008` n `6`; index avg `0.0175` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0041` n `765`
- 1h: commodity avg `0.0368` n `12`; crypto_alt avg `0.0946` n `230`; crypto_major avg `0.1606` n `8`; equity avg `0.0109` n `92`; fx avg `-0.0006` n `6`; index avg `0.032` n `25`; metal avg `0.0095` n `20`; unknown avg `0.0173` n `765`
- 4h: commodity avg `-0.0329` n `12`; crypto_alt avg `0.1964` n `230`; crypto_major avg `0.5421` n `8`; equity avg `0.0349` n `92`; fx avg `0.0007` n `6`; index avg `0.045` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.0641` n `765`
- 24h: commodity avg `0.4801` n `12`; crypto_alt avg `-0.8536` n `230`; crypto_major avg `-0.21` n `8`; equity avg `0.0396` n `92`; fx avg `0.0272` n `6`; index avg `-0.081` n `25`; metal avg `-0.0879` n `20`; unknown avg `0.1489` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
