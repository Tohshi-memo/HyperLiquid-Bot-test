# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:37:23.817672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.0256` n `230`; crypto_major avg `0.0464` n `8`; equity avg `-0.0044` n `121`; fx avg `-0.0018` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0311` n `20`; unknown avg `0.0368` n `793`
- 1h: commodity avg `-0.0706` n `12`; crypto_alt avg `-0.9962` n `230`; crypto_major avg `-0.3448` n `8`; equity avg `0.1186` n `121`; fx avg `0.0007` n `6`; index avg `0.007` n `25`; metal avg `-0.0343` n `20`; unknown avg `1.0172` n `793`
- 4h: commodity avg `-0.0556` n `12`; crypto_alt avg `-0.878` n `230`; crypto_major avg `-0.5326` n `8`; equity avg `-0.0513` n `121`; fx avg `0.032` n `6`; index avg `-0.0377` n `25`; metal avg `0.0206` n `20`; unknown avg `1.1825` n `793`
- 24h: commodity avg `0.1014` n `12`; crypto_alt avg `6.5319` n `230`; crypto_major avg `4.8513` n `8`; equity avg `1.0256` n `121`; fx avg `-0.0926` n `6`; index avg `0.1029` n `25`; metal avg `0.5278` n `20`; unknown avg `2.2173` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
