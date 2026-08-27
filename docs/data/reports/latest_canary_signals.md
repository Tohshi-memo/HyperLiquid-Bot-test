# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T11:52:32.525445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0674` n `12`; crypto_alt avg `-0.0357` n `231`; crypto_major avg `0.0004` n `8`; equity avg `-0.119` n `127`; fx avg `0.0056` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0286` n `20`; unknown avg `-0.0337` n `792`
- 1h: commodity avg `0.0661` n `12`; crypto_alt avg `0.0664` n `231`; crypto_major avg `-0.0643` n `8`; equity avg `-0.2438` n `127`; fx avg `-0.0186` n `6`; index avg `-0.0079` n `26`; metal avg `0.025` n `20`; unknown avg `-0.0427` n `792`
- 4h: commodity avg `0.3484` n `12`; crypto_alt avg `0.3371` n `231`; crypto_major avg `0.6632` n `8`; equity avg `0.0561` n `127`; fx avg `-0.0171` n `6`; index avg `0.006` n `26`; metal avg `-0.0144` n `20`; unknown avg `0.0008` n `792`
- 24h: commodity avg `0.4843` n `12`; crypto_alt avg `1.0432` n `231`; crypto_major avg `1.7072` n `8`; equity avg `1.7131` n `127`; fx avg `-0.109` n `6`; index avg `0.2636` n `26`; metal avg `-0.3281` n `20`; unknown avg `0.4766` n `775`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
