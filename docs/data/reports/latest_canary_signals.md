# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T17:07:50.733161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.0187` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5284` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.1132` n `231`; crypto_major avg `-0.1526` n `8`; equity avg `0.036` n `127`; fx avg `-0.005` n `6`; index avg `0.0061` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.0071` n `792`
- 1h: commodity avg `0.1055` n `12`; crypto_alt avg `0.5197` n `231`; crypto_major avg `0.6104` n `8`; equity avg `0.1375` n `127`; fx avg `0.0005` n `6`; index avg `0.0336` n `26`; metal avg `0.0377` n `20`; unknown avg `0.0243` n `792`
- 4h: commodity avg `0.1309` n `12`; crypto_alt avg `1.319` n `231`; crypto_major avg `1.8481` n `8`; equity avg `-0.1706` n `127`; fx avg `0.0025` n `6`; index avg `0.0216` n `26`; metal avg `0.3197` n `20`; unknown avg `0.1677` n `792`
- 24h: commodity avg `0.0782` n `12`; crypto_alt avg `4.2848` n `231`; crypto_major avg `5.0766` n `8`; equity avg `1.8666` n `127`; fx avg `-0.0639` n `6`; index avg `0.2435` n `26`; metal avg `0.1886` n `20`; unknown avg `0.9446` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
