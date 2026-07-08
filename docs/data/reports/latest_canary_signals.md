# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T02:22:30.557314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.1801` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.6349` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5807` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5709` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.3755` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `-0.2154` n `229`; crypto_major avg `-0.2368` n `8`; equity avg `0.1462` n `91`; fx avg `0.0268` n `6`; index avg `0.0424` n `25`; metal avg `0.0155` n `20`; unknown avg `-0.0943` n `763`
- 1h: commodity avg `0.1426` n `12`; crypto_alt avg `-1.5329` n `229`; crypto_major avg `-1.4903` n `8`; equity avg `-0.3116` n `91`; fx avg `-0.0179` n `6`; index avg `-0.1148` n `25`; metal avg `0.0806` n `20`; unknown avg `0.3614` n `763`
- 4h: commodity avg `0.0251` n `12`; crypto_alt avg `-1.2266` n `229`; crypto_major avg `-1.5311` n `8`; equity avg `0.649` n `91`; fx avg `0.0189` n `6`; index avg `0.0496` n `25`; metal avg `0.1038` n `20`; unknown avg `-0.155` n `763`
- 24h: commodity avg `0.8217` n `12`; crypto_alt avg `-3.4439` n `229`; crypto_major avg `-2.7522` n `8`; equity avg `-1.788` n `91`; fx avg `-0.1999` n `6`; index avg `-0.2536` n `25`; metal avg `-0.3682` n `20`; unknown avg `-0.3906` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
