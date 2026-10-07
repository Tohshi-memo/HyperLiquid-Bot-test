# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T04:37:32.562208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3574` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0919` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0187` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5223` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0194` n `13`; crypto_alt avg `-0.2757` n `235`; crypto_major avg `-0.109` n `8`; equity avg `-0.0022` n `150`; fx avg `-0.0041` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0167` n `20`; unknown avg `-0.1088` n `1076`
- 1h: commodity avg `0.0443` n `13`; crypto_alt avg `-0.695` n `235`; crypto_major avg `-0.3004` n `8`; equity avg `0.0408` n `150`; fx avg `-0.0151` n `6`; index avg `-0.0029` n `26`; metal avg `0.0001` n `20`; unknown avg `-0.0392` n `1068`
- 4h: commodity avg `0.1656` n `13`; crypto_alt avg `-3.4272` n `235`; crypto_major avg `-2.1918` n `8`; equity avg `-0.6695` n `150`; fx avg `-0.0532` n `6`; index avg `-0.0999` n `26`; metal avg `-0.1731` n `20`; unknown avg `1.9659` n `1068`
- 24h: commodity avg `0.5149` n `13`; crypto_alt avg `-3.6049` n `235`; crypto_major avg `-2.6051` n `8`; equity avg `0.0221` n `149`; fx avg `0.0228` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0381` n `20`; unknown avg `871.2612` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1879`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
