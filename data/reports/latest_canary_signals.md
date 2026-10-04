# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T09:52:32.104757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.005` n `235`; crypto_major avg `0.0504` n `8`; equity avg `-0.0051` n `143`; fx avg `0.0` n `6`; index avg `0.0031` n `26`; metal avg `-0.002` n `20`; unknown avg `0.1035` n `1079`
- 1h: commodity avg `0.0009` n `13`; crypto_alt avg `-0.1166` n `235`; crypto_major avg `0.1942` n `8`; equity avg `0.0045` n `143`; fx avg `0.0032` n `6`; index avg `0.0061` n `26`; metal avg `-0.0095` n `20`; unknown avg `0.2785` n `1077`
- 4h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.0721` n `235`; crypto_major avg `0.4308` n `8`; equity avg `-0.0165` n `143`; fx avg `0.0064` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0068` n `20`; unknown avg `0.1238` n `1033`
- 24h: commodity avg `0.1156` n `13`; crypto_alt avg `2.0601` n `235`; crypto_major avg `1.378` n `8`; equity avg `0.2457` n `143`; fx avg `-0.027` n `6`; index avg `0.0254` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.1159` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
