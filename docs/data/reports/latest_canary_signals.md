# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T14:52:31.898739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.3316` n `230`; crypto_major avg `-0.3759` n `8`; equity avg `-0.1971` n `112`; fx avg `0.0023` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0298` n `20`; unknown avg `0.0218` n `782`
- 1h: commodity avg `0.1232` n `12`; crypto_alt avg `-0.4942` n `230`; crypto_major avg `-0.4601` n `8`; equity avg `-0.3438` n `112`; fx avg `0.0109` n `6`; index avg `-0.0628` n `25`; metal avg `-0.0844` n `20`; unknown avg `0.0472` n `782`
- 4h: commodity avg `0.3232` n `12`; crypto_alt avg `-0.3799` n `230`; crypto_major avg `-0.1421` n `8`; equity avg `-0.2114` n `112`; fx avg `-0.015` n `6`; index avg `-0.0182` n `25`; metal avg `-0.1508` n `20`; unknown avg `-0.0314` n `782`
- 24h: commodity avg `0.4479` n `12`; crypto_alt avg `-0.5051` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `0.3162` n `109`; fx avg `-0.1239` n `6`; index avg `-0.1208` n `25`; metal avg `0.2075` n `20`; unknown avg `0.0124` n `765`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
