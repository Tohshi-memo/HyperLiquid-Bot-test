# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T03:07:30.820947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.1353` n `233`; crypto_major avg `-0.2435` n `8`; equity avg `-0.0946` n `136`; fx avg `-0.0116` n `6`; index avg `-0.0099` n `27`; metal avg `0.0043` n `20`; unknown avg `0.529` n `906`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `-0.1083` n `233`; crypto_major avg `-0.2474` n `8`; equity avg `-0.0274` n `136`; fx avg `0.0157` n `6`; index avg `0.0042` n `27`; metal avg `0.0728` n `20`; unknown avg `0.1752` n `906`
- 4h: commodity avg `0.1209` n `12`; crypto_alt avg `-0.3617` n `233`; crypto_major avg `-0.5513` n `8`; equity avg `0.1825` n `136`; fx avg `0.1092` n `6`; index avg `0.1001` n `27`; metal avg `0.1215` n `20`; unknown avg `0.3527` n `900`
- 24h: commodity avg `-0.0388` n `12`; crypto_alt avg `-0.6022` n `233`; crypto_major avg `0.3862` n `8`; equity avg `-0.1184` n `136`; fx avg `0.0871` n `6`; index avg `-0.0343` n `27`; metal avg `-0.2408` n `20`; unknown avg `5.2691` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
