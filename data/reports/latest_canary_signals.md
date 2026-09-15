# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T02:37:25.945241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.0315` n `233`; crypto_major avg `-0.0194` n `8`; equity avg `0.0527` n `136`; fx avg `-0.0191` n `6`; index avg `0.0118` n `27`; metal avg `0.026` n `20`; unknown avg `0.2486` n `908`
- 1h: commodity avg `0.0854` n `12`; crypto_alt avg `-0.0681` n `233`; crypto_major avg `0.025` n `8`; equity avg `0.1541` n `136`; fx avg `0.0608` n `6`; index avg `0.0268` n `27`; metal avg `0.1025` n `20`; unknown avg `0.3886` n `906`
- 4h: commodity avg `0.1411` n `12`; crypto_alt avg `-0.4077` n `233`; crypto_major avg `-0.6461` n `8`; equity avg `0.3458` n `136`; fx avg `0.0955` n `6`; index avg `0.1133` n `27`; metal avg `0.0631` n `20`; unknown avg `0.7615` n `900`
- 24h: commodity avg `0.0418` n `12`; crypto_alt avg `-0.2971` n `233`; crypto_major avg `0.9912` n `8`; equity avg `-0.0261` n `136`; fx avg `0.0966` n `6`; index avg `-0.0256` n `27`; metal avg `-0.3691` n `20`; unknown avg `5.2199` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
