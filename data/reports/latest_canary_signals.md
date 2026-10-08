# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T21:22:28.714785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2601` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.0595` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0399` n `13`; crypto_alt avg `0.1625` n `235`; crypto_major avg `0.1958` n `8`; equity avg `-0.0183` n `150`; fx avg `-0.0059` n `6`; index avg `-0.0062` n `26`; metal avg `0.0048` n `20`; unknown avg `0.0921` n `1077`
- 1h: commodity avg `0.1493` n `13`; crypto_alt avg `0.0819` n `235`; crypto_major avg `0.3018` n `8`; equity avg `0.0142` n `150`; fx avg `-0.0047` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0134` n `20`; unknown avg `-0.122` n `1067`
- 4h: commodity avg `0.1768` n `13`; crypto_alt avg `2.6932` n `235`; crypto_major avg `2.2363` n `8`; equity avg `0.7568` n `150`; fx avg `0.0307` n `6`; index avg `0.103` n `26`; metal avg `-0.0238` n `20`; unknown avg `0.5212` n `1007`
- 24h: commodity avg `0.7124` n `13`; crypto_alt avg `-2.6779` n `235`; crypto_major avg `-3.4004` n `8`; equity avg `-2.7479` n `150`; fx avg `0.0563` n `6`; index avg `-0.3579` n `26`; metal avg `-0.0136` n `20`; unknown avg `6.095` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
