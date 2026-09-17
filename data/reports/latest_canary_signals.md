# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T00:52:05.663359+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0848` n `12`; crypto_alt avg `-0.0014` n `234`; crypto_major avg `-0.014` n `8`; equity avg `-0.0687` n `137`; fx avg `0.0044` n `6`; index avg `-0.0092` n `27`; metal avg `-0.0524` n `20`; unknown avg `0.5179` n `919`
- 1h: commodity avg `-0.1432` n `12`; crypto_alt avg `0.0729` n `234`; crypto_major avg `-0.0725` n `8`; equity avg `-0.0907` n `137`; fx avg `-0.0054` n `6`; index avg `-0.0439` n `27`; metal avg `-0.0179` n `20`; unknown avg `0.461` n `911`
- 4h: commodity avg `-0.1953` n `12`; crypto_alt avg `1.2206` n `234`; crypto_major avg `0.1924` n `8`; equity avg `0.7372` n `137`; fx avg `-0.0336` n `6`; index avg `0.1405` n `27`; metal avg `0.091` n `20`; unknown avg `0.9199` n `813`
- 24h: commodity avg `-0.7326` n `12`; crypto_alt avg `1.4875` n `234`; crypto_major avg `1.0115` n `8`; equity avg `1.512` n `137`; fx avg `-0.0497` n `6`; index avg `0.135` n `27`; metal avg `-0.1814` n `20`; unknown avg `0.5248` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
