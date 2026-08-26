# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T23:52:24.862158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0958` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9145` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.3553` n `231`; crypto_major avg `0.384` n `8`; equity avg `0.0894` n `124`; fx avg `-0.0145` n `6`; index avg `0.0298` n `25`; metal avg `0.0062` n `20`; unknown avg `0.1064` n `795`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `0.8846` n `231`; crypto_major avg `1.0373` n `8`; equity avg `0.1458` n `124`; fx avg `-0.0016` n `6`; index avg `0.0181` n `25`; metal avg `0.0695` n `20`; unknown avg `0.2285` n `795`
- 4h: commodity avg `0.0158` n `12`; crypto_alt avg `2.3315` n `231`; crypto_major avg `2.1116` n `8`; equity avg `1.8813` n `124`; fx avg `-0.0212` n `6`; index avg `0.3131` n `25`; metal avg `0.1971` n `20`; unknown avg `0.808` n `795`
- 24h: commodity avg `0.3131` n `12`; crypto_alt avg `2.3387` n `231`; crypto_major avg `2.0455` n `8`; equity avg `1.8668` n `124`; fx avg `-0.0649` n `6`; index avg `0.4026` n `25`; metal avg `-0.1802` n `20`; unknown avg `1.0989` n `778`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
