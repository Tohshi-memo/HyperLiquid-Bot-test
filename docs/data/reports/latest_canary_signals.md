# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T04:22:25.044600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.596` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4289` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.3648` n `230`; crypto_major avg `0.3337` n `8`; equity avg `0.0592` n `92`; fx avg `-0.0108` n `6`; index avg `-0.0023` n `25`; metal avg `0.0207` n `20`; unknown avg `0.4078` n `766`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.3016` n `230`; crypto_major avg `0.1248` n `8`; equity avg `-0.1938` n `92`; fx avg `0.001` n `6`; index avg `-0.0584` n `25`; metal avg `0.005` n `20`; unknown avg `0.9083` n `766`
- 4h: commodity avg `0.0436` n `12`; crypto_alt avg `-1.7788` n `230`; crypto_major avg `-1.8901` n `8`; equity avg `-2.1778` n `92`; fx avg `0.0589` n `6`; index avg `-0.4612` n `25`; metal avg `-0.2941` n `20`; unknown avg `4.8559` n `766`
- 24h: commodity avg `0.1213` n `12`; crypto_alt avg `-2.1221` n `230`; crypto_major avg `-1.2127` n `8`; equity avg `-2.4139` n `92`; fx avg `0.0345` n `6`; index avg `-0.5153` n `25`; metal avg `-0.4876` n `20`; unknown avg `-0.0902` n `741`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
