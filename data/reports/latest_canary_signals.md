# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T20:07:30.134235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0729` n `13`; crypto_alt avg `-0.0517` n `236`; crypto_major avg `0.0313` n `8`; equity avg `-0.0097` n `151`; fx avg `-0.0045` n `6`; index avg `0.0102` n `26`; metal avg `0.0021` n `20`; unknown avg `0.0293` n `1177`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `0.2723` n `236`; crypto_major avg `0.2818` n `8`; equity avg `-0.0191` n `151`; fx avg `-0.002` n `6`; index avg `-0.0007` n `26`; metal avg `0.0135` n `20`; unknown avg `2.5021` n `1153`
- 4h: commodity avg `0.0392` n `13`; crypto_alt avg `0.7758` n `236`; crypto_major avg `0.5006` n `8`; equity avg `0.1853` n `151`; fx avg `-0.0194` n `6`; index avg `0.0189` n `26`; metal avg `0.0111` n `20`; unknown avg `3.6824` n `1105`
- 24h: commodity avg `0.1186` n `13`; crypto_alt avg `-0.8876` n `236`; crypto_major avg `-0.0181` n `8`; equity avg `-0.1372` n `151`; fx avg `-0.0346` n `6`; index avg `-0.01` n `26`; metal avg `-0.0186` n `20`; unknown avg `4.7522` n `999`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1716`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1479`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
