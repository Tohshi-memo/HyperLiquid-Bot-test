# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T11:52:32.710204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `12`; crypto_alt avg `0.0238` n `230`; crypto_major avg `0.0787` n `8`; equity avg `0.0654` n `98`; fx avg `0.0013` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.0085` n `771`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `0.0456` n `230`; crypto_major avg `0.2116` n `8`; equity avg `-0.0421` n `98`; fx avg `0.0027` n `6`; index avg `-0.0178` n `25`; metal avg `-0.0539` n `20`; unknown avg `-0.0643` n `771`
- 4h: commodity avg `0.3642` n `12`; crypto_alt avg `-0.1249` n `230`; crypto_major avg `0.0789` n `8`; equity avg `0.2835` n `98`; fx avg `0.0026` n `6`; index avg `0.0535` n `25`; metal avg `-0.0662` n `20`; unknown avg `0.0548` n `771`
- 24h: commodity avg `0.7817` n `12`; crypto_alt avg `1.6739` n `230`; crypto_major avg `1.7239` n `8`; equity avg `0.9438` n `98`; fx avg `-0.0726` n `6`; index avg `0.1274` n `25`; metal avg `0.4608` n `20`; unknown avg `0.1175` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.087`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
