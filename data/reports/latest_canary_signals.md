# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T12:52:21.442983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3732` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `0.2338` n `228`; crypto_major avg `0.13` n `8`; equity avg `0.0798` n `74`; fx avg `0.0008` n `6`; index avg `0.0129` n `23`; metal avg `0.0249` n `18`; unknown avg `0.1728` n `516`
- 1h: commodity avg `0.128` n `12`; crypto_alt avg `-1.2133` n `228`; crypto_major avg `-1.0465` n `8`; equity avg `-0.2016` n `74`; fx avg `0.0066` n `6`; index avg `-0.0887` n `23`; metal avg `-0.1595` n `18`; unknown avg `-0.091` n `516`
- 4h: commodity avg `0.2163` n `12`; crypto_alt avg `-1.8096` n `228`; crypto_major avg `-1.6555` n `8`; equity avg `-0.2445` n `74`; fx avg `-0.0053` n `6`; index avg `-0.2823` n `23`; metal avg `-0.3032` n `18`; unknown avg `-3.5283` n `516`
- 24h: commodity avg `0.2083` n `12`; crypto_alt avg `1.304` n `228`; crypto_major avg `1.183` n `8`; equity avg `1.3165` n `74`; fx avg `0.0302` n `6`; index avg `0.3521` n `23`; metal avg `0.3502` n `18`; unknown avg `-0.1497` n `405`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
