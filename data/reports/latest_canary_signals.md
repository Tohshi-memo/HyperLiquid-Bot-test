# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T23:22:28.957131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `0.239` n `235`; crypto_major avg `0.1339` n `8`; equity avg `-0.0135` n `150`; fx avg `0.0022` n `6`; index avg `-0.0007` n `26`; metal avg `0.0333` n `20`; unknown avg `0.0138` n `1077`
- 1h: commodity avg `-0.0717` n `13`; crypto_alt avg `0.2824` n `235`; crypto_major avg `0.1505` n `8`; equity avg `-0.0591` n `150`; fx avg `0.0064` n `6`; index avg `-0.0103` n `26`; metal avg `0.0521` n `20`; unknown avg `-0.0606` n `1075`
- 4h: commodity avg `-0.1385` n `13`; crypto_alt avg `1.266` n `235`; crypto_major avg `0.9139` n `8`; equity avg `0.4591` n `150`; fx avg `0.0269` n `6`; index avg `0.0663` n `26`; metal avg `0.0966` n `20`; unknown avg `-0.0672` n `1007`
- 24h: commodity avg `0.5201` n `13`; crypto_alt avg `-2.8004` n `235`; crypto_major avg `-3.2611` n `8`; equity avg `-2.7797` n `150`; fx avg `0.0646` n `6`; index avg `-0.3678` n `26`; metal avg `0.0579` n `20`; unknown avg `6.3559` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
