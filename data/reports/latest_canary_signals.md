# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T12:37:31.112437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.242` n `12`; crypto_alt avg `-0.3317` n `233`; crypto_major avg `-0.2336` n `8`; equity avg `-0.1737` n `136`; fx avg `0.0138` n `6`; index avg `-0.0534` n `27`; metal avg `-0.0619` n `20`; unknown avg `86.777` n `888`
- 1h: commodity avg `0.224` n `12`; crypto_alt avg `-0.2164` n `233`; crypto_major avg `-0.1435` n `8`; equity avg `-0.4313` n `136`; fx avg `0.0032` n `6`; index avg `-0.0698` n `27`; metal avg `-0.0357` n `20`; unknown avg `4.3839` n `886`
- 4h: commodity avg `0.2119` n `12`; crypto_alt avg `-0.4078` n `233`; crypto_major avg `-0.0101` n `8`; equity avg `-0.5418` n `136`; fx avg `0.0376` n `6`; index avg `-0.0813` n `27`; metal avg `-0.2048` n `20`; unknown avg `4.9824` n `886`
- 24h: commodity avg `0.7665` n `12`; crypto_alt avg `-0.2695` n `233`; crypto_major avg `1.7175` n `8`; equity avg `-1.1546` n `136`; fx avg `0.0632` n `6`; index avg `-0.2505` n `27`; metal avg `-0.4789` n `20`; unknown avg `1.5022` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
