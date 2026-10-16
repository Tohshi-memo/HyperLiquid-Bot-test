# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T06:52:28.427413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1521` n `13`; crypto_alt avg `0.3349` n `236`; crypto_major avg `0.1445` n `8`; equity avg `0.0658` n `151`; fx avg `0.0046` n `6`; index avg `0.0104` n `26`; metal avg `0.0096` n `20`; unknown avg `0.7974` n `1136`
- 1h: commodity avg `0.1393` n `13`; crypto_alt avg `0.473` n `236`; crypto_major avg `0.2053` n `8`; equity avg `-0.3978` n `151`; fx avg `-0.0299` n `6`; index avg `-0.0768` n `26`; metal avg `-0.0212` n `20`; unknown avg `-0.0883` n `1110`
- 4h: commodity avg `0.1722` n `13`; crypto_alt avg `1.152` n `236`; crypto_major avg `0.5848` n `8`; equity avg `0.0704` n `151`; fx avg `-0.0749` n `6`; index avg `-0.006` n `26`; metal avg `0.0119` n `20`; unknown avg `2.6145` n `1102`
- 24h: commodity avg `0.0844` n `13`; crypto_alt avg `4.908` n `236`; crypto_major avg `2.5947` n `8`; equity avg `2.4255` n `151`; fx avg `0.0069` n `6`; index avg `0.3608` n `26`; metal avg `0.5154` n `20`; unknown avg `26.7411` n `904`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0923`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0629`, n `666`, weak_sample_signal
