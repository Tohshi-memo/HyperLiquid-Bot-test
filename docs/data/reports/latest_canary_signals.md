# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:09:46.362571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `0.3385` n `230`; crypto_major avg `0.0897` n `8`; equity avg `0.0002` n `121`; fx avg `0.0009` n `6`; index avg `-0.0148` n `25`; metal avg `-0.0204` n `20`; unknown avg `0.0131` n `793`
- 1h: commodity avg `-0.0547` n `12`; crypto_alt avg `0.4865` n `230`; crypto_major avg `0.3194` n `8`; equity avg `0.0406` n `121`; fx avg `-0.0011` n `6`; index avg `-0.0105` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.0543` n `793`
- 4h: commodity avg `-0.0855` n `12`; crypto_alt avg `-0.3621` n `230`; crypto_major avg `-0.0692` n `8`; equity avg `-0.0419` n `121`; fx avg `0.008` n `6`; index avg `-0.0509` n `25`; metal avg `0.027` n `20`; unknown avg `0.0732` n `793`
- 24h: commodity avg `0.0688` n `12`; crypto_alt avg `6.9937` n `230`; crypto_major avg `4.8706` n `8`; equity avg `0.8862` n `121`; fx avg `-0.0786` n `6`; index avg `0.1112` n `25`; metal avg `0.5298` n `20`; unknown avg `1.0632` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
