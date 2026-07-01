# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T16:22:26.758410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7237` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.5784` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7529` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `-0.1239` n `228`; crypto_major avg `-0.1845` n `8`; equity avg `-0.0459` n `88`; fx avg `0.0009` n `6`; index avg `0.0059` n `25`; metal avg `-0.0305` n `20`; unknown avg `-0.0057` n `763`
- 1h: commodity avg `-0.0239` n `12`; crypto_alt avg `0.0208` n `228`; crypto_major avg `0.0958` n `8`; equity avg `-0.1329` n `88`; fx avg `-0.0045` n `6`; index avg `-0.0334` n `25`; metal avg `0.0541` n `20`; unknown avg `0.1667` n `763`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `1.8392` n `228`; crypto_major avg `2.4764` n `8`; equity avg `-0.102` n `88`; fx avg `-0.0552` n `6`; index avg `-0.1733` n `25`; metal avg `0.7235` n `20`; unknown avg `1.0511` n `763`
- 24h: commodity avg `-0.727` n `12`; crypto_alt avg `2.3447` n `228`; crypto_major avg `2.4131` n `8`; equity avg `-0.102` n `88`; fx avg `-0.0182` n `6`; index avg `-0.3591` n `25`; metal avg `0.3582` n `20`; unknown avg `0.6689` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0458`, n `668`, weak_sample_signal
