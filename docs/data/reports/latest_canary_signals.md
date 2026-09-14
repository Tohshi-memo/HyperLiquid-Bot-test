# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T17:52:44.012994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `0.2045` n `233`; crypto_major avg `0.2765` n `8`; equity avg `0.1089` n `136`; fx avg `-0.0014` n `6`; index avg `0.0195` n `27`; metal avg `0.012` n `20`; unknown avg `5.554` n `908`
- 1h: commodity avg `0.0806` n `12`; crypto_alt avg `0.1983` n `233`; crypto_major avg `0.1711` n `8`; equity avg `0.0856` n `136`; fx avg `0.0289` n `6`; index avg `-0.0135` n `27`; metal avg `-0.0824` n `20`; unknown avg `0.0495` n `906`
- 4h: commodity avg `-0.3231` n `12`; crypto_alt avg `1.0158` n `233`; crypto_major avg `1.0154` n `8`; equity avg `1.0568` n `136`; fx avg `-0.0172` n `6`; index avg `0.1222` n `27`; metal avg `0.1927` n `20`; unknown avg `0.4604` n `864`
- 24h: commodity avg `0.259` n `12`; crypto_alt avg `0.0992` n `233`; crypto_major avg `1.886` n `8`; equity avg `-0.0848` n `136`; fx avg `0.0658` n `6`; index avg `-0.0974` n `27`; metal avg `-0.3114` n `20`; unknown avg `1.0644` n `688`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
