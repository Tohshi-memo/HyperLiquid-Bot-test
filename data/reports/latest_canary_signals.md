# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T03:52:30.876176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.0537` n `233`; crypto_major avg `-0.122` n `8`; equity avg `0.0018` n `136`; fx avg `-0.0099` n `6`; index avg `0.0053` n `27`; metal avg `-0.0318` n `20`; unknown avg `-0.0207` n `902`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.3794` n `233`; crypto_major avg `-0.3566` n `8`; equity avg `-0.2214` n `136`; fx avg `-0.0274` n `6`; index avg `-0.028` n `27`; metal avg `-0.0278` n `20`; unknown avg `0.2441` n `896`
- 4h: commodity avg `0.0967` n `12`; crypto_alt avg `-0.4623` n `233`; crypto_major avg `-0.3896` n `8`; equity avg `0.0932` n `136`; fx avg `0.0671` n `6`; index avg `0.0627` n `27`; metal avg `0.1515` n `20`; unknown avg `0.1686` n `890`
- 24h: commodity avg `-0.1051` n `12`; crypto_alt avg `-0.7437` n `233`; crypto_major avg `0.333` n `8`; equity avg `-0.132` n `136`; fx avg `0.0929` n `6`; index avg `-0.0125` n `27`; metal avg `-0.2378` n `20`; unknown avg `5.2033` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
