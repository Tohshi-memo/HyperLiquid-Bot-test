# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T07:06:35.331704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `-0.0524` n `233`; crypto_major avg `0.0652` n `8`; equity avg `-0.1417` n `136`; fx avg `-0.0164` n `6`; index avg `-0.0246` n `27`; metal avg `-0.037` n `20`; unknown avg `0.175` n `868`
- 1h: commodity avg `0.1268` n `12`; crypto_alt avg `-0.2771` n `233`; crypto_major avg `-0.1954` n `8`; equity avg `-0.2112` n `136`; fx avg `0.0199` n `6`; index avg `-0.063` n `27`; metal avg `-0.094` n `20`; unknown avg `0.595` n `864`
- 4h: commodity avg `0.0258` n `12`; crypto_alt avg `0.0713` n `233`; crypto_major avg `0.3395` n `8`; equity avg `-0.4212` n `136`; fx avg `-0.0262` n `6`; index avg `-0.1091` n `27`; metal avg `-0.1066` n `20`; unknown avg `0.6135` n `828`
- 24h: commodity avg `0.6487` n `12`; crypto_alt avg `-0.2934` n `233`; crypto_major avg `0.5496` n `8`; equity avg `-1.312` n `136`; fx avg `0.0529` n `6`; index avg `-0.3202` n `26`; metal avg `-0.2217` n `20`; unknown avg `1.2268` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
