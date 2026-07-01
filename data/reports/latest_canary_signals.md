# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T17:52:29.957245+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.5031` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `0.0917` n `228`; crypto_major avg `0.0395` n `8`; equity avg `0.0349` n `88`; fx avg `-0.0034` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0488` n `20`; unknown avg `2.0459` n `763`
- 1h: commodity avg `-0.0881` n `12`; crypto_alt avg `0.1074` n `228`; crypto_major avg `0.3401` n `8`; equity avg `-0.1012` n `88`; fx avg `-0.0049` n `6`; index avg `-0.0315` n `25`; metal avg `-0.0313` n `20`; unknown avg `2.5348` n `763`
- 4h: commodity avg `-0.2022` n `12`; crypto_alt avg `0.8067` n `228`; crypto_major avg `1.2731` n `8`; equity avg `-0.0959` n `88`; fx avg `-0.0529` n `6`; index avg `-0.1462` n `25`; metal avg `-0.23` n `20`; unknown avg `2.8336` n `763`
- 24h: commodity avg `-0.5798` n `12`; crypto_alt avg `2.109` n `228`; crypto_major avg `2.2578` n `8`; equity avg `-0.5277` n `88`; fx avg `-0.0181` n `6`; index avg `-0.4612` n `25`; metal avg `0.236` n `20`; unknown avg `2.7727` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
