# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T01:37:25.683005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.0349` n `232`; crypto_major avg `0.0102` n `8`; equity avg `0.0284` n `133`; fx avg `-0.0159` n `6`; index avg `0.0118` n `26`; metal avg `0.0717` n `20`; unknown avg `0.2054` n `792`
- 1h: commodity avg `0.0394` n `12`; crypto_alt avg `0.5934` n `232`; crypto_major avg `0.4698` n `8`; equity avg `0.0968` n `133`; fx avg `-0.0827` n `6`; index avg `0.0294` n `26`; metal avg `0.13` n `20`; unknown avg `15.5946` n `790`
- 4h: commodity avg `0.1079` n `12`; crypto_alt avg `0.7109` n `232`; crypto_major avg `0.3217` n `8`; equity avg `0.0626` n `133`; fx avg `-0.0416` n `6`; index avg `-0.0045` n `26`; metal avg `0.0992` n `20`; unknown avg `15.0463` n `790`
- 24h: commodity avg `0.0004` n `12`; crypto_alt avg `1.0534` n `232`; crypto_major avg `0.5503` n `8`; equity avg `1.2807` n `133`; fx avg `-0.3607` n `6`; index avg `0.1373` n `26`; metal avg `0.7949` n `20`; unknown avg `-0.3295` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
