# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T05:37:25.811591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `13`; crypto_alt avg `-0.0136` n `239`; crypto_major avg `0.0974` n `8`; equity avg `0.0118` n `168`; fx avg `0.009` n `6`; index avg `0.0103` n `27`; metal avg `0.089` n `20`; unknown avg `3.0328` n `1265`
- 1h: commodity avg `0.0074` n `13`; crypto_alt avg `-0.1595` n `239`; crypto_major avg `0.1052` n `8`; equity avg `-0.1374` n `168`; fx avg `0.0042` n `6`; index avg `0.0016` n `27`; metal avg `0.0924` n `20`; unknown avg `229.4749` n `1259`
- 4h: commodity avg `0.1027` n `13`; crypto_alt avg `0.0125` n `239`; crypto_major avg `0.6506` n `8`; equity avg `0.2891` n `168`; fx avg `-0.0148` n `6`; index avg `0.032` n `27`; metal avg `0.5123` n `20`; unknown avg `-0.0723` n `1243`
- 24h: commodity avg `0.8303` n `13`; crypto_alt avg `3.2941` n `239`; crypto_major avg `3.5925` n `8`; equity avg `3.0516` n `168`; fx avg `0.0161` n `6`; index avg `0.2565` n `27`; metal avg `0.9618` n `20`; unknown avg `773.5805` n `1017`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
