# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T13:52:33.237970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1173` n `12`; crypto_alt avg `0.8181` n `230`; crypto_major avg `0.8432` n `8`; equity avg `0.1823` n `121`; fx avg `0.0083` n `6`; index avg `0.0171` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0439` n `793`
- 1h: commodity avg `-0.0907` n `12`; crypto_alt avg `0.2505` n `230`; crypto_major avg `0.8632` n `8`; equity avg `-0.281` n `121`; fx avg `-0.0078` n `6`; index avg `-0.1171` n `25`; metal avg `0.0131` n `20`; unknown avg `1.1544` n `793`
- 4h: commodity avg `-0.008` n `12`; crypto_alt avg `1.7312` n `230`; crypto_major avg `0.0828` n `8`; equity avg `-0.2451` n `121`; fx avg `-0.0157` n `6`; index avg `-0.0716` n `25`; metal avg `0.0297` n `20`; unknown avg `1.3787` n `793`
- 24h: commodity avg `0.1196` n `12`; crypto_alt avg `8.4457` n `230`; crypto_major avg `7.0922` n `8`; equity avg `1.7736` n `121`; fx avg `-0.095` n `6`; index avg `0.0922` n `25`; metal avg `0.8675` n `20`; unknown avg `3.563` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2345`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
