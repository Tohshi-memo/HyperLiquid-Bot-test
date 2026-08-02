# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T08:37:23.813446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `-0.0591` n `230`; crypto_major avg `-0.1367` n `8`; equity avg `-0.0126` n `102`; fx avg `0.0013` n `6`; index avg `-0.017` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0041` n `782`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.1264` n `230`; crypto_major avg `-0.1884` n `8`; equity avg `0.2361` n `102`; fx avg `0.0043` n `6`; index avg `0.013` n `25`; metal avg `-0.0141` n `20`; unknown avg `-0.0641` n `782`
- 4h: commodity avg `0.0208` n `12`; crypto_alt avg `0.0776` n `230`; crypto_major avg `-0.2265` n `8`; equity avg `0.2011` n `102`; fx avg `-0.0506` n `6`; index avg `0.0575` n `25`; metal avg `0.0171` n `20`; unknown avg `0.2903` n `766`
- 24h: commodity avg `-1.1481` n `12`; crypto_alt avg `0.3044` n `230`; crypto_major avg `0.2877` n `8`; equity avg `0.9807` n `102`; fx avg `-0.1694` n `6`; index avg `0.2594` n `25`; metal avg `0.2433` n `20`; unknown avg `0.2683` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
