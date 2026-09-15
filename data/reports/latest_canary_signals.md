# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T18:22:36.141822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0516` n `12`; crypto_alt avg `-0.4012` n `233`; crypto_major avg `-0.1968` n `8`; equity avg `-0.0533` n `137`; fx avg `0.0152` n `6`; index avg `-0.0032` n `27`; metal avg `0.0737` n `20`; unknown avg `0.8849` n `918`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `0.0958` n `233`; crypto_major avg `0.4066` n `8`; equity avg `-0.001` n `137`; fx avg `0.0047` n `6`; index avg `0.0262` n `27`; metal avg `0.1482` n `20`; unknown avg `0.4282` n `915`
- 4h: commodity avg `0.1644` n `12`; crypto_alt avg `-0.5124` n `233`; crypto_major avg `-0.5038` n `8`; equity avg `-0.5068` n `137`; fx avg `0.0182` n `6`; index avg `-0.0238` n `27`; metal avg `0.1832` n `20`; unknown avg `0.2244` n `889`
- 24h: commodity avg `0.4665` n `12`; crypto_alt avg `-3.0982` n `233`; crypto_major avg `-3.1584` n `8`; equity avg `-1.4385` n `137`; fx avg `0.2144` n `6`; index avg `-0.1645` n `27`; metal avg `0.1136` n `20`; unknown avg `0.9499` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
