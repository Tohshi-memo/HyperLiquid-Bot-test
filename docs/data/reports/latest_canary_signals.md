# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T21:22:25.084337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7264` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6928` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3777` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_commodity_crypto_divergence: score `-2.2882` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.2774` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-2.0264` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0009` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.7161` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `-0.5019` n `239`; crypto_major avg `-0.6572` n `8`; equity avg `0.0621` n `162`; fx avg `0.012` n `6`; index avg `0.0066` n `27`; metal avg `0.0763` n `20`; unknown avg `5.0654` n `1260`
- 1h: commodity avg `-0.023` n `13`; crypto_alt avg `-2.2138` n `239`; crypto_major avg `-2.3112` n `8`; equity avg `-0.5951` n `162`; fx avg `0.0074` n `6`; index avg `-0.0338` n `27`; metal avg `-0.2848` n `20`; unknown avg `40.6928` n `1232`
- 4h: commodity avg `-0.0034` n `13`; crypto_alt avg `-3.6994` n `239`; crypto_major avg `-2.7298` n `8`; equity avg `-0.7289` n `162`; fx avg `0.0118` n `6`; index avg `-0.037` n `27`; metal avg `-0.3521` n `20`; unknown avg `0.4069` n `1214`
- 24h: commodity avg `-0.1308` n `13`; crypto_alt avg `-9.4841` n `239`; crypto_major avg `-8.5144` n `8`; equity avg `-2.092` n `162`; fx avg `-0.0122` n `6`; index avg `-0.1466` n `27`; metal avg `-0.5646` n `20`; unknown avg `0.3622` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
