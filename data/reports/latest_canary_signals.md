# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T13:07:31.539888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0774` n `12`; crypto_alt avg `0.2005` n `232`; crypto_major avg `0.15` n `8`; equity avg `0.0695` n `132`; fx avg `-0.0185` n `6`; index avg `0.0097` n `26`; metal avg `0.0871` n `20`; unknown avg `0.1406` n `790`
- 1h: commodity avg `0.0721` n `12`; crypto_alt avg `0.1098` n `232`; crypto_major avg `0.0845` n `8`; equity avg `0.0456` n `132`; fx avg `-0.0041` n `6`; index avg `-0.0286` n `26`; metal avg `0.06` n `20`; unknown avg `0.3023` n `790`
- 4h: commodity avg `-0.1819` n `12`; crypto_alt avg `-0.7765` n `232`; crypto_major avg `-0.496` n `8`; equity avg `0.2864` n `132`; fx avg `-0.0824` n `6`; index avg `0.058` n `26`; metal avg `0.2832` n `20`; unknown avg `-0.1747` n `790`
- 24h: commodity avg `0.4425` n `12`; crypto_alt avg `-0.628` n `232`; crypto_major avg `-1.7255` n `8`; equity avg `-0.8088` n `131`; fx avg `-0.2784` n `6`; index avg `-0.1194` n `26`; metal avg `-0.0357` n `20`; unknown avg `0.2983` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
