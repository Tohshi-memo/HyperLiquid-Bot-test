# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T04:06:18.144882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0922` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6336` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4963` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `-0.1106` n `8`; equity avg `-0.2256` n `92`; fx avg `0.0035` n `6`; index avg `-0.0297` n `25`; metal avg `-0.0108` n `20`; unknown avg `-0.1386` n `766`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.3497` n `230`; crypto_major avg `-0.4852` n `8`; equity avg `-0.3904` n `92`; fx avg `0.008` n `6`; index avg `-0.078` n `25`; metal avg `-0.0281` n `20`; unknown avg `0.2817` n `766`
- 4h: commodity avg `0.0762` n `12`; crypto_alt avg `-1.9672` n `230`; crypto_major avg `-2.016` n `8`; equity avg `-2.378` n `92`; fx avg `0.0827` n `6`; index avg `-0.5197` n `25`; metal avg `-0.3824` n `20`; unknown avg `5.491` n `766`
- 24h: commodity avg `0.123` n `12`; crypto_alt avg `-2.5102` n `230`; crypto_major avg `-1.6419` n `8`; equity avg `-2.4731` n `92`; fx avg `0.046` n `6`; index avg `-0.5016` n `25`; metal avg `-0.5038` n `20`; unknown avg `-0.1182` n `741`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
