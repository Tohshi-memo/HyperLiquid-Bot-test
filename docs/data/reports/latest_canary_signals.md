# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T15:07:42.277127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `13`; crypto_alt avg `-0.7638` n `235`; crypto_major avg `-0.4721` n `8`; equity avg `-0.2751` n `150`; fx avg `-0.0048` n `6`; index avg `-0.0409` n `26`; metal avg `-0.0504` n `20`; unknown avg `-0.1775` n `1075`
- 1h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.6645` n `235`; crypto_major avg `-0.3521` n `8`; equity avg `-0.3046` n `150`; fx avg `0.0154` n `6`; index avg `-0.0513` n `26`; metal avg `-0.0814` n `20`; unknown avg `-0.4596` n `1051`
- 4h: commodity avg `-0.0779` n `13`; crypto_alt avg `-0.5121` n `235`; crypto_major avg `-0.6758` n `8`; equity avg `-0.2308` n `150`; fx avg `0.0453` n `6`; index avg `0.037` n `26`; metal avg `-0.0566` n `20`; unknown avg `-0.0193` n `1021`
- 24h: commodity avg `0.6218` n `13`; crypto_alt avg `0.5475` n `235`; crypto_major avg `-1.8813` n `8`; equity avg `-1.5376` n `150`; fx avg `0.0885` n `6`; index avg `-0.1298` n `26`; metal avg `-0.0775` n `20`; unknown avg `22.1991` n `990`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
