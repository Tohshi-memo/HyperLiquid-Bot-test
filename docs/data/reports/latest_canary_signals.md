# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T08:52:31.026023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3242` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0232` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7793` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7381` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0763` n `12`; crypto_alt avg `-0.8908` n `234`; crypto_major avg `-0.8479` n `8`; equity avg `-0.1844` n `140`; fx avg `-0.0188` n `6`; index avg `-0.0122` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.2028` n `945`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.5597` n `234`; crypto_major avg `-0.9195` n `8`; equity avg `-0.1515` n `140`; fx avg `-0.0262` n `6`; index avg `-0.0243` n `26`; metal avg `-0.0329` n `20`; unknown avg `0.8167` n `937`
- 4h: commodity avg `0.2668` n `12`; crypto_alt avg `-0.9922` n `234`; crypto_major avg `-2.0574` n `8`; equity avg `-0.3193` n `140`; fx avg `0.1454` n `6`; index avg `-0.0342` n `26`; metal avg `-0.2781` n `20`; unknown avg `1.4032` n `921`
- 24h: commodity avg `0.5117` n `12`; crypto_alt avg `2.1637` n `234`; crypto_major avg `-0.0129` n `8`; equity avg `1.0968` n `140`; fx avg `0.0585` n `6`; index avg `0.1129` n `26`; metal avg `-0.1091` n `20`; unknown avg `1.6494` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
