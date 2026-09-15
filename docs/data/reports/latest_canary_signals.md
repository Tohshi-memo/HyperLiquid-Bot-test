# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T11:52:30.289044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `0.1371` n `233`; crypto_major avg `0.0998` n `8`; equity avg `0.0091` n `136`; fx avg `-0.0042` n `6`; index avg `0.0082` n `27`; metal avg `0.0101` n `20`; unknown avg `0.0679` n `908`
- 1h: commodity avg `-0.0868` n `12`; crypto_alt avg `-0.3522` n `233`; crypto_major avg `-0.3013` n `8`; equity avg `0.0842` n `136`; fx avg `-0.0122` n `6`; index avg `0.04` n `27`; metal avg `0.0236` n `20`; unknown avg `1.33` n `906`
- 4h: commodity avg `-0.2786` n `12`; crypto_alt avg `-0.149` n `233`; crypto_major avg `0.1833` n `8`; equity avg `0.4879` n `136`; fx avg `-0.0033` n `6`; index avg `0.1436` n `27`; metal avg `0.2134` n `20`; unknown avg `1.2773` n `898`
- 24h: commodity avg `-0.2426` n `12`; crypto_alt avg `-1.539` n `233`; crypto_major avg `-0.8922` n `8`; equity avg `0.5953` n `136`; fx avg `0.1634` n `6`; index avg `0.0901` n `27`; metal avg `0.0902` n `20`; unknown avg `-0.4653` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
