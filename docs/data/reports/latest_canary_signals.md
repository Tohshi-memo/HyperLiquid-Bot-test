# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T06:52:29.958765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.1866` n `230`; crypto_major avg `-0.0994` n `8`; equity avg `0.1139` n `107`; fx avg `0.0364` n `6`; index avg `0.0195` n `25`; metal avg `0.027` n `20`; unknown avg `-0.0223` n `781`
- 1h: commodity avg `-0.0696` n `12`; crypto_alt avg `-0.2645` n `230`; crypto_major avg `-0.2244` n `8`; equity avg `0.206` n `107`; fx avg `0.0567` n `6`; index avg `0.0118` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.0174` n `765`
- 4h: commodity avg `-0.057` n `12`; crypto_alt avg `-0.4697` n `230`; crypto_major avg `-0.3313` n `8`; equity avg `0.8009` n `107`; fx avg `0.1034` n `6`; index avg `0.1097` n `25`; metal avg `0.0256` n `20`; unknown avg `-0.0589` n `764`
- 24h: commodity avg `0.3961` n `12`; crypto_alt avg `0.978` n `230`; crypto_major avg `1.1185` n `8`; equity avg `2.5688` n `107`; fx avg `0.0714` n `6`; index avg `0.2644` n `25`; metal avg `0.0212` n `20`; unknown avg `0.1632` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
