# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T12:37:24.000577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0413` n `230`; crypto_major avg `-0.0549` n `8`; equity avg `0.0095` n `102`; fx avg `0.0082` n `6`; index avg `-0.0013` n `25`; metal avg `0.0173` n `20`; unknown avg `-0.0191` n `782`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `0.0505` n `230`; crypto_major avg `-0.0793` n `8`; equity avg `0.0304` n `102`; fx avg `0.0195` n `6`; index avg `0.0159` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0243` n `782`
- 4h: commodity avg `0.1583` n `12`; crypto_alt avg `-0.1819` n `230`; crypto_major avg `-0.3955` n `8`; equity avg `-0.3211` n `102`; fx avg `0.0129` n `6`; index avg `-0.0699` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.0506` n `782`
- 24h: commodity avg `-1.0692` n `12`; crypto_alt avg `0.1596` n `230`; crypto_major avg `0.0698` n `8`; equity avg `0.7596` n `102`; fx avg `-0.0612` n `6`; index avg `0.1917` n `25`; metal avg `0.2441` n `20`; unknown avg `0.2291` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
