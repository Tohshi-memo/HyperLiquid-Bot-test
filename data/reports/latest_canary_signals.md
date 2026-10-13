# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T14:37:29.504647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1238` n `13`; crypto_alt avg `-0.1727` n `235`; crypto_major avg `-0.0873` n `8`; equity avg `-0.1067` n `151`; fx avg `-0.0015` n `6`; index avg `0.0246` n `26`; metal avg `-0.0175` n `20`; unknown avg `-0.1084` n `1121`
- 1h: commodity avg `0.3935` n `13`; crypto_alt avg `-0.0967` n `235`; crypto_major avg `0.1318` n `8`; equity avg `0.4016` n `151`; fx avg `-0.0089` n `6`; index avg `0.0279` n `26`; metal avg `-0.1946` n `20`; unknown avg `0.0816` n `1109`
- 4h: commodity avg `0.8551` n `13`; crypto_alt avg `0.5012` n `235`; crypto_major avg `0.5963` n `8`; equity avg `-0.2262` n `151`; fx avg `0.0513` n `6`; index avg `0.012` n `26`; metal avg `-0.2999` n `20`; unknown avg `0.6014` n `1095`
- 24h: crypto_alt avg `-2.364` n `227`; crypto_major avg `-0.9692` n `7`; metal avg `0.0288` n `1`; unknown avg `-0.2206` n `915`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1612`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1459`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1364`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
