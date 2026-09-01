# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T21:52:28.413815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0452` n `12`; crypto_alt avg `0.2703` n `232`; crypto_major avg `0.3` n `8`; equity avg `-0.0214` n `131`; fx avg `-0.0029` n `6`; index avg `0.0006` n `26`; metal avg `0.0283` n `20`; unknown avg `0.1152` n `793`
- 1h: commodity avg `-0.0481` n `12`; crypto_alt avg `0.0317` n `232`; crypto_major avg `-0.0661` n `8`; equity avg `-0.1558` n `131`; fx avg `-0.0113` n `6`; index avg `-0.0025` n `26`; metal avg `0.0679` n `20`; unknown avg `-0.1635` n `785`
- 4h: commodity avg `0.1563` n `12`; crypto_alt avg `-0.1846` n `232`; crypto_major avg `-0.3376` n `8`; equity avg `-0.1806` n `131`; fx avg `-0.0095` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0964` n `20`; unknown avg `2.0886` n `773`
- 24h: commodity avg `0.8374` n `12`; crypto_alt avg `-0.7957` n `232`; crypto_major avg `-2.3234` n `8`; equity avg `-2.1007` n `130`; fx avg `0.0301` n `6`; index avg `-0.3366` n `26`; metal avg `-0.8317` n `20`; unknown avg `-0.4013` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0318`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0304`, n `668`, weak_sample_signal
