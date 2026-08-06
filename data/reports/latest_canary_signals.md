# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T09:22:25.499765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.3181` n `230`; crypto_major avg `-0.1817` n `8`; equity avg `-0.0094` n `108`; fx avg `-0.0043` n `6`; index avg `0.0117` n `25`; metal avg `0.0496` n `20`; unknown avg `-0.0597` n `782`
- 1h: commodity avg `-0.102` n `12`; crypto_alt avg `-0.2294` n `230`; crypto_major avg `-0.0868` n `8`; equity avg `0.0867` n `108`; fx avg `-0.0244` n `6`; index avg `0.0121` n `25`; metal avg `0.1877` n `20`; unknown avg `0.0377` n `782`
- 4h: commodity avg `0.1171` n `12`; crypto_alt avg `-0.2075` n `230`; crypto_major avg `-0.4838` n `8`; equity avg `-0.4965` n `108`; fx avg `0.0702` n `6`; index avg `-0.0774` n `25`; metal avg `0.2245` n `20`; unknown avg `0.0475` n `750`
- 24h: commodity avg `-0.2673` n `12`; crypto_alt avg `-0.0417` n `230`; crypto_major avg `-0.4844` n `8`; equity avg `-1.5199` n `108`; fx avg `0.0097` n `6`; index avg `-0.3251` n `25`; metal avg `0.5653` n `20`; unknown avg `0.1585` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
