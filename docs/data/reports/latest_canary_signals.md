# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T11:54:43.661217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.1521` n `233`; crypto_major avg `0.0862` n `8`; equity avg `-0.0054` n `136`; fx avg `0.0053` n `6`; index avg `0.0045` n `27`; metal avg `0.0085` n `20`; unknown avg `0.0386` n `908`
- 1h: commodity avg `-0.1026` n `12`; crypto_alt avg `-0.3373` n `233`; crypto_major avg `-0.3148` n `8`; equity avg `0.0695` n `136`; fx avg `-0.0027` n `6`; index avg `0.0362` n `27`; metal avg `0.022` n `20`; unknown avg `0.5771` n `906`
- 4h: commodity avg `-0.2943` n `12`; crypto_alt avg `-0.1339` n `233`; crypto_major avg `0.1697` n `8`; equity avg `0.4731` n `136`; fx avg `0.0062` n `6`; index avg `0.1398` n `27`; metal avg `0.2118` n `20`; unknown avg `1.2553` n `898`
- 24h: commodity avg `-0.2583` n `12`; crypto_alt avg `-1.5235` n `233`; crypto_major avg `-0.9055` n `8`; equity avg `0.5805` n `136`; fx avg `0.173` n `6`; index avg `0.0863` n `27`; metal avg `0.0886` n `20`; unknown avg `-0.4055` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
