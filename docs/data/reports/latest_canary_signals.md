# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T06:52:32.969707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0885` n `12`; crypto_alt avg `0.1071` n `233`; crypto_major avg `0.2016` n `8`; equity avg `0.0021` n `136`; fx avg `0.004` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0382` n `20`; unknown avg `1.2129` n `894`
- 1h: commodity avg `0.0472` n `12`; crypto_alt avg `0.2788` n `233`; crypto_major avg `0.264` n `8`; equity avg `0.0781` n `136`; fx avg `0.0141` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0049` n `20`; unknown avg `0.5997` n `840`
- 4h: commodity avg `0.014` n `12`; crypto_alt avg `0.1229` n `233`; crypto_major avg `0.3361` n `8`; equity avg `-0.3246` n `136`; fx avg `-0.0105` n `6`; index avg `-0.0938` n `27`; metal avg `-0.0845` n `20`; unknown avg `0.6487` n `828`
- 24h: commodity avg `0.6148` n `12`; crypto_alt avg `-0.25` n `233`; crypto_major avg `0.4821` n `8`; equity avg `-1.2229` n `136`; fx avg `0.0715` n `6`; index avg `-0.3029` n `26`; metal avg `-0.1912` n `20`; unknown avg `1.1638` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
