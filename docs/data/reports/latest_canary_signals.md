# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T14:22:28.638668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0596` n `12`; crypto_alt avg `0.0196` n `230`; crypto_major avg `0.1288` n `8`; equity avg `0.1199` n `112`; fx avg `0.0139` n `6`; index avg `-0.016` n `25`; metal avg `0.0791` n `20`; unknown avg `-0.0273` n `782`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.1736` n `230`; crypto_major avg `-0.3766` n `8`; equity avg `-1.0698` n `112`; fx avg `0.0348` n `6`; index avg `-0.1468` n `25`; metal avg `-0.0602` n `20`; unknown avg `0.1106` n `782`
- 4h: commodity avg `0.2185` n `12`; crypto_alt avg `-0.2218` n `230`; crypto_major avg `0.0741` n `8`; equity avg `-0.0652` n `112`; fx avg `-0.0105` n `6`; index avg `0.0091` n `25`; metal avg `-0.1095` n `20`; unknown avg `-0.022` n `782`
- 24h: commodity avg `0.4376` n `12`; crypto_alt avg `-0.0047` n `230`; crypto_major avg `0.2477` n `8`; equity avg `0.2237` n `109`; fx avg `-0.151` n `6`; index avg `-0.1316` n `25`; metal avg `0.3175` n `20`; unknown avg `0.0591` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
