# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T00:22:33.561346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2543` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0476` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.0675` n `231`; crypto_major avg `-0.1146` n `8`; equity avg `-0.3178` n `124`; fx avg `-0.027` n `6`; index avg `-0.0376` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.0653` n `795`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.3796` n `231`; crypto_major avg `0.2535` n `8`; equity avg `-0.1816` n `124`; fx avg `-0.0473` n `6`; index avg `-0.0474` n `25`; metal avg `-0.0145` n `20`; unknown avg `0.0155` n `795`
- 4h: commodity avg `0.0156` n `12`; crypto_alt avg `2.6853` n `231`; crypto_major avg `2.2699` n `8`; equity avg `1.6104` n `124`; fx avg `-0.05` n `6`; index avg `0.2568` n `25`; metal avg `0.2223` n `20`; unknown avg `1.0977` n `795`
- 24h: commodity avg `0.3449` n `12`; crypto_alt avg `2.1232` n `231`; crypto_major avg `1.6647` n `8`; equity avg `1.47` n `124`; fx avg `-0.1171` n `6`; index avg `0.3083` n `25`; metal avg `-0.1891` n `20`; unknown avg `1.0817` n `778`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
