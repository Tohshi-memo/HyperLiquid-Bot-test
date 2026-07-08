# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T04:37:25.749182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.865` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7285` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4924` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0142` n `12`; crypto_alt avg `-0.1792` n `229`; crypto_major avg `-0.2017` n `8`; equity avg `-0.329` n `91`; fx avg `-0.0058` n `6`; index avg `-0.1034` n `25`; metal avg `0.0208` n `20`; unknown avg `0.0183` n `763`
- 1h: commodity avg `-0.0362` n `12`; crypto_alt avg `-0.3439` n `229`; crypto_major avg `-0.353` n `8`; equity avg `-0.7434` n `91`; fx avg `-0.0069` n `6`; index avg `-0.2307` n `25`; metal avg `-0.0471` n `20`; unknown avg `-0.1654` n `763`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `-1.5004` n `229`; crypto_major avg `-1.6717` n `8`; equity avg `0.0568` n `91`; fx avg `-0.0762` n `6`; index avg `-0.1793` n `25`; metal avg `0.1933` n `20`; unknown avg `0.3176` n `763`
- 24h: commodity avg `0.9123` n `12`; crypto_alt avg `-2.5368` n `229`; crypto_major avg `-1.8492` n `8`; equity avg `-1.1437` n `91`; fx avg `-0.1829` n `6`; index avg `-0.2282` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.3485` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
