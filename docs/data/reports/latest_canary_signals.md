# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T00:37:32.058002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `12`; crypto_alt avg `0.1464` n `233`; crypto_major avg `0.2115` n `8`; equity avg `-0.106` n `136`; fx avg `0.0085` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0369` n `20`; unknown avg `0.4737` n `834`
- 1h: commodity avg `0.0836` n `12`; crypto_alt avg `0.1895` n `233`; crypto_major avg `0.2208` n `8`; equity avg `-0.2057` n `136`; fx avg `0.0252` n `6`; index avg `-0.109` n `27`; metal avg `-0.0293` n `20`; unknown avg `14.2534` n `812`
- 4h: commodity avg `0.4101` n `12`; crypto_alt avg `-1.4861` n `233`; crypto_major avg `-0.9746` n `8`; equity avg `-0.6646` n `136`; fx avg `0.0434` n `6`; index avg `-0.1805` n `27`; metal avg `-0.0652` n `20`; unknown avg `15.6279` n `788`
- 24h: commodity avg `0.7286` n `12`; crypto_alt avg `-1.6525` n `233`; crypto_major avg `-1.415` n `8`; equity avg `-1.7926` n `136`; fx avg `0.062` n `6`; index avg `-0.4102` n `26`; metal avg `-0.1495` n `20`; unknown avg `1.5194` n `696`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
